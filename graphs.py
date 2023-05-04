from typing import Any


# TODO: unit tests
class Graph:
    """An adjacency list implementation of an unweighted, undirected graph."""

    def __init__(self):
        self.adjacency_list: dict[Any, list] = {}

    def __str__(self):
        # TODO
        return str(self.adjacency_list)

    def __repr__(self):
        # TODO
        return str(self.adjacency_list)

    def __eq__(self, other):
        # TODO
        return False

    def adjacent_nodes(self, vertex) -> list:
        """:return: a list of the vertices adjacent to vertex.
        :raise: a ValueError if :param: vertex is not a valid node.
        """

        if vertex not in self.adjacency_list:
            raise ValueError()

        return list(self.adjacency_list[vertex])

    def degree(self, vertex) -> int:
        """:return: the degree of :param: vertex.
        :raise: a ValueError if :param: vertex is not a valid node.
        """

        if vertex not in self.adjacency_list:
            raise ValueError()

        return len(self.adjacency_list[vertex])

    @property
    def num_vertices(self) -> int:
        """:return: the number of vertices in the graph."""

        return len(self.adjacency_list)

    @property
    def num_edges(self) -> int:
        """:return: the number of edges in the graph."""

        acc_size = 0
        for node in self.adjacency_list:
            acc_size += self.degree(node)
        assert acc_size % 2 == 0
        return int(acc_size / 2)

    def add_node(self, vertex):
        """:raise: a ValueError if :param: vertex is not a valid node.
        :param: vertex:
        :return:
        """
        if vertex not in self.adjacency_list:
            raise ValueError()

        self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Adds an edge between vertex1 and vertex2.
        :raise: a ValueError if neither vertex2 nor vertex2 are valid nodes.
        """
        if vertex1 not in self.adjacency_list:
            raise ValueError()
        if vertex2 not in self.adjacency_list:
            raise ValueError()

        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)


class DirGraph:
    pass


class WeightedGraph:
    pass


class WeightedDirGraph:
    pass
