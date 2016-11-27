import unittest
from functools import partial

from depth_first_search import depth_first_search, postorder_depth_first_search


class DfsTest(unittest.TestCase):
    def test_start_node_must_exist_in_graph(self):
        graph = [[], [], []]
        with self.assertRaises(AssertionError):
            list(depth_first_search(graph, 3))

    def test_trivial_graph(self):
        trivial_graph = [[]]

        result = depth_first_search(trivial_graph, 0)

        self.assertEqual(list(result), [0])

    def test_simple_path(self):
        path = [[1], [2], [3], [4], []]

        result = depth_first_search(path, 0)

        self.assertEqual(list(result), [0, 1, 2, 3, 4])

    def test_simple_cycle(self):
        cycle = [[1], [2], [3], [4], [0]]

        result = depth_first_search(cycle, 0)

        self.assertEqual(list(result), [0, 1, 2, 3, 4])

    def test_binary_tree(self):
        binary_tree = [[1, 5], [2, 3], [], [4], [], [6], []]

        result = depth_first_search(binary_tree, 0)

        dfs_order_index = [None] * len(binary_tree)
        for index, node in enumerate(result):
            dfs_order_index[node] = index

        assert_comes_after = partial(self.assert_comes_after, dfs_order_index)
        assert_comes_immediately_after = partial(self.assert_comes_immediately_after, dfs_order_index)
        assert_comes_after(0, 1)
        assert_comes_after(0, 5)
        assert_comes_after(1, 2)
        assert_comes_after(1, 3)
        assert_comes_immediately_after(3, 4)
        assert_comes_immediately_after(5, 6)

    def assert_comes_after(self, order, a, b):
        self.assertLess(order[a], order[b])

    def assert_comes_immediately_after(self, order, a, b):
        self.assertEqual(order[b], order[a] + 1)


class PostorderDfsTest(unittest.TestCase):
    def test_start_node_must_exist_in_graph(self):
        graph = [[], [], []]
        with self.assertRaises(AssertionError):
            list(postorder_depth_first_search(graph, 3))

    def test_trivial_graph(self):
        trivial_graph = [[]]

        result = postorder_depth_first_search(trivial_graph, 0)

        self.assertEqual(list(result), [0])

    def test_simple_path(self):
        path = [[1], [2], [3], [4], []]

        result = postorder_depth_first_search(path, 0)

        self.assertEqual(list(result), [4, 3, 2, 1, 0])

    def test_simple_cycle(self):
        cycle = [[1], [2], [3], [4], [0]]

        result = postorder_depth_first_search(cycle, 0)

        self.assertEqual(list(result), [4, 3, 2, 1, 0])

    def test_binary_tree(self):
        binary_tree = [[1, 5], [2, 3], [], [4], [], [6], []]

        result = postorder_depth_first_search(binary_tree, 0)

        dfs_order_index = [None] * len(binary_tree)
        for index, node in enumerate(result):
            dfs_order_index[node] = index

        self.assertEqual(dfs_order_index[0], len(binary_tree) - 1)  # root is last

        assert_comes_after = partial(self.assert_comes_after, dfs_order_index)
        assert_comes_immediately_after = partial(self.assert_comes_immediately_after, dfs_order_index)
        assert_comes_after(2, 1)
        assert_comes_after(3, 1)
        assert_comes_immediately_after(4, 3)
        assert_comes_immediately_after(6, 5)

    def assert_comes_after(self, order, a, b):
        self.assertLess(order[a], order[b], msg='{} comes after {}'.format(a, b))

    def assert_comes_immediately_after(self, order, a, b):
        self.assertEqual(order[b], order[a] + 1)