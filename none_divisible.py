from itertools import chain, combinations


def subset_creator(array):
    subsets = []
    for i in range(len(array)+1):
        subsets.append(list(combinations(array, i)))
    subsets = list(chain.from_iterable(subsets))
    return subsets


def non_devisible(array, k):
    none_divisible_list = []
    division = False
    subset = subset_creator(array)
    for i in range(len(subset)):
        if len(subset[i]) > 1:
            x = subset[i]
            x_subsets = list(combinations(x, 2))
            for l in x_subsets:
                if sum(l) % k == 0:
                    division = True

            if division:
                division = False
                continue
            else:
                none_divisible_list.append(x)

    print(none_divisible_list)
    return none_divisible_list


non_devisible([1, 2, 7, 4], 3)
