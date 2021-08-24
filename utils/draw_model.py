import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
import camera
from vector_utils import *
from math import *
from transforms import *


blues = matplotlib.cm.get_cmap('Blues')


def normal(face):
    v1, v2, v3 = face
    return cross(subtract(v2, v1), subtract(v3, v1))


def get_normalized_vector_similarity(v1, v2):
    return dot(unit(v1), unit(v2))


def shade(face, color_map=blues, light=(1, 2, 3)):
    v1, v2 = normal(face), light
    return color_map(1 - get_normalized_vector_similarity(v1, v2))


