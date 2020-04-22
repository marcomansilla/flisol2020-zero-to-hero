from flask import request, jsonify
from flask_restful import Resource
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import json

client = MongoClient('mongodb://db:27017', username='root', password='root')
db = client.Contactos
contactos = db['contactos']


class Contact(Resource):
    def get(self):
        pass

    def post(self):
        data = request.get_json()
        print(data)
        nombre = data['nombre']
        apellido = data['apellido']
        direccion = data['direccion']
        telefono = data['telefono']
        cumple = data['cumple']

        contactos.insert({
            'nombre': nombre,
            'apellido': apellido,
            'direccion': direccion,
            'telefono': telefono,
            'cumple': cumple,
        })

        return jsonify({'status': 200,
                        'message': 'El contacto se ha agregado exitosamente'})

    def put(self):
        pass

    def delete(self):
        id = request.get_json()['id']
        resultado =  contactos.delete_one({'_id': ObjectId(id)})
        return jsonify({'resultado': resultado.deleted_count})


class Contacts(Resource):
    def get(self):
        resultado = [json.loads(dumps(doc)) for doc in contactos.find()]
        return resultado
