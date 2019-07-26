from math import sin
import math
from math import sqrt
import turtle

turtle.speed(100000000)
turtle.shape("turtle")

def sgn(t):
    return t / abs(t) if 0.1 < t or -0.1 > t else 0

def step(t):
    return int(t >= 0)

def x(t):
    return ((-3/10*sin(19/13 - 7*t) - 31/4*sin(14/9 - 6*t) - 15/8*sin(14/9 - 5*t) - 49/11*sin(11/7 - 4*t) - 61/4*sin(11/7 - 3*t) - 415/18*sin(11/7 - 2*t) + 178/9*sin(t + 11/7) + 538/11)*step(75*math.pi - t)*step(t - 71*math.pi) + (466/9*sin(t + 11/7) + 95/9*sin(2*t + 11/7) + 47/6*sin(3*t + 11/7) + 37/11*sin(4*t + 11/7) - 4157/11)*step(71*math.pi - t)*step(t - 67*math.pi) + (-13/25*sin(14/9 - 15*t) - 2*sin(14/9 - 10*t) - 66/7*sin(11/7 - 9*t) - 257/11*sin(11/7 - 7*t) - 29/3*sin(11/7 - 5*t) + 995/8*sin(t + 11/7) + 458/5*sin(2*t + 11/7) + 96/7*sin(3*t + 19/12) + 1024/33*sin(4*t + 11/7) + 59/9*sin(6*t + 14/9) + 147/11*sin(8*t + 11/7) + 20/7*sin(11*t + 11/7) + 17/11*sin(12*t + 14/3) + 11/5*sin(13*t + 8/5) + 1/5*sin(14*t + 5/3) + 1981/11)*step(67*math.pi - t)*step(t - 63*math.pi) + (-27/14*sin(11/7 - 6*t) - 19/10*sin(11/7 - 4*t) + 535/6*sin(t + 11/7) + 308/15*sin(2*t + 33/7) + 37/9*sin(3*t + 11/7) + 39/8*sin(5*t + 11/7) - 3134/13)*step(63*math.pi - t)*step(t - 59*math.pi) + (-8/15*sin(14/9 - 11*t) - 5/6*sin(11/7 - 9*t) - 11/21*sin(14/9 - 7*t) + 602/5*sin(t + 33/7) + 61/11*sin(2*t + 11/7) + 124/13*sin(3*t + 33/7) + 10/7*sin(4*t + 14/3) + 67/17*sin(5*t + 33/7) + 11/7*sin(6*t + 11/7) + 13/9*sin(8*t + 11/7) + 4/13*sin(10*t + 8/5) + 1/6*sin(12*t + 23/15) - 5491/11)*step(59*math.pi - t)*step(t - 55*math.pi) + (-29/7*sin(14/9 - 9*t) - 5/6*sin(28/19 - 6*t) - 91/9*sin(11/7 - 3*t) + 172/3*sin(t + 11/7) + 286/9*sin(2*t + 11/7) + 107/4*sin(4*t + 11/7) + 23/15*sin(5*t + 17/11) + 56/13*sin(7*t + 11/7) + 39/19*sin(8*t + 11/7) + 13/4*sin(10*t + 11/7) + 16/5*sin(11*t + 11/7) + 5/7*sin(12*t + 11/7) - 1345/6)*step(55*math.pi - t)*step(t - 51*math.pi) + (-75/7*sin(11/7 - 17*t) - 127/14*sin(20/13 - 14*t) - 58/7*sin(3/2 - 13*t) - 25/6*sin(16/11 - 4*t) - 227/9*sin(17/11 - 3*t) - 1601/16*sin(11/7 - 2*t) + 259/11*sin(t + 14/9) + 16/5*sin(5*t + 5/3) + 272/9*sin(6*t + 11/7) + 7/12*sin(7*t + 26/9) + 28/27*sin(8*t + 29/8) + 29/8*sin(9*t + 12/7) + 419/35*sin(10*t + 8/5) + 11/12*sin(11*t + 48/11) + 112/37*sin(12*t + 3/2) + 27/4*sin(15*t + 14/9) + 103/11*sin(16*t + 14/9) + 55/7*sin(18*t + 61/13) + 85/9*sin(19*t + 8/5) + 19/2*sin(20*t + 8/5) + 63/8*sin(21*t + 61/13) + 655/12)*step(51*math.pi - t)*step(t - 47*math.pi) + (-7/4*sin(11/7 - 20*t) - 11/12*sin(3/2 - 17*t) - 23/5*sin(14/9 - 15*t) - 230/11*sin(11/7 - 8*t) - 288/5*sin(11/7 - 7*t) - 401/16*sin(11/7 - 5*t) - 33/7*sin(11/7 - 3*t) - 493/5*sin(11/7 - t) + 53/4*sin(2*t + 11/7) + 117/14*sin(4*t + 11/7) + 69/5*sin(6*t + 11/7) + 226/25*sin(9*t + 11/7) + 42/17*sin(10*t + 11/7) + 13/12*sin(11*t + 8/5) + 1/10*sin(12*t + 37/10) + 16/15*sin(13*t + 14/3) + 52/9*sin(14*t + 8/5) + 5/2*sin(16*t + 33/7) + 13/5*sin(18*t + 11/7) + 23/10*sin(19*t + 33/7) + 3253/8)*step(47*math.pi - t)*step(t - 43*math.pi) + (-467/7*sin(4/3 - 3*t) + 1205/3*sin(t + 11/7) + 3267/13*sin(2*t + 5/3) + 1339/20*sin(4*t + 16/9) + 17/2*sin(5*t + 8/7) + 83/11*sin(6*t + 2) + 61/8*sin(7*t + 18/11) + 94/11*sin(8*t + 11/6) + 36/35*sin(9*t + 3/5) + 47/7*sin(10*t + 19/9) + 38/15*sin(11*t + 5/6) + 22/7*sin(12*t + 7/3) - 23693/33)*step(43*math.pi - t)*step(t - 39*math.pi) + (-2/7*sin(3/4 - 8*t) - 9/10*sin(10/7 - 6*t) - 8/15*sin(5/9 - 5*t) - 9/8*sin(3/2 - 4*t) + 533/10*sin(t + 2/3) + 31/9*sin(2*t + 29/7) + 44/7*sin(3*t + 24/11) + 1/3*sin(7*t + 8/7) + 3/7*sin(9*t + 10/3) + 2/11*sin(10*t + 11/5) + 1/16*sin(11*t + 20/7) + 1/9*sin(12*t + 2/9) + 2137/6)*step(39*math.pi - t)*step(t - 35*math.pi) + (-1/6*sin(3/7 - 33*t) - 1/15*sin(7/6 - 31*t) - 2/9*sin(3/7 - 29*t) - 1/7*sin(2/5 - 27*t) - 3/10*sin(1/9 - 19*t) - 6/11*sin(1/6 - 15*t) - 16/9*sin(8/7 - 6*t) - 102/11*sin(16/15 - 5*t) - 169/56*sin(9/10 - 4*t) - 187/10*sin(7/6 - 3*t) - 1941/16*sin(4/3 - t) + 395/8*sin(2*t + 11/9) + 19/13*sin(7*t + 45/11) + 17/8*sin(8*t + 100/33) + 4/7*sin(9*t + 47/10) + 3/7*sin(10*t + 12/5) + 13/7*sin(11*t + 3/4) + 4/7*sin(12*t + 4/3) + 3/7*sin(13*t + 23/22) + 9/14*sin(14*t + 111/28) + 1/7*sin(16*t + 75/19) + 1/8*sin(17*t + 3/11) + 5/8*sin(18*t + 19/5) + 1/68*sin(20*t + 37/8) + 2/7*sin(21*t + 7/5) + 3/8*sin(22*t + 30/11) + 1/6*sin(23*t + 4/9) + 1/6*sin(24*t + 23/10) + 1/4*sin(25*t + 4/5) + 1/5*sin(26*t + 30/13) + 1/8*sin(28*t + 27/8) + 3/11*sin(30*t + 37/12) + 1/6*sin(32*t + 10/3) + 3/11*sin(34*t + 20/7) + 656/11)*step(35*math.pi - t)*step(t - 31*math.pi) + (-28/11*sin(3/4 - 46*t) - 67/22*sin(4/7 - 42*t) - 29/11*sin(2/5 - 41*t) - 81/40*sin(6/5 - 40*t) - 70/9*sin(1/9 - 31*t) - 59/8*sin(6/5 - 25*t) - 133/12*sin(6/5 - 18*t) - 187/10*sin(1/14 - 14*t) - 79/9*sin(3/7 - 13*t) - 107/6*sin(23/24 - 11*t) - 350/11*sin(5/8 - 6*t) - 51/2*sin(12/11 - 3*t) + 6370/9*sin(t + 1/8) + 919/9*sin(2*t + 1/5) + 10/7*sin(4*t + 55/28) + 645/11*sin(5*t + 13/8) + 106/9*sin(7*t + 12/11) + 89/7*sin(8*t + 16/7) + 106/7*sin(9*t + 29/8) + 195/8*sin(10*t + 2/5) + 117/5*sin(12*t + 25/7) + 71/9*sin(15*t + 2/9) + 107/7*sin(16*t + 23/12) + 10*sin(17*t + 11/4) + 57/5*sin(19*t + 65/14) + 65/7*sin(20*t + 49/11) + 17/2*sin(21*t + 57/14) + 9/5*sin(22*t + 41/10) + 16/3*sin(23*t + 19/8) + 113/16*sin(24*t + 7/5) + 111/28*sin(26*t + 15/4) + 50/7*sin(27*t + 20/11) + 157/21*sin(28*t + 19/11) + 35/11*sin(29*t + 41/11) + 19/10*sin(30*t + 3/7) + 31/5*sin(32*t + 1/8) + 29/10*sin(33*t + 3/7) + 37/11*sin(34*t + 15/7) + 1/2*sin(35*t + 20/7) + 2*sin(36*t + 41/11) + 22/13*sin(37*t + 20/7) + 13/4*sin(38*t + 3/2) + 12/5*sin(39*t + 1/2) + 43/14*sin(43*t + 47/14) + 20/7*sin(44*t + 17/6) + 7/6*sin(45*t + 37/8) - 1582/13)*step(31*math.pi - t)*step(t - 27*math.pi) + (-5/8*sin(1/13 - 12*t) - 95/12*sin(17/18 - 5*t) - 65/9*sin(1/3 - 4*t) + 137/23*sin(t + 9/5) + 7/5*sin(2*t + 37/10) + 37/8*sin(3*t + 27/11) + 3*sin(6*t + 14/11) + 11/4*sin(7*t + 21/5) + 25/17*sin(8*t + 1/2) + 10/7*sin(9*t + 19/5) + 8/15*sin(10*t + 1) + 7/8*sin(11*t + 37/10) + 2957/8)*step(27*math.pi - t)*step(t - 23*math.pi) + (-1/2*sin(1/2 - 11*t) - 43/11*sin(1/48 - 7*t) - 23/2*sin(8/7 - 5*t) - 260/29*sin(4/7 - 4*t) - 31/6*sin(7/10 - 2*t) + 19/8*sin(t + 26/7) + 13/6*sin(3*t + 11/9) + 7/6*sin(6*t + 50/11) + 20/9*sin(8*t + 22/9) + 13/12*sin(9*t + 58/13) + 13/8*sin(10*t + 10/3) + 8/9*sin(12*t + 9/2) + 1663/7)*step(23*math.pi - t)*step(t - 19*math.pi) + (-3/7*sin(1/8 - 10*t) - 59/7*sin(5/4 - 5*t) + 1283/13*sin(t + 3/7) + 331/9*sin(2*t + 25/7) + 469/13*sin(3*t + 63/16) + 93/11*sin(4*t + 14/5) + 9/5*sin(6*t + 19/13) + 21/10*sin(7*t + 61/20) + 40/7*sin(8*t + 7/5) + 1/5*sin(9*t + 9/7) + 19/13*sin(11*t + 12/13) + 17/8*sin(12*t + 1/9) + 2425/7)*step(19*math.pi - t)*step(t - 15*math.pi) + (-2/7*sin(10/7 - 16*t) - 5/7*sin(22/15 - 14*t) - 25/11*sin(11/7 - 8*t) - 14/13*sin(1/5 - 7*t) - 29/8*sin(1/3 - 6*t) - 5*sin(11/7 - 4*t) + 349/5*sin(t + 11/8) + 286/9*sin(2*t + 20/7) + 49/5*sin(3*t + 31/16) + 27/4*sin(5*t + 22/15) + 3/10*sin(9*t + 19/5) + 10/11*sin(10*t + 27/8) + 2/3*sin(11*t + 20/13) + 2/7*sin(12*t + 17/4) + 9/8*sin(13*t + 3/2) + 2/7*sin(15*t + 5/7) + 1/8*sin(17*t + 35/9) + 2/7*sin(18*t + 105/26) + 2345/8)*step(15*math.pi - t)*step(t - 11*math.pi) + (-62/9*sin(3/5 - 9*t) + 35/4*sin(t + 22/9) + 39/8*sin(2*t + 10/3) + 97/9*sin(3*t + 22/13) + 8/3*sin(4*t + 3/5) + 91/6*sin(5*t + 2/9) + 75/8*sin(6*t + 43/10) + 117/7*sin(7*t + 47/10) + 113/4*sin(8*t + 4) + 27/2*sin(10*t + 1/7) + 37/3*sin(11*t + 17/5) + 7/2*sin(12*t + 4/11) + 12/5*sin(13*t + 42/11) + 5/14*sin(14*t + 41/11) + 3/4*sin(15*t + 32/9) + 18/7*sin(16*t + 8/17) + 25/12*sin(17*t + 21/5) + 5067/8)*step(11*math.pi - t)*step(t - 7*math.pi) + (-3/7*sin(3/8 - 16*t) - 3/2*sin(2/3 - 14*t) - 16/7*sin(2/11 - 12*t) - 10/7*sin(8/7 - 5*t) - 79/5*sin(8/11 - 3*t) - 361/11*sin(9/14 - 2*t) + 1151/11*sin(t + 5/7) + 7/5*sin(4*t + 16/5) + 50/11*sin(6*t + 1) + 16/7*sin(7*t + 23/5) + 59/29*sin(8*t + 8/17) + 31/9*sin(9*t + 19/5) + 47/23*sin(10*t + 2/5) + 16/9*sin(11*t + 36/11) + 7/5*sin(13*t + 112/37) + 9/7*sin(15*t + 20/7) + 5/8*sin(17*t + 17/9) + 1625/7)*step(7*math.pi - t)*step(t - 3*math.pi) + (-5/8*sin(29/19 - 28*t) - 19/9*sin(2/3 - 26*t) - 11/6*sin(15/11 - 19*t) - 22/5*sin(2/9 - 18*t) - 30/7*sin(6/11 - 16*t) - 74/25*sin(17/18 - 15*t) - 131/26*sin(10/7 - 9*t) - 166/5*sin(6/5 - 7*t) - 4668/13*sin(4/5 - t) + 360/7*sin(2*t + 34/11) + 169/3*sin(3*t + 13/6) + 221/7*sin(4*t + 7/11) + 240/7*sin(5*t + 41/10) + 175/9*sin(6*t + 3/5) + 91/6*sin(8*t + 77/26) + 14/5*sin(10*t + 1/6) + 45/11*sin(11*t + 25/9) + 32/5*sin(12*t + 147/37) + 59/13*sin(13*t + 7/6) + 19/7*sin(14*t + 20/7) + 23/12*sin(17*t + 18/7) + 19/8*sin(20*t + 91/30) + 12/5*sin(21*t + 21/5) + 25/6*sin(22*t + 21/11) + 12/5*sin(23*t + 27/7) + 6/5*sin(24*t + 16/11) + 11/7*sin(25*t + 21/10) + 3/4*sin(27*t + 85/28) + 29/10*sin(29*t + 20/19) + 1955/11)*step(3*math.pi - t)*step(t + math.pi))*step(sqrt(sgn(sin(t/2))))

