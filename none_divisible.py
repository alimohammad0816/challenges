from itertools import chain, combinations


def subset_creator(array):
    subsets = []
    for i in range(len(array)+1):
        subsets.append(list(combinations(array, i)))
    subsets = list(chain.from_iterable(subsets))
    return subsets


def none_devisible_calculator(array, k):
    division = False
    subset = subset_creator(array)
    for i in range(len(subset)):
        if len(subset[i]) > 1:
            x = subset[i]
            x_subsets = list(combinations(x, 2))
            for l in x_subsets:
                if sum(l) % k == 0:
                    division = True
                    break
            if division:
                division = False
                continue
            else:
                yield x


def none_divisible(array, k):
    my_list = []
    for i in none_devisible_calculator(array, k):
        my_list.append(i)
    print(my_list)
    return my_list


none_divisible([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15)
