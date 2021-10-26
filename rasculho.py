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

r = complex(0, 11)
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
