from flask import Flask
from flask_restful import Resource, Api

from base_a.manager import Manager

app = Flask(__name__)
api = Api(app)

class Person(Resource):
    def get(self, cpf):
        manager = Manager()
        person = manager.get_person(cpf)

        payload = {
            'cpf': person.cpf,
            'name': person.name,
            'address': person.address,
            'dividas': [{
                'company': divida.company,
                'value': divida.value,
                'status': divida.status,
                'contract': divida.contract
            } for divida in person.dividas]
        }
        return payload

api.add_resource(Person, '/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True)