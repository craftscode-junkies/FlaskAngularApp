from flask_restful import Resource
import logging as logger
from flask import  request ,json
from pymongo import MongoClient
from bson.json_util import dumps





client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.angularquiz #Select the database
question = db.questions

class Question (Resource):

    def get(self):
        logger.debug("inside get method")
        result = question.find()
        res = dumps(result)
        r = json.loads(res)
        logger.debug(r)
        return r,200

    def post(self):
        logger.debug("inside post method")
        data = json.loads(request.data)
        logger.debug(type(data))
        question.insert(data)
        return request.json,200


    def put(self):
        logger.debug("inside put method")
        return {"message": "inside put method"},200



    def delete(self):
        logger.debug("inside delete method")
        return {"message": "inside put method"},200
