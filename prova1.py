import cmath
import math
from fasores import *

'''show_n(polar_rect(10, 30) - 5)

Z = [[complex(13, -5), complex(10, -95)], [complex(27, 8), complex(200, 95)]]

S = [polar_rect(-8, -40), polar_rect(6.19, 53.79)]

solve_sistem(Z, S)

s = 0.03914899354583767-0.07318158702904162j
d = -0.2182736440085194+0.6539925318919009j
show_n(10*s)
show_n(10*d)

show_n(polar_rect(8, 10)/10)'''

z = polar_rect(10, 60)/polar_rect(2.55, 251.32)

show_n(paralelo(z.real, 19))