def y(t):
    return ((-25/9*sin(11/7 - 7*t) - 24/7*sin(17/11 - 6*t) - 58/11*sin(11/7 - 5*t) - 3/5*sin(23/15 - 4*t) - 127/5*sin(11/7 - 3*t) + 1001/25*sin(t + 11/7) + 1028/21*sin(2*t + 11/7) - 3656/7)*step(75*math.pi - t)*step(t - 71*math.pi) + (-43/10*sin(11/7 - 3*t) - 595/8*sin(11/7 - t) + 152/17*sin(2*t + 11/7) + 23/7*sin(4*t + 11/7) - 5042/9)*step(71*math.pi - t)*step(t - 67*math.pi) + (-21/8*sin(14/9 - 13*t) - 71/6*sin(14/9 - 10*t) - 111/5*sin(11/7 - 6*t) - 1237/5*sin(11/7 - t) + 97/6*sin(2*t + 11/7) + 52/9*sin(3*t + 47/10) + 433/6*sin(4*t + 11/7) + 374/7*sin(5*t + 11/7) + 369/16*sin(7*t + 11/7) + 101/7*sin(8*t + 8/5) + 22/7*sin(9*t + 19/12) + 89/7*sin(11*t + 11/7) + sin(12*t + 17/10) + 5/7*sin(14*t + 17/11) + 37/11*sin(15*t + 8/5) + 6249/14)*step(67*math.pi - t)*step(t - 63*math.pi) + (-36/5*sin(11/7 - 4*t) - 101/7*sin(11/7 - 3*t) - 477/10*sin(11/7 - 2*t) + 28/3*sin(t + 11/7) + 21/8*sin(5*t + 11/7) + 1/6*sin(6*t + 11/7) - 24991/32)*step(63*math.pi - t)*step(t - 59*math.pi) + (-1/31*sin(7/9 - 12*t) - 7/8*sin(7/5 - 4*t) + 2165/8*sin(t + 11/7) + 19/7*sin(2*t + 3/2) + 317/10*sin(3*t + 11/7) + 124/11*sin(5*t + 11/7) + 5/11*sin(6*t + 11/8) + 37/6*sin(7*t + 11/7) + 3/7*sin(8*t + 3/2) + 24/7*sin(9*t + 11/7) + 1/7*sin(10*t + 9/7) + 16/7*sin(11*t + 11/7) - 3946/7)*step(59*math.pi - t)*step(t - 55*math.pi) + (-1/4*sin(17/12 - 12*t) - 144/13*sin(11/7 - 9*t) - 507/8*sin(11/7 - 3*t) - 2395/6*sin(11/7 - t) + 233/14*sin(2*t + 33/7) + 77/5*sin(4*t + 11/7) + 153/11*sin(5*t + 33/7) + 53/5*sin(6*t + 33/7) + 32/5*sin(7*t + 33/7) + 59/9*sin(8*t + 11/7) + 25/11*sin(10*t + 33/7) + 41/21*sin(11*t + 19/12) - 3661/8)*step(55*math.pi - t)*step(t - 51*math.pi) + (46/9*sin(t + 15/8) + 4523/12*sin(2*t + 11/7) + 121/7*sin(3*t + 32/7) + 419/8*sin(4*t + 8/5) + 9/2*sin(5*t + 22/5) + 78/5*sin(6*t + 5/3) + 150/13*sin(7*t + 5/3) + 345/11*sin(8*t + 19/12) + sin(9*t + 43/11) + 40/7*sin(10*t + 13/8) + 1/3*sin(11*t + 23/11) + 21/5*sin(12*t + 5/3) + 35/18*sin(13*t + 14/3) + 41/11*sin(14*t + 13/8) + 7/4*sin(15*t + 23/5) + 20/9*sin(16*t + 7/4) + 11/4*sin(17*t + 12/7) + 17/4*sin(18*t + 22/13) + 3/2*sin(19*t + 23/12) + 109/22*sin(20*t + 23/14) + 2/3*sin(21*t + 35/8) - 5990/11)*step(51*math.pi - t)*step(t - 47*math.pi) + (-3/2*sin(17/11 - 15*t) - 4/3*sin(14/9 - 13*t) - 22/7*sin(14/9 - 12*t) - 22/9*sin(14/9 - 10*t) - 12/13*sin(26/17 - 9*t) - 57/5*sin(11/7 - 8*t) - 30/7*sin(11/7 - 7*t) + 488/11*sin(t + 11/7) + 38/7*sin(2*t + 11/7) + 1/6*sin(3*t + 13/8) + 97/9*sin(4*t + 11/7) + 55/8*sin(5*t + 33/7) + 226/15*sin(6*t + 11/7) + 9/19*sin(11*t + 47/10) + 7/9*sin(14*t + 33/7) + 1/23*sin(16*t + 33/16) + 9/14*sin(17*t + 8/5) + 8/9*sin(18*t + 11/7) + 5/9*sin(19*t + 13/8) + 2/7*sin(20*t + 14/3) + 4217/7)*step(47*math.pi - t)*step(t - 43*math.pi) + (-5/7*sin(9/13 - 12*t) - 9/7*sin(10/7 - 11*t) - 14/11*sin(8/7 - 10*t) - 40/11*sin(12/11 - 9*t) - 51/5*sin(11/8 - 7*t) - 776/31*sin(11/9 - 4*t) - 1223/7*sin(3/2 - t) + 488/5*sin(2*t + 13/8) + 193/9*sin(3*t + 37/8) + 32/3*sin(5*t + 51/26) + 6/5*sin(6*t + 45/11) + 28/5*sin(8*t + 41/20) - 13472/13)*step(43*math.pi - t)*step(t - 39*math.pi) + (-5/11*sin(15/11 - 9*t) - 4/13*sin(1/7 - 8*t) - 27/4*sin(1/7 - 2*t) - 897/11*sin(7/10 - t) + 3/5*sin(7*t) + 27/7*sin(3*t + 20/9) + 35/8*sin(4*t + 13/10) + 38/15*sin(5*t + 37/8) + 17/10*sin(6*t + 23/8) + 2/3*sin(10*t + 20/9) + 4/7*sin(11*t + 1/36) + 4/11*sin(12*t + 26/7) + 2573/26)*step(39*math.pi - t)*step(t - 35*math.pi) + (-2/9*sin(3/7 - 32*t) - 1/4*sin(1/13 - 22*t) - 9/14*sin(1/3 - 20*t) - 5/8*sin(1 - 18*t) - 20/9*sin(11/8 - 6*t) - 38/7*sin(7/13 - 5*t) - 241/16*sin(1/6 - 3*t) + 1963/11*sin(t + 12/11) + 734/21*sin(2*t + 7/6) + 13/14*sin(4*t + 1/3) + 11/8*sin(7*t + 25/6) + 22/21*sin(8*t + 19/6) + 26/17*sin(9*t + 39/10) + 11/12*sin(10*t + 22/9) + 27/28*sin(11*t + 37/15) + 5/6*sin(12*t + 6/7) + 5/4*sin(13*t + 7/3) + 10/11*sin(14*t + 1/15) + 1/7*sin(15*t + 10/7) + 14/15*sin(16*t + 1/22) + 2/7*sin(17*t + 25/7) + 5/12*sin(19*t + 25/7) + 7/9*sin(21*t + 28/9) + 1/2*sin(23*t + 42/13) + 5/11*sin(24*t + 1/3) + 2/5*sin(25*t + 14/5) + 5/11*sin(26*t + 1/4) + 4/11*sin(27*t + 37/11) + 3/7*sin(28*t + 1/61) + 1/7*sin(29*t + 48/13) + 3/11*sin(30*t + 1/7) + 1/3*sin(31*t + 18/5) + 2/9*sin(33*t + 7/2) + 1/6*sin(34*t + 7/11) + 1739/6)*step(35*math.pi - t)*step(t - 31*math.pi) + (-13/9*sin(2/7 - 39*t) - 5/4*sin(2/11 - 38*t) - 35/13*sin(5/9 - 37*t) - 20/9*sin(3/2 - 32*t) - 31/7*sin(7/5 - 29*t) - 47/8*sin(11/10 - 28*t) - 68/9*sin(2/9 - 27*t) - 116/11*sin(5/9 - 23*t) - 57/5*sin(3/5 - 15*t) - 37/5*sin(17/11 - 14*t) - 221/10*sin(14/9 - 13*t) - 135/7*sin(10/11 - 10*t) - 981/20*sin(3/7 - 5*t) - 1561/30*sin(1/53 - 3*t) + 529*sin(t + 33/7) + 979/6*sin(2*t + 22/13) + 667/6*sin(4*t + 41/12) + 93/2*sin(6*t + 5/3) + 703/12*sin(7*t + 49/13) + 1831/61*sin(8*t + 4/9) + 136/5*sin(9*t + 32/9) + 115/6*sin(11*t + 16/5) + 116/9*sin(12*t + 64/21) + 119/6*sin(16*t + 10/11) + 69/14*sin(17*t + 53/15) + 95/11*sin(18*t + 14/5) + 224/15*sin(19*t + 4) + 35/3*sin(20*t + 16/9) + 75/19*sin(21*t + 24/23) + 7*sin(22*t + 33/32) + 27/10*sin(24*t + 19/6) + 48/7*sin(25*t + 7/9) + 50/9*sin(26*t + 13/6) + 39/10*sin(30*t + 31/7) + 68/15*sin(31*t + 17/5) + 13/10*sin(33*t + 22/5) + 15/8*sin(34*t + 4/7) + 17/5*sin(35*t + 2/3) + 8/3*sin(36*t + 8/11) + 13/7*sin(40*t + 3/2) + 15/11*sin(41*t + 16/5) + 11/7*sin(42*t + 19/10) + 11/12*sin(43*t + 25/9) + 25/13*sin(44*t + 5/3) + 14/13*sin(45*t + 10/19) + 1/5*sin(46*t + 43/11) - 2967/5)*step(31*math.pi - t)*step(t - 27*math.pi) + (-3/4*sin(7/5 - 9*t) - 36/7*sin(3/2 - 7*t) - 739/29*sin(1/5 - 5*t) - 64/9*sin(11/9 - 2*t) + 121/20*sin(t + 13/8) + 83/10*sin(3*t + 22/7) + 137/8*sin(4*t + 3/7) + 73/9*sin(6*t + 16/9) + 17/7*sin(8*t + 13/9) + 2/5*sin(10*t + 29/8) + 7/11*sin(11*t + 9/5) + 5/4*sin(12*t + 1/6) + 2164/3)*step(27*math.pi - t)*step(t - 23*math.pi) + (-11/7*sin(5/8 - 12*t) - 54/7*sin(7/6 - 9*t) - 32/9*sin(5/8 - 6*t) + 53/10*sin(t + 29/8) + 651/65*sin(2*t + 12/11) + 35/6*sin(3*t + 41/11) + 221/8*sin(4*t + 17/16) + 349/10*sin(5*t + 1/10) + 101/9*sin(7*t + 5/4) + 87/8*sin(8*t + 37/12) + 53/9*sin(10*t + 8/9) + 32/11*sin(11*t + 36/11) + 2281/3)*step(23*math.pi - t)*step(t - 19*math.pi) + (-7/5*sin(7/6 - 12*t) - 3/8*sin(5/7 - 11*t) - 15/8*sin(1/24 - 8*t) + 471/11*sin(t + 17/7) + 539/4*sin(2*t + 51/13) + 162/13*sin(3*t + 19/8) + 9/5*sin(4*t + 3/8) + 13/5*sin(5*t + 6/11) + 86/11*sin(6*t + 33/14) + 4*sin(7*t + 11/7) + 9/8*sin(9*t + 29/9) + 11/6*sin(10*t + 3/4) + 11349/14)*step(19*math.pi - t)*step(t - 15*math.pi) + (-3/7*sin(1/22 - 15*t) - 13/8*sin(3/7 - 11*t) - 39/20*sin(5/8 - 7*t) - 41/2*sin(1/7 - 3*t) - 427/6*sin(9/17 - t) + 509/8*sin(2*t + 9/7) + 61/9*sin(4*t + 50/11) + 40/9*sin(5*t + 4) + 13/5*sin(6*t + 15/7) + 4/9*sin(8*t + 22/7) + 4/9*sin(9*t + 29/10) + 7/4*sin(10*t + 25/13) + 12/13*sin(12*t + 86/19) + 1/5*sin(13*t + 127/32) + 5/11*sin(14*t + 25/11) + 3/8*sin(16*t + 10/3) + 5/14*sin(17*t + 25/7) + 3/8*sin(18*t + 25/17) + 2721/8)*step(15*math.pi - t)*step(t - 11*math.pi) + (-5/8*sin(1/11 - 14*t) - 38/7*sin(2/5 - 12*t) - 144/11*sin(4/7 - 10*t) - 272/21*sin(37/38 - 5*t) + 125/14*sin(t + 7/9) + 33/4*sin(2*t + 1/6) + 86/9*sin(3*t + 11/9) + 56/13*sin(4*t + 2) + 89/7*sin(6*t + 26/7) + 254/15*sin(7*t + 24/7) + 256/11*sin(8*t + 44/15) + 74/11*sin(9*t + 9/2) + 65/6*sin(11*t + 14/5) + 13/5*sin(13*t + 19/7) + 81/20*sin(15*t + 37/11) + 19/5*sin(16*t + 1/7) + 15/8*sin(17*t + 43/17) + 3666/7)*step(11*math.pi - t)*step(t - 7*math.pi) + (-45/44*sin(8/9 - 6*t) - 29/8*sin(7/5 - 4*t) - 81/4*sin(3/8 - 2*t) + 1897/9*sin(t + 49/11) + 153/7*sin(3*t + 57/14) + 53/11*sin(5*t + 71/24) + 1/2*sin(7*t + 16/9) + 20/19*sin(8*t + 27/7) + 1/4*sin(9*t + 23/7) + sin(10*t + 7/3) + 3/11*sin(11*t + 1/4) + 6/11*sin(12*t + 10/9) + 1/9*sin(13*t + 6/5) + 3/5*sin(14*t + 1/4) + 1/7*sin(15*t + 71/24) + 1/3*sin(16*t + 3/10) + 2/7*sin(17*t + 8/9) + 4877/11)*step(7*math.pi - t)*step(t - 3*math.pi) + (-18/7*sin(1/3 - 29*t) - 7/8*sin(13/10 - 28*t) - 37/6*sin(4/5 - 13*t) - 37/10*sin(1/29 - 12*t) - 61/4*sin(3/2 - 10*t) - 12*sin(8/7 - 9*t) + 2164/7*sin(t + 38/9) + 8287/37*sin(2*t + 5/8) + 133*sin(3*t + 17/18) + 220/3*sin(4*t + 7/11) + 133/10*sin(5*t + 1/4) + 137/9*sin(6*t + 7/5) + 365/17*sin(7*t + 19/5) + 61/5*sin(8*t + 1/4) + 63/10*sin(11*t + 4/5) + 59/13*sin(14*t + 17/6) + 21/8*sin(15*t + 51/14) + 21/5*sin(16*t + 25/8) + 6/7*sin(17*t + 25/8) + 5/2*sin(18*t + 37/8) + 39/11*sin(19*t + 35/8) + 20/7*sin(20*t + 11/7) + 9/8*sin(21*t + 35/9) + 25/17*sin(22*t + 2/3) + 17/4*sin(23*t + 13/6) + 8/9*sin(24*t + 1/30) + 5/3*sin(25*t + 9/5) + 13/7*sin(26*t + 13/3) + 20/9*sin(27*t + 7/5) + 6793/12)*step(3*math.pi - t)*step(t + math.pi))*step(sqrt(sgn(sin(t/2))))

def dist(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

pi_count = 76
div_const = 4
steps_per_pi = 25


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