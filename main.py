from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, unliked_articles, did_not_read
from demographic_filtering import output
from content_filtering import get_recommendations
from flask_cors import CORS
import csv
with open('articles.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
liked_articles = []
not_liked_articles = []
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":all_articles[0],
        "message":"success"
    }),200
@app.route("/get-articles")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })
@app.route("/liked-articles", methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-articles", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201
@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "title": article[12],
            "poster_link": article[11],
            "rating": article[4],
            "overview": article[5]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if(__name__=="__main__"):
    app.run(debug = True)
    
@app.route("/recommended-articles")
def recommended_articles():
   all_recommended = []
   for liked_article in liked_articles:
       output = get_recommendations(liked_article[19])
       for data in output:
           all_recommended.append(data)
   import itertools
   all_recommended.sort()
   all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
   article_data = []
   for recommended in all_recommended:
       _d = {
           "title": recommended[0],
           "rating": recommended[4],
           "meta": recommended[18]
       }
       article_data.append(_d)
   return jsonify({
       "data": article_data,
       "status": "success"
   }), 200