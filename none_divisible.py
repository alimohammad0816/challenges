from itertools import chain, combinations


def subset_creator(array):
    subsets = []
    for i in range(len(array)+1):
        subsets.append(list(combinations(array, i)))
    subsets = list(chain.from_iterable(subsets))
    return subsets


def non_devisible(array, k):
    none_divisible_list = []
    division = 0
    subset = subset_creator(array)
    for i in range(len(subset)):
        if len(subset[i]) > 1:
            x = subset[i]
            for l in range(1, len(x)):
                plus = x[l-1] + x[l]
                if plus % k == 0:
                    division = 1
                    continue
            if division != 0:
                division = 0
                continue
            else:
                none_divisible_list.append(x)

    print(none_divisible_list)
    return none_divisible_list


non_devisible([1, 2, 7, 4], 3)
