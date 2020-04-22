from flask import request
from flask_restful import Resource
from pymongo import MongoClient

client = MongoClient('mongodb://db:27017')
db = client.ContactList
contacts = db['contacts']


class Contact(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class Contacts(Resource):
    def get(self):
        pass
