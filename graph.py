from typing import List


class Graph:
    def __init__(self, graph_ways: List[tuple]):
        self.graph_ways = graph_ways
        self.ways, self.weights = self._get_info()

    def find_way(self, x, y):
        if not self.ways.get(x):
            print("invalid startpoint")

        elif not self.ways.get(x):
            print("invalid endpoint")

        elif x == y:
            return "same start point"

        ways = self.weights.keys()
        if f"{x}-{y}" in ways:
            path = [x, y]

        else:
            path = self._find_way(x, y)

        weight = 0
        for i in range(1, len(path)-1):
            weight += self.weights[f"{path[i-1]}-{path[i]}"]

        return f'{" -> ".join(path)}, weight: {weight}'

    def _find_way(self, startpoint, endpoint):
        shortest_paths = {startpoint: (None, 0)}
        this_node = startpoint
        visited = []

        while this_node != endpoint:
            visited.append(this_node)
            destinations = self.ways[this_node]
            weight_to_this_node = shortest_paths[this_node][1]

            for next_node in destinations:
                weight = self.weights[f"{this_node}-{next_node}"] + weight_to_this_node

                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (this_node, weight)

                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (this_node, weight)
            
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}

            if not next_destinations:
                return "no connection"

            this_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        while this_node is not None:
            path.append(this_node)
            next_node = shortest_paths[this_node][0]
            this_node = next_node

        path.reverse()
        return path

    def _get_info(self):
        ways = {}
        weights = {}

        for way in self.graph_ways:
            n1, n2, w = way
            weights[f"{n1}-{n2}"] = w
            weights[f"{n2}-{n1}"] = w

            if ways.get(n1):
                if n2 not in ways[n1]:
                    ways[n1].append(n2)

            else:
                ways[n1] = [n2]

            if ways.get(n2):
                if n1 not in ways[n2]:
                    ways[n2].append(n1)

            else:
                ways[n2] = [n1]

        return ways, weights


a = Graph([
    ("a1", "b1", 4), ("a1", "b2", 7), ("b2", "c1", 8), ("b2", "c2", 4),
    ("c1", "d1", 1), ("c1", "d2", 5), ("a2", "b3", 9), ("a2", "b4", 1),
    ("b3", "c3", 7), ("b3", "c4", 2), ("b3", "c5", 10), ("b3", "c6", 3),
    ("c4", "d3", 5), ("c4", "d4", 6), ("a1", "a2", 8), ("b1", "c3", 9),
    ("b2", "b3", 3), ("c2", "c3", 1), ("d2", "d3", 4), ("c6", "c1", 2),
])


print(a.find_way("a1", "d4"))
