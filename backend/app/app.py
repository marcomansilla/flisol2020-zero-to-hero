from flask import Flask
from flask_restful import Api
from routes import Contact, ContactById, Contacts

app = Flask(__name__)
api = Api(app)

api.add_resource(Contact, '/api/contact')
api.add_resource(ContactById, '/api/contact/<id>')
api.add_resource(Contacts, '/api/contacts')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
