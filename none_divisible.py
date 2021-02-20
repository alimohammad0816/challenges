from itertools import chain, combinations


def subset_creator(array):
    subsets = []
    for i in range(1, len(array)+1):
        subsets.append(list(combinations(array, i)))
    subsets = list(chain.from_iterable(subsets))
    return subsets


def none_devisible_calculator(array, k):
    is_div = False
    subset = subset_creator(array)
    for i in range(len(subset)-1, 1, -1):
        if len(subset[i]) > 1:
            x = subset[i]
            x_subsets = list(combinations(x, 2))
            for l in x_subsets:
                if sum(l) % k == 0:
                    is_div = True

            if not is_div:
                print(list(subset[i]))
                return list(subset[i])

            elif is_div:
                is_div = False


my_list = [4, 3, 2, 1]
none_devisible_calculator(my_list, 3)
