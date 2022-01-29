from flask import Flask, request
from flask_cors import CORS, cross_origin
import pandas as pd
import pickle
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from newsapi import NewsApiClient


# Spliting the data
from sklearn.utils import shuffle
# For finding out keywords
from sklearn.feature_extraction.text import CountVectorizer

# For checking similarity of our note with the articles available
from sklearn.metrics.pairwise import cosine_similarity

model = pickle.load(open('d:/Works/Modeling/mine_attempt/achar101.pkl', 'rb'))
tfidf = pickle.load(open('d:/Works/Modeling/mine_attempt/tf101.pkl', 'rb'))

tech_csv = pd.read_csv('d:/machine learning/articles/categorisation/tech.csv')
politics_csv = pd.read_csv(
    'd:/machine learning/articles/categorisation/politics.csv')
sports_csv = pd.read_csv(
    'd:/machine learning/articles/categorisation/sport.csv')
biz_csv = pd.read_csv('d:/machine learning/articles/categorisation/biz.csv')
others_csv = pd.read_csv(
    'd:/machine learning/articles/categorisation/others.csv')


app = Flask(__name__)
api = Api(app)
CORS(app)

qu = ""


@app.route('/')
def hello():
    return "Its working"


@app.route("/query", methods=["POST"])
def receiveQuery():
    query = request.data
    global qu
    qu = query
    features = []
    features.append(query)
    notes_list = [
        "You won't guess what the latest trend in data analysis is!",
    "Hello hello",
    "This is Shahrukh khan dancing",
        "I",
        "I like to eat apples",
        "10 popular JS IDEs for java developers",
        "Dance was good!",
        "Stock prices have risen",
         "I have to complete my machine learning project in time",
         "Electronic have large usage now a days",
         "The Indian team won by 2 wickets and 45 run.",
         "The dancing show was awesome!",
         " wireless",
    "hey this is me swirling through my project and I am happy to play games and bet money on share stocks business",
         "The Samsung galaxy S10+ seems address a lot of issues that users have with their existing devices. ",
         "Loosing yourself in online gaming",
         "Machine learning is fun!",
    "I love to sing ",
    "I like pubg",
  "Today it will get you nearer €1.14. It has suffered a similar fate against most major currencies, losing about 15% of its value over that time", "Rohan has been on lot of shows and is a famous celebrity.",
        "Sachin tendulkar is a great batsman",
'''A high voter turnout, including over 80 per cent in Assam, was recorded in the third and largest phase of Lok Sabha elections Tuesday covering 116 constituencies amid complaints of EVM malfunctioning in many states and killing of a man outside a booth in West Bengal.

Election Commission officials in Delhi put the voting percentage at 65.61 at 8 pm. Final figures are likely to change as queues of voters were seen at several centres even after the scheduled time for voting ended.


Polling was also held in Anantnag seat in Jammu and Kashmir which saw a turnout of 13.61 per cent. Elections for this seat are being conducted in three phases. The driver of a vehicle carrying ITBP troops back from their poll duty in Kokarnag area of south Kashmir was killed as it overturned after a mob hurled stones at it, officials said. With Tuesday's polling, voting has been held in 302 Lok Sabha constituencies apart from Anantnag.


In Gujarat, a turnout of 63.67 per cent was registered for the 26 seats. Key political leaders, including Prime Minister Narendra Modi, BJP president Amit Shah, party veteran L K Advani, Union Finance Minister Arun Jaitley and Congress leader Ahmed Patel cast their votes at different places in the state. Shah is contesting from Gandhinagar seat.
''']
    text_features = tfidf.transform(features)
    predictions = model.predict(text_features)
    for text, predicted in zip(features, predictions):
        print('"{}"'.format(text))
        print("  - Predicted as: '{}'".format(predicted))

    return jsonify(predictions[0])


@app.route("/recommend", methods=["POST"])
def getRecommendations():

    global qu
    # print("query",qu)
    a = request.get_json()
    # a=request.get_json(force=True)
    print("receiving",a)
    cn='in'
    # secret='52c11279b478428daeaf4bfecc1c684a'
    secret="3f79f5996fd54c7cad134baba6f8c06a"
    top="https://newsapi.org/v2/top-headlines?country="+ cn+"&apiKey="+secret
    


    print("query type", type(a))
    print("query", a)
    
    
    # print("ar", ar)

    links=[]

    
    # return qu
    # news_api=NewsApiClient(api_key=secret)
    # all_articles = news_api.get_everything(q=str(qu))
    # Define the endpoint
    url = 'https://newsapi.org/v2/everything?'
    # Specify the query and number of returns
    parameters = {
    'q': "", # query phrase
    'pageSize': 10,
      # maximum is 100
    'apiKey': secret # your own API key
    
    }
    
    for i in a:
        import requests
        parameters["q"]=i
        response = requests.get(url, params=parameters)
        response_json = response.json()
        links.append(response_json)
    return jsonify(links) 
        
    # Make the request
    
    # Convert the response to JSON format and pretty print it
    
    # print(response)
    # print("from direct api",all_articles)
    


if __name__  == '__main__':
    app.run(port=5300,debug=True)
    # app.run(debug=True)
