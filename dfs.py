from typing import Callable

from Set import MySet
from graph import Graph, T, AdjacentEdge, Edge

__is_found: bool = False


def dfs(graph: Graph[T], start: T, walkfunc: Callable[[T], bool]) -> None:
    global __is_found
    visited = MySet[T]()
    __is_found = False
    __dfs(graph, start, visited, walkfunc)


def __dfs(graph: Graph[T], start: T, visited: MySet[T], walkfunc: Callable[[T], bool]) -> None:
    global __is_found
    visited.add(start)

    __is_found = walkfunc(start)
    if __is_found:
        return

    def __foreach(edge: AdjacentEdge[T]) -> None:
        if __is_found:
            return
        if not visited.contains(edge.finish_edge):
            __dfs(graph, edge.finish_edge, visited, walkfunc)

    graph.for_each_adjacent_edge(start, __foreach)


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

    def dfs_walk(vertex: str) -> bool:
        print(vertex + " ", end='')
        return vertex == "S"

    dfs(graph, "A", dfs_walk)
    path: list[str] = []

    def dfs_walk_with_path(vertex: str) -> bool:
        path.append(vertex)
        return vertex == "S"

    dfs(graph, "A", dfs_walk_with_path)
    print()

    path.reverse()
    min_path: list[str] = ["S"]
    find: str = "S"
    for vertex in path:
        if graph.vertexes[vertex].contains(AdjacentEdge[str](find)):
            min_path.append(vertex)
            find = vertex

    min_path.reverse()
    print(min_path)