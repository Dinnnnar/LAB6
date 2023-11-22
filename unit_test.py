import unittest
from graph import Edge, Graph, AdjacentEdge
from bfs import bfs
from dfs import dfs

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph[int]()
        self.graph.add_edge(1, 2, 10)
        self.graph.add_edge(2, 3, 20)
        self.graph.add_edge(3, 1, 30)

    def test_add_vertex(self):
        self.graph.add_vertex(4)
        self.assertTrue(4 in self.graph.vertexes)

    def test_add_edge(self):
        self.graph.add_edge(1, 4, 15)

        edges_vertex_1 = list(self.graph.vertexes.keys())
        edges_vertex_4 = list(self.graph.vertexes.keys())

        self.assertTrue(any(edge == 4 for edge in edges_vertex_1))
        self.assertTrue(any(edge == 1 for edge in edges_vertex_4))

    def test_for_each_vertex(self):
        result = []

        def collect_vertices(vertex):
            result.append(vertex)

        self.graph.for_each_vertex(collect_vertices)
        self.assertEqual(result, [1, 2, 3])

    def test_for_each_edge(self):
        result = []

        def collect_edges(edge):
            result.append(edge)

        self.graph.for_each_edge(collect_edges)
        expected_edges = [Edge(start_edge=1, finish_edge=2, weight=10), Edge(start_edge=1, finish_edge=3, weight=30),
                          Edge(start_edge=2, finish_edge=1, weight=10), Edge(start_edge=2, finish_edge=3, weight=20),
                          Edge(start_edge=3, finish_edge=2, weight=20), Edge(start_edge=3, finish_edge=1, weight=30)]
        self.assertEqual(result, expected_edges)

    def test_for_each_adjacent_edge(self):
        result = []

        def collect_adjacent_edges(adj_edge):
            result.append(adj_edge)

        self.graph.for_each_adjacent_edge(1, collect_adjacent_edges)
        self.assertEqual(result, [AdjacentEdge(finish_edge=2, weight=10), AdjacentEdge(finish_edge=3, weight=30)])

    def test_amount_edges(self):
        self.assertEqual(self.graph.amount_edges(), 3)

    def test_amount_vertexes(self):
        self.assertEqual(self.graph.amount_vertexes(), 3)

'''    def test_print_all_edges(self):

    def test_print_all_vertexes(self):'''


class Testbfs(unittest.TestCase):
    def printgraph(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B"),
            Edge("A", "C"),
            Edge("C", "F"),
            Edge("C", "G"),
            Edge("G", "M"),
            Edge("G", "N"),
            Edge("B", "D"),
            Edge("B", "E"),
            Edge("D", "H"),
            Edge("D", "I"),
            Edge("D", "J"),
            Edge("E", "K"),
            Edge("E", "L"),
        ]

        graph: Graph[str] = Graph[str]()

        for it in vertexes:
            graph.add_edge_without_weight(it.start_edge, it.finish_edge)

        def bsf_walk(vertex: str) -> bool:
            print(vertex + " ", end='')
            return vertex == "K"

        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        bfs(graph, "A", bsf_walk)
        printed_output = sys.stdout.getvalue()

        sys.stdout = saved_stdout
        self.assertEqual(printed_output, "A B C D E F G H I J K ")

    def path(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B"),
            Edge("A", "C"),
            Edge("C", "F"),
            Edge("C", "G"),
            Edge("G", "M"),
            Edge("G", "N"),
            Edge("B", "D"),
            Edge("B", "E"),
            Edge("D", "H"),
            Edge("D", "I"),
            Edge("D", "J"),
            Edge("E", "K"),
            Edge("E", "L"),
        ]

        graph: Graph[str] = Graph[str]()

        for it in vertexes:
            graph.add_edge_without_weight(it.start_edge, it.finish_edge)
        path: list[str] = []

        def bfs_walk_with_path(vertex: str) -> bool:
            path.append(vertex)
            return vertex == "K"

        bfs(graph, "A", bfs_walk_with_path)

        path.reverse()
        min_path: list[str] = ["K"]
        find: str = "K"
        for vertex in path:
            if graph.vertexes[vertex].contains(AdjacentEdge[str](find)):
                min_path.append(vertex)
                find = vertex

        min_path.reverse()
        self.assertEqual(min_path, "['A', 'B', 'E', 'K']")


class Testdfs(unittest.TestCase):
    def printgraph(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B"),
            Edge("A", "C"),
            Edge("C", "F"),
            Edge("C", "G"),
            Edge("G", "M"),
            Edge("G", "N"),
            Edge("B", "D"),
            Edge("B", "E"),
            Edge("D", "H"),
            Edge("D", "I"),
            Edge("D", "J"),
            Edge("E", "K"),
            Edge("E", "L"),
        ]

        graph: Graph[str] = Graph[str]()

        for it in vertexes:
            graph.add_edge_without_weight(it.start_edge, it.finish_edge)

        def dfs_walk(vertex: str) -> bool:
            print(vertex + " ", end='')
            return vertex == "K"

        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        dfs(graph, "A", dfs_walk)
        printed_output = sys.stdout.getvalue()

        sys.stdout = saved_stdout
        self.assertEqual(printed_output, "A B C D E F G H I J K ")

    def dfs_path(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B"),
            Edge("A", "C"),
            Edge("C", "F"),
            Edge("C", "G"),
            Edge("G", "M"),
            Edge("G", "N"),
            Edge("B", "D"),
            Edge("B", "E"),
            Edge("D", "H"),
            Edge("D", "I"),
            Edge("D", "J"),
            Edge("E", "K"),
            Edge("E", "L"),
        ]

        graph: Graph[str] = Graph[str]()

        for it in vertexes:
            graph.add_edge_without_weight(it.start_edge, it.finish_edge)
        path: list[str] = []

        def dfs_walk_with_path(vertex: str) -> bool:
            path.append(vertex)
            return vertex == "K"

        dfs(graph, "A", dfs_walk_with_path)

        path.reverse()
        min_path: list[str] = ["K"]
        find: str = "K"
        for vertex in path:
            if graph.vertexes[vertex].contains(AdjacentEdge[str](find)):
                min_path.append(vertex)
                find = vertex

        min_path.reverse()
        self.assertEqual(min_path, "['A', 'B', 'E', 'K']")


if __name__ == '__main__':
    unittest.main()