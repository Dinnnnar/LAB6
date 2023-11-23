from typing import Callable

from Set import MySet
from Queue import MyQueue
from graph import Graph, T, AdjacentEdge, Edge


def bfs(graph: Graph[T], start: T, walkfunc: Callable[[T], bool]) -> None:
    queue = MyQueue[T]()
    visited = MySet[T]()
    queue.enqueue(start)

    def __foreach(edge: AdjacentEdge[T]) -> None:
        if not visited.contains(edge.finish_edge):
            queue.enqueue(edge.finish_edge)

    while not queue.is_empty():
        vertex = queue.dequeue()

        if walkfunc(vertex):
            return

        visited.add(vertex)

        graph.for_each_adjacent_edge(vertex, __foreach)


if __name__ == '__main__':
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
        Edge("K", "I"),
        Edge("I", "S"),
    ]

    graph: Graph[str] = Graph[str]()

    for it in vertexes:
        graph.add_edge_without_weight(it.start_edge, it.finish_edge)

    def bfs_walk(vertex: str) -> bool:
        print(vertex + " ", end='')
        return vertex == "S"

    bfs(graph, "A", bfs_walk)
    print()
    path: list[str] = []

    def bfs_walk_with_path(vertex: str) -> bool:
        path.append(vertex)
        return vertex == "S"

    bfs(graph, "A", bfs_walk_with_path)

    path.reverse()
    min_path: list[str] = ["S"]
    find: str = "S"
    for vertex in path:
        if graph.vertexes[vertex].contains(AdjacentEdge[str](find)):
            min_path.append(vertex)
            find = vertex

    min_path.reverse()
    print(min_path)