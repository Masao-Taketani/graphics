from math import sqrt, sin, cos, acos, atan2


def add(*vectors):
    by_coordinate = zip(vectors)
    added_vec_list = [sum(coord) for coord in by_coordinate]
    return tuple(added_vec_list)


def subtract(v1, v2):
    # loop for each coordinate (e.g. if v has (x, y, z) coords, it loops 3 times)
    return tuple(v1_elem - v2_elem for v1_elem, v2_elem in zip(v1, v2))