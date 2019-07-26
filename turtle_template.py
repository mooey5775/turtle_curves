from math import sin
import math
from math import sqrt
import turtle

pi_count = # ADD WOLFRAM ALPHA'S MAX PLOTTING PI COUNT
div_const = 4 # SCALE DOWN FACTOR
steps_per_pi = 50 # changes drawing resolution

turtle.speed(100000000)
turtle.shape("turtle")

def sgn(t):
    return t / abs(t) if 0.1 < t or -0.1 > t else 0

def step(t):
    return int(t >= 0)

def x(t):
    return # PLACE OUTPUT OF PARAMETRIC CONVERTER HERE

def y(t):
    return # PLACE OUTPUT OF PARAMETRIC CONVERTER HERE

def dist(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

limits = [0, int(pi_count * math.pi * steps_per_pi)]

turtle.penup()
turtle.setposition(x(0) / div_const, y(0) / div_const)
turtle.pendown()

last_pos = (x(0) / div_const, y(0) / div_const)

for i in range(*limits):
    i /= steps_per_pi
    print(i)
    try:
        if dist(last_pos, (x(i) / div_const, y(i) / div_const)) > 50:
            turtle.penup()
        turtle.setposition(x(i)/div_const, y(i)/div_const)
        if dist(last_pos, (x(i) / div_const, y(i) / div_const)) > 50:
            turtle.pendown()
        last_pos = (x(i) / div_const, y(i) / div_const)
    except:
        print("error")
        pass

turtle.exitonclick()
