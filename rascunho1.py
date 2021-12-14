import cmath
import math

from numpy import ComplexWarning
from fasores import *

"""q = 4/complex(0, 2)
show_n(q)

Z = [[complex(2, -2), complex(1, 1), complex(-1, -2)],
     [1, -1, 0],
     [complex(0.8, -2), complex(1, 0), complex(-1, 2)]]
S = [0, 12, 0]

print(show_n(solve_sistem(Z, S)[0]))

show_n(complex(12, 0))"""

"""show_n(polar_rect(40, 30)/complex(0, -2))

show_n(-1/complex(0, -2) - 1/3 + 1/complex(8, 6))

show_n(1/complex(8, 6))

show_n(-1/complex(8, 6)+1/10)

Z = [[complex(0.25, 0.56), complex(0.08, -0.06)],
     [complex(0.08, -0.06), complex(-0.02, -0.06)]]

S = [complex(-9.9, 17.32), 5]

show_n(solve_sistem(Z, S)[0])
"""

"""show_n(polar_rect(50, 0))

Z = [[complex(0, -10), complex(0, 20)], [complex(0, 20), complex(40, -20)]]

S = [polar_rect(40, 30), -50]

solve_sistem(Z, S)
"""

"""print(capacitor_complex((330/1000), 10))

Z = [[complex(2, 10), complex(0, -10)], [complex(5, -10), complex(0, 9.7)]]

S = [polar_rect(2.5, 9), 0]

solve_sistem(Z, S)
"""
"""i_tree = [complex(0, -4), -5, complex(15, -4)]
i_sm = [complex(0, 4), complex(-5, 6), complex(5, -4)]
i_ger = [1, 1, 0]

S = [50, 0, 2.4]

solve_sistem([i_tree, i_sm, i_ger], S)"""

"""res = 2*(complex(0, -3)/complex(5, -3))
show_n(res)

show_n(((1/2)*res**2)*5)

v_zero = 5*res

show_n(v_zero)

p_source = (v_zero.real*2)/2

show_n(p_source)"""

"""carga = paralelo(complex(0, 0.00009), complex(60, 0))

v = complex(160, 0)

i = v/carga

show_n(carga)

show_n(i)

show_n(i.real*v)
"""
capacitor_complex(0.25, 2)
indutor_complex(3, 2)

print(paralelo(complex(2, -2), complex(0, 6)))

show_n(polar_rect(8, -40)/complex(4.6, -1.2))

i = polar_rect(8, -40)/complex(4.6, -1.2)

show_n((1/2)*i**2*1)

i_tw = (6j/(2+4j))*i

show_n(i_tw)


p = potencia_resistor(i_tw, 2)
