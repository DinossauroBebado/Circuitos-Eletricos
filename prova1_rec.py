import cmath
import math
from fasores import *

show_n(polar_rect(12, -70))


show_n(polar_rect(10, 10))

show_n(polar_rect(5, 45))

Z = [[complex(17.5, 5), complex(-8, -5)],
     [0, complex(7, 0)]]

S = [polar_rect(-12, -70), polar_rect(-10, 10) - polar_rect(-5, 45)]

show_n(-solve_sistem(Z, S)[1]*(5j)*5)
