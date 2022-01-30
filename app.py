from flask import Flask, request
from flask_cors import CORS, cross_origin

from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from newsapi import NewsApiClient





app = Flask(__name__)
api = Api(app)
CORS(app)

qu = ""


@app.route('/')
def hello():
    return "Its working"





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
