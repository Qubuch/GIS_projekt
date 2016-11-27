import unittest

from kosaraju import kosaraju_strongly_connected_components, transpose_graph


def path(n):
    graph = [[i] for i in range(1, n+1)]
    graph[n-1] = []
    return graph


class KosarajuTests(unittest.TestCase):
    def test_trivial_graph(self):
        graph = [[]]

        result = kosaraju_strongly_connected_components(graph)

        self.assertEqual(result, [1])

    def test_three_separated_vertices(self):
        graph = [[], [], []]

        result = kosaraju_strongly_connected_components(graph)

        self.assertCountEqual(result, [1, 2, 3])

    def test_path(self):
        graph = [[1], [2], [3], [4], []]

        result = kosaraju_strongly_connected_components(graph)

        self.assertCountEqual(result, [1, 2, 3, 4, 5])

    def test_very_long_path(self):
        n = 1000000

        result = kosaraju_strongly_connected_components(path(n))

        self.assertCountEqual(result, range(1, n+1))


class TransposeGraphTests(unittest.TestCase):
    def test_transpose_trivial_graph(self):
        graph = [[]]

        result = transpose_graph(graph)

        self.assertEqual(result, graph)

    def test_transpose_path(self):
        graph = [[1], [2], [3], [4], []]

        result = transpose_graph(graph)

        self.assertEqual(result, [[], [0], [1], [2], [3]])
