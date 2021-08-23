from math import sqrt, sin, cos, acos, atan2


#def add(*vectors):
#    by_coordinate = zip(vectors)
#    added_vec_list = [sum(coord) for coord in by_coordinate]
#    return tuple(added_vec_list)


def add(*vectors):
    """zip(v1, v2, ..., vn) -> (v11, v21, ..., vn1), (v12, v22, ..., vn2), ..."""
    #return tuple([sum(same_elems) for same_elems in zip(*vectors)])
    return tuple(map(sum, zip(*vectors)))


def subtract(v1, v2):
    # loop for each coordinate (e.g. if v has (x, y, z) coords, it loops 3 times)
    return tuple(v1_elem - v2_elem for v1_elem, v2_elem in zip(v1, v2))


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])


def distance(v1, v2):
    return length(subtract(v1, v2))


def perimeter(vectors):
    """
    It takes a list of vectors that are aligned together to make outline
    of some shape.
    It returns the perimeter length by suming the length of vectors that
    are supposed to be sequentially connected each other including the 
    distance from the last vector to the first to make the outline of 
    the shape.
    """
    return sum([distance(vectors[i], vectors[(i + 1) % len(vectors)])
                for i in range(0, len(vectors))])


def scale(scalar, v):
    return tuple([scalar * coord for coord in v])


def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length * cos(angle), length * sin(angle))


def to_polar(cartesian_vector):
    len = length(cartesian_vector)
    x, y = cartesian_vector
    ang = atan2(y, x)
    return (len, ang)


def rotate2d(rotate_angle, vector):
    length, angle = to_polar(vector)
    return to_cartesian((length, angle + rotate_angle))


def translate(translation, vectors):
    """Apply trainslations to list of vectors"""
    return [add(vec, translation) for vec in vectors]


def angle_between(v1, v2):
    return acos(dot(v1, v2) / (length(v1) * length(v2)))


def cross(u, v):
    assert len(u) == 3 and len(v) == 3, "length of u and v has to be 3." \
                                        f"len of u is {len(u)} and len of v is {len(v)}"
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)


def component(v, direction):
    """To project v to the specified direction and it returns a scalar,
    indicating how long v extends to the direction."""
    return dot(v, direction) / length(direction)


def unit(v):
    return scale(1. / length(v), v)


def linear_combination(scalars, *vectors):
    return add(*[scale(scal, vec) for scal, vec in zip(scalars, vectors)])