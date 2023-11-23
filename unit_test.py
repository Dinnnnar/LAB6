import unittest
from graph import Edge, Graph, AdjacentEdge
from bfs import bfs
from dfs import dfs


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph[int]()
        self.graph.add_edge("A", "B", 10)
        self.graph.add_edge("B", "C", 20)

    def test_print(self):
        self.assertEqual(f"{self.graph}", "Graph: Vertex: A Vertex: B Vertex: C ")

    def test_add_edge_and_vertex(self):
        self.graph.add_vertex("E")
        self.assertTrue("E" in self.graph.vertexes)
        self.graph.add_edge("A", "D", 15)

        edges_vertex_1 = list(self.graph.vertexes.keys())
        edges_vertex_4 = list(self.graph.vertexes.keys())

        self.assertTrue(any(edge == "D" for edge in edges_vertex_1))
        self.assertTrue(any(edge == "A" for edge in edges_vertex_4))

    def test_for_each_vertex(self):
        result = []

        def app_vertex(vertex):
            result.append(vertex)

        self.graph.for_each_vertex(app_vertex)
        self.assertEqual(result, ["A","B","C"])

    def test_for_each_edge(self):
        result = []

        def add_edge(edge):
            result.append(edge)

        self.graph.for_each_edge(add_edge)
        expected_edges = [Edge(start_edge='A', finish_edge='B', weight=10),
                            Edge(start_edge='B', finish_edge='A', weight=10),
                            Edge(start_edge='B', finish_edge='C', weight=20),
                            Edge(start_edge='C', finish_edge='B', weight=20)]
        self.assertEqual(result, expected_edges)

    def test_for_each_adjacent_edge(self):
        result = []

        def adjacent_edges(adj_edge):
            result.append(adj_edge)

        self.graph.for_each_adjacent_edge("A", adjacent_edges)
        self.assertEqual(result, [AdjacentEdge(finish_edge='B', weight=10)])

    def test_amount_edges(self):
        self.assertEqual(self.graph.amount_edges(), 2)

    def test_amount_vertexes(self):
        self.assertEqual(self.graph.amount_vertexes(), 3)

    def test_bfs_path(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B"), Edge("A", "C"), Edge("C", "F"),
            Edge("C", "G"), Edge("G", "M"), Edge("G", "N"),
            Edge("B", "D"), Edge("B", "E"), Edge("D", "H"),
            Edge("D", "I"),  Edge("D", "J"),  Edge("E", "K"),
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
        self.assertEqual(min_path, ['A', 'B', 'E', 'K'])

    def test_dfs_path(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B"), Edge("A", "C"), Edge("C", "F"),
            Edge("C", "G"), Edge("G", "M"), Edge("G", "N"),
            Edge("B", "D"), Edge("B", "E"), Edge("D", "H"),
            Edge("D", "I"), Edge("D", "J"), Edge("E", "K"),
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
        self.assertEqual(min_path, ['A', 'B', 'E', 'K'])


if __name__ == '__main__':
    unittest.main()