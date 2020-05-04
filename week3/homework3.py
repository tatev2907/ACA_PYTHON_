import numpy as np


def arr_replace(arr1):
    arr1[arr1 % 2 != 0] = 0
    return arr1


def arr_replace_wher(arr1):
    return np.where(arr1 % 2 == 0, 0, arr1)


def arr_repeat(arr1):
    return np.repeat(arr1, 3)


def arr_join(arr1):
    return np.concatenate((arr1, arr1, arr1))


def arr_intersect(arr1, arr2):
    return np.intersect1d(arr1, arr2)


def arr_random():
    return np.random.uniform(5, 10, (2, 2))
