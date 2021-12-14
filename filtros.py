import cmath
import math


def passa_baixa_C(w, R, C):
    print("Passa Baixa :capacitor na saída")
    H = 1/complex(1, R*w*C)
    wc = 1/R*C
    print(f"H{H} wc :{wc}")
    return H


def passa_baixa_L(w, R, L):
    print("Passa Baixa :capacitor na saída")
    H = 1/complex(1, (w*L)/R)
    wc = R/L
    print(f"H{H} wc :{wc}")
    return H


def passa_alta_C(w, R, C):
    print("Passa Alta :resistor na saída")
    H = complex(0, R*w*C)/complex(1, R*w*C)
    wc = 1/R*C
    print(f"H{H} wc :{wc}")
    return H


def passa_alta_C(w, R, L):
    print("Passa Alta :resistor na saída")
    H = complex(0, R*w*L)/complex(1, R*w*L)
    wc = R/L
    print(f"H{H} wc :{wc}")
    return H


def passa_faixa(w, R, C, L):
    print("Passa Faixa :resistor na saída")
    H = R/complex(R, w*L - (1/(w*C)))
    wo = 1/(L*C)**(1/2)
    print(f"H{H} wzero :{wo}")
    return H


def rejeita_faixa(w, R, C, L):
    print("Rejeita Faixa :indutor na saída")
    H = complex(0, w*L - (1/(w*C)))/complex(R, w*L - (1/(w*C)))
    wo = 1/(L*C)**(1/2)
    print(f"H{H} wzero :{wo}")
    return H
