from random import randint as rnd
from math import pi, e

for i in range(7):
    lanzamiento = rnd(1, 6)
    if lanzamiento < 4:
        print(pi * lanzamiento)
    else:
        print(e * lanzamiento)