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
    print(f"Cos{abs(z):.2f}({w:.2f}t +{math.degrees(cmath.phase(z)):.2f})")
    print()
    print("-----------------------------------------------------------------------")


def paralelo(z, k):
    return (z*k)/(z+k)


def solve_det(Z: list) -> int:
    return np.linalg.det(np.array(Z))


def solve_sistem(Z: list, S: list) -> list:
    for i, result in enumerate(np.linalg.solve(np.array(Z), np.array(S))):
        print(f"Var{i} : ")
        show_n(result)
    return np.linalg.solve(np.array(Z), np.array(S))


def capacitor_complex(f, w):
    z = 1/(complex(0, w*f))
    show_n(z)
    return z


def indutor_complex(l, w):
    z = complex(0, w*l)
    show_n(z)
    return z


def potencia_media_resistor(I, R):
    pot = (1/2)*I**2*R
    show_n(pot)
    return abs(pot)


def potencia_media_resistor_rms(I, R):
    pot = I**2*R
    show_n(pot)
    return abs(pot)


def not_cientifica(number, base):
    notação = {'k': 1000, 'm': 1/1000, 'u': 1/1000000,
               "n": 1/1000000000, "p": 1/1000000000000}
    return number*notação[base]


def Irsm(I):
    return I/(2**(1/2))


def Vrsm(V):
    return V/(2**(1/2))
