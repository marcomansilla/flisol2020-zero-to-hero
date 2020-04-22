from flask import request, jsonify
from flask_restful import Resource
from pymongo import MongoClient

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
        pass


class Contacts(Resource):
    def get(self):
        pass
