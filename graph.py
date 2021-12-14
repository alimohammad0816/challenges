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
            return f'from "{x}" go to "{y}", cost: {self.weights[f"{x}-{y}"]}'

        else:
            return self._find_way(x, y)

    def _find_way(self, startpoint, endpoint):
        visited = []
        ways = [[startpoint]]

        while ways:
            path = ways.pop(0)
            node = path[-1]

            if node not in visited:
                for c in self.ways[node]:
                    new_path = list(path)
                    new_path.append(c)
                    ways.append(new_path)

                    if c == endpoint:
                        weight = 0
                        for i in range(1, len(new_path)-1):
                            weight += self.weights[f"{new_path[i-1]}-{new_path[i]}"]
                        return f'{" -> ".join(new_path)} weight: {weight}'

                visited.append(node)

    def _has_connection(self, way):
        if self.ways.get(way):
            return True

        else:
            return False

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
