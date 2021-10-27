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

print(capacitor_complex((330/1000), 10))

Z = [[complex(2, 10), complex(0, -10)], [complex(5, -10), complex(0, 9.7)]]

S = [polar_rect(2.5, 9), 0]

solve_sistem(Z, S)
