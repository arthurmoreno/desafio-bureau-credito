from flask import Flask
from flask_restful import Resource, Api

from base_a.manager import Manager

app = Flask(__name__)
api = Api(app)

class Person(Resource):
    def get(self, cpf):
        manager = Manager()
        people = manager.get_people(cpf)
        return {
            'cpf': people.cpf,
            'name': people.name,
            'address': people.address
        }

api.add_resource(Person, '/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True)