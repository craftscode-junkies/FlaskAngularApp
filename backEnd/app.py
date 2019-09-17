from flask import Flask, jsonify, request
import logging as logger
from flask_pymongo import PyMongo
logger.basicConfig(level="DEBUG")

angularQuiz = Flask(__name__)
angularQuiz.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(angularQuiz)

if __name__ == '__main__':
    logger.debug("starting app")
    from api import *
    angularQuiz.run(host="127.0.0.1",port=5000,debug=True)
