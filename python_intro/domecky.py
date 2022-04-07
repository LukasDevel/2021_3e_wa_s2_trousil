import math
from turtle import *

pensizes = [3,5,8]

def domecek(par, size):
    pen(pensize=pensizes[size])
    x = math.sqrt(2)
    forward(par)
    left(90)
    forward(par)
    left(45)
    forward((par/2)*x)
    left(90)
    forward((par/2)*x)
    left(135)
    forward(par)
    right(135)
    forward(par*x)
    right(135)
    forward(par)
    right(135)
    forward(par*x)
    left(45)
    

domecek(100,1)
domecek(75,2)
domecek(120,0)


exitonclick()