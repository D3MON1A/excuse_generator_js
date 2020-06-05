"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
import random
#from models import Person

api = Blueprint('api', __name__)

#@api.route('/hello', methods=['POST', 'GET'])
#def handle_hello():

@api.route('/excuse', methods=['GET'])
def getrandomexecuse():

    response_body = {
        "hello": "world"
    }
    excuse = ("I cant trust my eyes,", "Oh Lord,", "Believe it or not but,")
    who = ("My Dog", "My Son", "The Cat")
    action = ("ate", "ran over", "punched")
    what = ("the pillow", "the pool", "my car tire")
    when = ("yesterday", "today", "on sunday")

    #return jsonify(response_body), 200 
    temporary = random.randint(0,2)
    excuse= who[temporary]+" "+action[temporary] +" "+what[temporary]+" "+when[temporary]


    return jsonify(excuse), 200 