from flask import Flask
from flask_restful import Api
from routes import Contact, Contacts

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'index page'

api.add_resource(Contact, '/contact')
api.add_resource(Contacts, '/contacts')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
