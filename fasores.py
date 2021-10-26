import numpy as np
import cmath
import math

# angulos sempre em radianos

"""
(40L50 + 20L-30)^1/2

complex(-1.0, 0.0)

"""


def polar_rect(r, i):
    return cmath.rect(r, math.radians(i))


def rect_polar(z):
    return cmath.polar(z)


def show_n(z):
    print("-----------------------------------------------------------------------")
    print()
    print(f"Resultado rect : {z}")
    print(f"Resultado polar(rad): {abs(z)} L {math.degrees(cmath.phase(z))}")
    print()
    print("-----------------------------------------------------------------------")


def dominio_tempo(z, w):
    print("-----------------------------------------------------------------------")
    print()
    print(f"Cos{abs(z):.2f}({w:.2f}t +{math.degrees(cmath.phase(z)):.2f}")
    print()
    print("-----------------------------------------------------------------------")


def paralelo(z, k):
    return (z*k)/(z+k)


def solve_det(Z: list) -> int:
    return np.linalg.det(np.array(Z))


def solve_sistem(Z: list, S: list) -> list:
    return np.linalg.solve(np.array(Z), np.array(S))
