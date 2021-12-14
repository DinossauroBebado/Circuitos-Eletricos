import cmath
import math
from fasores import *

"""
Example:

x = polar_rect(40, 50)
show_n(x)
y = polar_rect(20, -30)
show_n(y)

show_n(x+y)"""

'''r = complex(0, 11)
j = complex(16, 0)

k = complex(4, 20) + paralelo(r, j)

v = complex(12, 0)

show_n(v/k)

dominio_tempo(v/k, 10)

Z = [[complex(8, -2), complex(0, 2), complex(-8, 0), complex(0, 0)],
     [complex(0, 0), complex(1, 0), complex(0, 0), complex(0, 0)],
     [complex(-8, 0), complex(0, -5), complex(8, -4), complex(6, 5)],
     [complex(0, 0), complex(0, 0), complex(-1, 0), complex(1, 0)]]

S = [10, -3, 0, 4]

show_n(solve_sistem(Z, S)[0])


show_n(polar_rect(2, 0))

show_n(complex(0, 16)/complex(4, 3))

show_n(complex(6, 8)*complex(4, 3))
res = (complex(-2.92, -2.56)*complex(0, 50))/complex(10, 61)
show_n(res)
dominio_tempo(res, 4)

show_n(complex(20, 0)/complex(30, 10))

Z = [[complex(2, 1), complex(0, -1)],
     [complex(-4, 1), complex(-0.6, -0.8)]]

S = [10, 0]

r = solve_sistem(Z, S)[1]*(3/complex(3, 1))

show_n(r)

dominio_tempo(r, 1000)

g = 1/complex(0, -4) + 6/10

c = 4.8/g

a = 12

show_n((a - c)/2)
'''
capacitor_complex(not_cientifica(40, 'u'), 1000)

i_tw = (-180+150j)/(40-5j)

ix = 6 + i_tw

show_n(Irsm(ix))

potencia_media_resistor_rms(abs(Irsm(ix)), 50)
