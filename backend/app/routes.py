from flask import request, jsonify
from flask_restful import Resource
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import json

client = MongoClient('mongodb://db:27017', username='root', password='root')
db = client.Contactos
contactos = db['contactos']


class ContactById(Resource):
    def get(self, id):
        resultado = contactos.find_one({'_id': ObjectId(id)})
        return json.loads(dumps(resultado))


class Contact(Resource):
    def post(self):
        data = request.get_json()

        nombre = data['nombre']
        apellido = data['apellido']
        direccion = data['direccion']
        telefono = data['telefono']
        cumple = data['cumple']
        email = data['email']

        contactos.insert({
            'nombre': nombre,
            'apellido': apellido,
            'direccion': direccion,
            'telefono': telefono,
            'cumple': cumple,
            'email': email
        })

        return jsonify({'status': 200,
                        'message': 'El contacto se ha agregado exitosamente'})

    def put(self):
        data = request.get_json()

        nombre = data['nombre']
        apellido = data['apellido']
        direccion = data['direccion']
        telefono = data['telefono']
        cumple = data['cumple']
        email = data['email']

        resultado = contactos.find_one_and_update({
            '_id': ObjectId(data['_id']['$oid'])
        },
                                                  {
            '$set': {
                'nombre': nombre,
                'apellido': apellido,
                'direccion': direccion,
                'telefono': telefono,
                'cumple': cumple,
                'email': email}
        }, return_document=True)

        return json.loads(dumps(resultado))

    def delete(self):
        id = request.get_json()['id']
        resultado = contactos.delete_one({'_id': ObjectId(id)})
        return jsonify({'resultado': resultado.deleted_count})


class Contacts(Resource):
    def get(self):
        resultado = [json.loads(dumps(doc)) for doc in contactos.find()]
        return resultado
