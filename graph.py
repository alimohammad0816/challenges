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
            correct_paths = self._find_way(x, y, x, [])
            correct_paths_dict = {}

            for path in correct_paths:
                weight = 0
                for i in range(1, len(path)-1):
                    weight += self.weights[f"{path[i-1]}-{path[i]}"]

                correct_paths_dict[f'{",".join(path)}'] = weight
            
            way = list(correct_paths_dict.keys())[0].split(",")
            weight = list(correct_paths_dict.values())[0]

            for key, value in correct_paths_dict.items():
                if value < weight:
                    weight = value
                    way = key.split(",")

                elif value == weight:
                    if len(key.split(",")) < len(way):
                        way = key.split(",")

            return f'Best Way: {" -> ".join(way)}, weight: {weight}'

    def _find_way(self, startpoint, endpoint, current_path, correct_paths):
        for i in self.ways[startpoint]:
            if i == endpoint:
                c = current_path+","+i
                correct_paths.append(c.split(","))

            elif i != startpoint:
                if i not in current_path:
                    self._find_way(i, endpoint, current_path+","+i, correct_paths)
        
        return correct_paths

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
    ("a", "b", 2), ("a", "c", 4),
    ("b", "d", 5), ("c", "d", 1),
    ("d", "e", 3),
])

print(a.find_way("a", "e"))

b = Graph([
    ("a1", "b1", 4), ("a1", "b2", 7), ("b2", "c1", 8), ("b2", "c2", 4),
    ("c1", "d1", 1), ("c1", "d2", 5), ("a2", "b3", 9), ("a2", "b4", 1),
    ("b3", "c3", 7), ("b3", "c4", 2), ("b3", "c5", 10), ("b3", "c6", 3),
    ("c4", "d3", 5), ("c4", "d4", 6), ("a1", "a2", 8), ("b1", "c3", 9),
    ("b2", "b3", 3), ("c2", "c3", 1), ("d2", "d3", 4), ("c6", "c1", 2),
])


print(b.find_way("a1", "d4"))
