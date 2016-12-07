import unittest

from naiwny import naive_strongly_connected_components, dfs_scc, dfs_back

def path(n):
    graph = [[i] for i in range(1, n+1)]
    graph[n-1] = []
    return graph

class NaiveTests(unittest.TestCase):
    def test_trivial_graph(self):
        graph = [[]]

        result = naive_strongly_connected_components(graph)

        self.assertEqual(result, [1])

    def test_three_separated_vertices(self):
        graph = [[], [], []]

        result = naive_strongly_connected_components(graph)

        self.assertCountEqual(result, [1, 2, 3])

    def test_path(self):
        graph = [[1], [2], [3], [4], []]

        result = naive_strongly_connected_components(graph)

        self.assertCountEqual(result, [1, 2, 3, 4, 5])

    def test_very_long_path(self):
        n = 10000

        result = naive_strongly_connected_components(path(n))

        self.assertCountEqual(result, range(1, n+1))
