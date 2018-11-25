from os import environ

from bson import json_util
from bson.objectid import ObjectId, InvalidId
from flask import Flask, jsonify, make_response
from flask_pymongo import PyMongo

from src.mongoflask import MongoJSONEncoder, ObjectIdConverter, find_restaurants

app = Flask(__name__)
app.config["MONGO_URI"] = environ.get("MONGO_URI")
app.json_encoder = MongoJSONEncoder
app.url_map.converters["objectid"] = ObjectIdConverter
mongo = PyMongo(app)

def jsonify_no_content():
    response = make_response('', 204)
    return response

@app.route("/api/v1/restaurant")
def restaurants():
    restaurants = find_restaurants(mongo)
    return jsonify(restaurants)


@app.route("/api/v1/restaurant/<id>")
def restaurant(id):
    try:
        restaurant, = find_restaurants(mongo, id)
        return jsonify(restaurant)
    except (ValueError, InvalidId) as ex:
        print("{}".format(ex))
        return jsonify_no_content()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8080)
