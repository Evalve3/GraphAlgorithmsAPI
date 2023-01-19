from flask import Flask
from flask_restful import Api, Resource, reqparse
from AdjacencyMatrix import HeightsNotCycledGraph
from IncidenceMatrix import FindOrMakeChane

app = Flask(__name__)
api = Api(app)


def is_matrix(matrix):
    return all(map(lambda x: isinstance(x, list), matrix))


class Algorithms(Resource):
    algorithms_dict = {'heights': HeightsNotCycledGraph.HeightsGraph.get_request,
                       'chainGraph': FindOrMakeChane.ChaneCreate.get_request}

    def get(self, algorithm: str):
        parser = reqparse.RequestParser()
        parser.add_argument('matrix', type=list, location='json')
        matrix = (parser.parse_args()['matrix'])

        if not is_matrix(matrix):
            return {"error": "Это не матрица"}, 400

        if algorithm in self.algorithms_dict:
            return self.algorithms_dict[algorithm](matrix)

        return {"error": "Такого алгоритма нет",
                "algorithm list": str([key for key in self.algorithms_dict.keys()])}, 404


api.add_resource(Algorithms, "/algorithms/<string:algorithm>")
if __name__ == '__main__':
    app.run(debug=True)
