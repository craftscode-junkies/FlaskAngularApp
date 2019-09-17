from flask_restful import Api
from app import angularQuiz
from .Question import  Question

restServer = Api(angularQuiz)

restServer.add_resource(Question,"/api/v1.0/question")