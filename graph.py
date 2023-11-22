import pickle
from dataclasses import dataclass
from typing import TypeVar, Generic, Callable

from Set import MySet

T = TypeVar("T")


@dataclass
class Edge(Generic[T]):
    start_edge: T
    finish_edge: T
    weight: int = 0


@dataclass
class AdjacentEdge(Generic[T]):
    finish_edge: T
    weight: int = 0

    def __hash__(self) -> int:
        return hash((self.finish_edge, self.weight))


class Graph(Generic[T]):
    def __init__(self, is_directed: bool = False) -> None:
        self.vertexes: dict[T, MySet[AdjacentEdge[T]]] = {}
        self.is_not_directed: bool = not is_directed

    def add_vertex(self, vertex: T) -> None:
        if vertex not in self.vertexes:
            self.vertexes[vertex] = MySet[AdjacentEdge[T]]()

    def add_edge(self, vertex1: T, vertex2: T, weight: int) -> None:
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.vertexes[vertex1].add(AdjacentEdge[T](vertex2, weight))
        if self.is_not_directed:
            self.vertexes[vertex2].add(AdjacentEdge[T](vertex1, weight))

    def add_edge_without_weight(self, vertex1: T, vertex2: T) -> None:
        self.add_edge(vertex1, vertex2, 0)

    def for_each_vertex(self, func: Callable[[T], None]) -> None:
        for v, _ in self.vertexes.items():
            func(v)

    def for_each_edge(self, func: Callable[[Edge[T]], None]) -> None:
        for vertex1, edges in self.vertexes.items():
            def edge_creator(value: AdjacentEdge[T]) -> None:
                func(Edge[T](vertex1, value.finish_edge, value.weight))

            edges.for_each(edge_creator)

    def for_each_adjacent_edge(self, vertex: T, func: Callable[[AdjacentEdge[T]], None]):
        if vertex in self.vertexes:
            edges = self.vertexes[vertex]
            edges.for_each(lambda x: func(x))

    def print_all_edges(self) -> None:
        def print_edge(edge: Edge[T]) -> None:
            print(f"Edge(V1: {edge.start_edge}, V2: {edge.finish_edge}, Weight: {edge.weight})")

        self.for_each_edge(print_edge)

    def print_all_vertexes(self) -> None:
        def print_vertex(vertex: T) -> None:
            print(f"Vertex: {vertex}")

        self.for_each_vertex(print_vertex)


if __name__ == '__main__':
    G = Graph()
    G.add_edge('A', 'B', 10)
    G.add_edge("B", "C", 20)
    G.add_edge("C", "D", 30)

    with open("graph", "wb") as file:
        pickle.dump(G, file)

    with open("graph", "rb") as file:
        load_graph = pickle.load(file)
    load_graph.print_all_edges()