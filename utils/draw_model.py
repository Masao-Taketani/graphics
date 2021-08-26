import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from utils import camera
from utils.vector_utils import *
from math import *
from utils.transforms import *


blues = matplotlib.cm.get_cmap('Blues')


def normal(face):
    v1, v2, v3 = face
    return cross(subtract(v2, v1), subtract(v3, v1))


def get_normalized_vector_similarity(v1, v2):
    return dot(unit(v1), unit(v2))


def shade(face, color_map=blues, light=(1, 2, 3)):
    v1, v2 = normal(face), light
    return color_map(1 - get_normalized_vector_similarity(v1, v2))


def Axes():
    axes =  [
        [(-1000,0,0),(1000,0,0)],
        [(0,-1000,0),(0,1000,0)],
        [(0,0,-1000),(0,0,1000)]
    ]
    glBegin(GL_LINES)
    for axis in axes:
        for vertex in axis:
            glColor3fv((1,1,1))
            glVertex3fv(vertex)
    glEnd()


def draw_model(faces, color_map=blues, light=(1,2,3),
                glRotatefArgs=None,
                get_matrix=None):
    pygame.init()
    display = (400,400)
    window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    cam = camera.default_camera
    cam.set_window(window)
    gluPerspective(45, 1, 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    if glRotatefArgs:
        glRotatef(*glRotatefArgs)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glCullFace(GL_BACK)

    while cam.is_shooting():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Axes()
        glBegin(GL_TRIANGLES)
        
        def do_matrix_transform(v):
            if get_matrix:
                m = get_matrix(pygame.time.get_ticks())
                return multiply_matrix_vector(m, v)
            else:
                return v
        transformed_faces = polygon_map(do_matrix_transform, faces)
        for face in transformed_faces:
            color = shade(face,color_map,light)
            for vertex in face:
                glColor3fv((color[0], color[1], color[2]))
                glVertex3fv(vertex)
        glEnd()
        cam.tick()
        pygame.display.flip()