from HeightsNotCycledGraph import HeightsGraph
from expections import GraphException


def calc_heights_in_graph(matrix: list):
    try:
        graph = HeightsGraph(matrix)
        graph.calc_all_heights()
        return {'matrix': graph.matrix}
    except GraphException as e:
        return {'error': e.args[0]}, 400
