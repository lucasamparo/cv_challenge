from flask import Flask,Response
import json
from flask_restplus import Api, Resource, fields
from service.BlackHoleService import findBlackHole


app = Flask(__name__)
api = Api(app)


info = api.model('InfoCoordenates', {
    'numberOfTeste': fields.Integer(min=1, max=10000, example=3),
    'coordenates': fields.List(fields.List(fields.Float(min=-10000.0, max=1000.0), min_items=2, max_items=2), example=[
            [12.00, 2.00],
            [5.00, 6.00],
            [10.00, 8.00],
            [2.00, 7.00],
            [0.50, -0.50],
            [-1.00, 0.00],
            [-0.50, -0.50],
            [0.00, 1.00],
            [0.50, 6.50],
            [-10.50, -3.50],
            [-1.50, 6.50],
            [-5.50, -8.50]
        ])
})



class FindBlackHole(Resource):
    @api.expect(info)
    def post(self):
        return Response(json.dumps(findBlackHole(api.payload['numberOfTeste'],api.payload['coordenates'])), mimetype='application/json')

api.add_resource(FindBlackHole, '/findBlackHole')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')