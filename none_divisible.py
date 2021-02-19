from itertools import chain, combinations
from time import perf_counter


def subset_creator(array):
    subsets = []
    for i in range(1, len(array)+1):
        subsets.append(list(combinations(array, i)))
    subsets = list(chain.from_iterable(subsets))
    return subsets


def none_devisible_calculator(array, k):
    subset = subset_creator(array)
    for i in range(len(subset)-1, 1, -1):
        if len(subset[i]) > 1:
            x = subset[i]
            x_subsets = list(combinations(x, 2))
            for l in x_subsets:
                if sum(l) % k == 0:
                    break
                else:
                    print(subset[i])
                    return subset[i]


x = perf_counter()
none_devisible_calculator(list(range(1, 12)), 3)
