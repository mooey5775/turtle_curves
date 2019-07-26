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
    return ((-13/5*sin(7/6 - 118*t) - 9/8*sin(4/7 - 103*t) - 16/5*sin(3/2 - 100*t) - 149/30*sin(11/9 - 81*t) - 69/17*sin(13/9 - 80*t) - 71/13*sin(3/2 - 76*t) - 62/7*sin(10/7 - 70*t) - 15/4*sin(2/3 - 68*t) - 10*sin(10/7 - 66*t) - 89/7*sin(10/7 - 64*t) - 128/9*sin(3/2 - 62*t) - 25/2*sin(7/5 - 60*t) - 100/7*sin(17/11 - 58*t) - 324/17*sin(11/7 - 40*t) - 42/5*sin(4/3 - 37*t) - 103/5*sin(7/5 - 30*t) - 141/5*sin(10/7 - 23*t) - 36/7*sin(6/7 - 20*t) - 284/19*sin(23/15 - 8*t) - 8/3*sin(6/5 - 2*t) + 3241/5*sin(t + 11/7) + 437/6*sin(3*t + 17/11) + 399/10*sin(4*t + 11/7) + 181/12*sin(5*t + 11/7) + 17/7*sin(6*t + 7/5) + 34*sin(7*t + 11/7) + 58/7*sin(9*t + 11/7) + 158/9*sin(10*t + 8/5) + 60/7*sin(11*t + 15/11) + 20/9*sin(12*t + 8/15) + 13*sin(13*t + 8/5) + 49/8*sin(14*t + 20/13) + 210/19*sin(15*t + 10/7) + 22/5*sin(16*t + 4/3) + 41/8*sin(17*t + 23/15) + 87/5*sin(18*t + 8/5) + 42/5*sin(19*t + 13/8) + 44/3*sin(21*t + 17/11) + 14*sin(22*t + 3/2) + 29/2*sin(24*t + 9/7) + 347/7*sin(25*t + 8/5) + 359/10*sin(26*t + 35/8) + 833/8*sin(27*t + 37/8) + 528/7*sin(28*t + 7/5) + 527/4*sin(29*t + 7/5) + 1202/13*sin(31*t + 32/7) + 1361/34*sin(32*t + 37/9) + 401/11*sin(33*t + 22/5) + 326/9*sin(34*t + 51/11) + 94/3*sin(35*t + 10/7) + 25*sin(36*t + 8/7) + 694/11*sin(38*t + 11/8) + 399/20*sin(39*t + 7/5) + 396/5*sin(41*t + 13/9) + 549/11*sin(42*t + 14/3) + 216/7*sin(43*t + 11/8) + 54/7*sin(44*t + 8/5) + 109/3*sin(45*t + 51/11) + 243/7*sin(46*t + 20/13) + 165/4*sin(47*t + 41/9) + 449/25*sin(48*t + 8/5) + 185/9*sin(49*t + 41/9) + 53/9*sin(50*t + 11/5) + 139/10*sin(51*t + 33/7) + 15/4*sin(52*t + 19/6) + 21/2*sin(53*t + 33/7) + 61/7*sin(54*t + 14/3) + 192/11*sin(55*t + 3/2) + 67/4*sin(56*t + 33/7) + 89/9*sin(57*t + 19/10) + 151/9*sin(59*t + 8/5) + 73/5*sin(61*t + 8/5) + 48/5*sin(63*t + 11/6) + 241/16*sin(65*t + 11/7) + 89/5*sin(67*t + 7/5) + 52/5*sin(69*t + 10/7) + 145/12*sin(71*t + 13/8) + 91/8*sin(72*t + 47/10) + 2*sin(73*t + 12/5) + 38/5*sin(74*t + 58/13) + 62/9*sin(75*t + 12/7) + 13/9*sin(77*t + 32/13) + 19/6*sin(78*t + 3/4) + 46/7*sin(79*t + 18/11) + 27/2*sin(82*t + 7/6) + 89/9*sin(83*t + 11/8) + 109/8*sin(84*t + 13/3) + 19/7*sin(85*t + 107/27) + 34/3*sin(86*t + 6/5) + 63/8*sin(87*t + 4/7) + 173/29*sin(88*t + 9/10) + 19/4*sin(89*t + 38/9) + 16/3*sin(90*t + 23/7) + 37/12*sin(91*t + 4) + 25/3*sin(92*t + 6/5) + 81/11*sin(93*t + 2/3) + 34/5*sin(94*t + 5/7) + 59/9*sin(95*t + 6/7) + 29/9*sin(96*t + 10/7) + 32/9*sin(97*t + 31/8) + 10/3*sin(98*t + 29/8) + 11/8*sin(99*t + 17/8) + 15/11*sin(101*t + 1/2) + 15/7*sin(102*t + 3/7) + 19/13*sin(104*t + 25/26) + 47/23*sin(105*t + 8/5) + 53/9*sin(106*t + 35/8) + 26/9*sin(107*t + 67/17) + 12/5*sin(108*t + 29/8) + 53/7*sin(109*t + 17/4) + 65/7*sin(110*t + 17/4) + 43/8*sin(111*t + 4) + 47/12*sin(112*t + 49/12) + 28/5*sin(113*t + 53/13) + 65/9*sin(114*t + 27/7) + 33/7*sin(115*t + 23/6) + 31/8*sin(116*t + 17/4) + 15/8*sin(117*t + 1/20) + 12/5*sin(119*t + 61/15) + 4/7*sin(120*t + 25/7) + 461/8)*step(155*math.pi - t)*step(t - 151*math.pi) + (-37/6*sin(11/7 - 3*t) - 812/13*sin(11/7 - t) + 138/11*sin(2*t + 11/7) + 20/9*sin(4*t + 11/7) - 4494/19)*step(151*math.pi - t)*step(t - 147*math.pi) + (-15/8*sin(11/7 - 4*t) - 205/51*sin(11/7 - 2*t) + 151/6*sin(t + 11/7) + 16/5*sin(3*t + 11/7) + 2599/9)*step(147*math.pi - t)*step(t - 143*math.pi) + (-16/5*sin(14/9 - 41*t) - 124/41*sin(11/7 - 39*t) - 43/11*sin(14/9 - 31*t) - 9/2*sin(11/7 - 17*t) - 55/14*sin(14/9 - 16*t) - 133/8*sin(14/9 - 11*t) - 169/11*sin(14/9 - 6*t) - 307/8*sin(14/9 - 5*t) + 3457/3*sin(t + 11/7) + 603/4*sin(2*t + 11/7) + 1175/6*sin(3*t + 33/7) + 336/5*sin(4*t + 33/7) + 92/5*sin(7*t + 47/10) + 135/17*sin(8*t + 13/8) + 39/38*sin(9*t + 59/13) + 57/5*sin(10*t + 8/5) + 121/8*sin(12*t + 11/7) + 123/10*sin(13*t + 33/7) + 12/7*sin(14*t + 13/7) + 12/7*sin(15*t + 12/7) + 31/7*sin(18*t + 14/3) + 70/9*sin(19*t + 47/10) + 34/9*sin(20*t + 47/10) + 71/18*sin(21*t + 47/10) + 1/5*sin(22*t + 32/11) + 23/4*sin(23*t + 33/7) + 11/7*sin(24*t + 12/7) + 82/15*sin(25*t + 33/7) + 7/4*sin(26*t + 37/8) + 26/9*sin(27*t + 33/7) + 23/6*sin(28*t + 14/3) + 13/7*sin(29*t + 23/5) + 9/10*sin(30*t + 41/9) + 13/8*sin(32*t + 13/8) + 23/8*sin(33*t + 14/3) + 5/3*sin(34*t + 14/3) + 11/5*sin(35*t + 5/3) + 10/3*sin(36*t + 47/10) + 12/7*sin(37*t + 8/5) + sin(38*t + 14/9) + 7/3*sin(40*t + 5/3) + 1/6*sin(42*t + 5/2) + 63/31*sin(43*t + 47/10) + 10/7*sin(44*t + 14/3) + 1/2*sin(45*t + 51/11) + 11/10*sin(46*t + 14/3) + 1/6*sin(47*t + 11/6) + 9/7*sin(48*t + 8/5) + 3/11*sin(49*t + 49/11) + 1/6*sin(50*t + 30/7) + 2/7*sin(51*t + 17/8) - 989/8)*step(143*math.pi - t)*step(t - 139*math.pi) + (46/5*sin(t + 11/7) + 118/5*sin(2*t + 33/7) + 13/12*sin(3*t + 14/3) + 326)*step(139*math.pi - t)*step(t - 135*math.pi) + (-93/2*sin(11/7 - 3*t) + 309/5*sin(t + 11/7) + 472/11*sin(2*t + 11/7) + 2/7*sin(4*t + 4/3) - 200/3)*step(135*math.pi - t)*step(t - 131*math.pi) + (1487/8*sin(t + 11/7) + sin(2*t + 16/11) + 93/5*sin(3*t + 11/7) + 6/5*sin(4*t + 17/11) - 287/4)*step(131*math.pi - t)*step(t - 127*math.pi) + (1116/7*sin(t + 11/7) + 101/4*sin(2*t + 11/7) + 74/5*sin(3*t + 11/7) + 52/9*sin(4*t + 14/9) - 1911/4)*step(127*math.pi - t)*step(t - 123*math.pi) + (-3*sin(7/5 - 18*t) - 31/6*sin(14/9 - 16*t) - 1/6*sin(8/7 - 15*t) - 7*sin(17/11 - 14*t) - 7/6*sin(27/28 - 12*t) - 25*sin(14/9 - 4*t) + 313/12*sin(t + 11/7) + 326/13*sin(2*t + 33/7) + 61/3*sin(3*t + 11/7) + 187/6*sin(5*t + 11/7) + 645/11*sin(6*t + 33/7) + 671/9*sin(7*t + 8/5) + 1665/32*sin(8*t + 13/8) + 23/7*sin(9*t + 125/31) + 57/29*sin(10*t + 13/6) + 9/4*sin(11*t + 3/2) + 7/2*sin(13*t + 13/9) + 13/6*sin(17*t + 10/7) + 2*sin(19*t + 10/7) + 1/9*sin(20*t + 35/12) + 30/7*sin(21*t + 14/3) + 19/8*sin(22*t + 7/4) + 46/9*sin(23*t + 13/8) + 7730/9)*step(123*math.pi - t)*step(t - 119*math.pi) + (-8/3*sin(17/11 - 22*t) - 37/7*sin(3/2 - 20*t) - 59/4*sin(17/11 - 15*t) - 80/9*sin(11/7 - 2*t) + 236/7*sin(t + 11/7) + 48/7*sin(3*t + 11/7) + 18/7*sin(4*t + 17/11) + 131/26*sin(5*t + 11/7) + 5/2*sin(6*t + 23/15) + 13/2*sin(7*t + 14/9) + 1/4*sin(8*t + 49/48) + 29/7*sin(9*t + 14/9) + 82/9*sin(10*t + 20/13) + 41/4*sin(11*t + 23/15) + 21/5*sin(12*t + 10/7) + 321/20*sin(13*t + 14/9) + 106/5*sin(14*t + 11/7) + 31/9*sin(16*t + 33/7) + 27/8*sin(17*t + 11/7) + 1/43*sin(18*t + 35/34) + 47/7*sin(19*t + 11/7) + 48/11*sin(21*t + 11/7) + 17/4*sin(23*t + 8/5) + 2*sin(24*t + 33/7) + 855)*step(119*math.pi - t)*step(t - 115*math.pi) + (-23/7*sin(11/7 - 27*t) - 120/7*sin(11/7 - 12*t) - 181/6*sin(11/7 - 8*t) - 19/6*sin(14/9 - 3*t) - 189/8*sin(11/7 - t) + 55/6*sin(2*t + 14/9) + 299/12*sin(4*t + 11/7) + 1/6*sin(5*t + 3/5) + 719/24*sin(6*t + 11/7) + 82/7*sin(7*t + 17/11) + 49/24*sin(9*t + 13/10) + 732/7*sin(10*t + 11/7) + 96/7*sin(11*t + 17/11) + 62/5*sin(13*t + 11/7) + 309/8*sin(14*t + 47/10) + 25/6*sin(15*t + 23/5) + 91/4*sin(16*t + 47/10) + 76/9*sin(17*t + 37/8) + 1/4*sin(18*t + 3) + 136/11*sin(19*t + 14/3) + 7/4*sin(20*t + 12/7) + 10*sin(21*t + 33/7) + 33/5*sin(22*t + 8/5) + 9*sin(23*t + 33/7) + sin(24*t + 2) + 119/9*sin(25*t + 47/10) + 91/11*sin(26*t + 13/8) + 59/7*sin(28*t + 14/3) + 39/5*sin(29*t + 33/7) + 97/14*sin(30*t + 8/5) + 23/10*sin(31*t + 33/7) + 3/4*sin(32*t + 2) - 11397/14)*step(115*math.pi - t)*step(t - 111*math.pi) + (39/7*sin(t + 11/7) + 29/6*sin(2*t + 11/7) + 11/3*sin(3*t + 8/5) + 5/9*sin(4*t + 8/5) - 5325/7)*step(111*math.pi - t)*step(t - 107*math.pi) + (-2/7*sin(14/9 - 4*t) - 36/7*sin(11/7 - 2*t) + 779/9*sin(t + 11/7) + 51/5*sin(3*t + 11/7) + 7/2*sin(5*t + 11/7) + 3044/9)*step(107*math.pi - t)*step(t - 103*math.pi) + (-38/3*sin(11/7 - 2*t) + 2619/20*sin(t + 11/7) + 82/7*sin(3*t + 11/7) + 5266/27)*step(103*math.pi - t)*step(t - 99*math.pi) + (2867/12*sin(t + 11/7) + 95/6*sin(2*t + 8/5) + 155/9*sin(3*t + 11/7) + 14/3*sin(4*t + 8/5) + 31/5*sin(5*t + 8/5) + 12/7*sin(6*t + 18/11) + 25/6*sin(7*t + 8/5) + 1/9*sin(8*t + 15/4) + 18/7*sin(9*t + 8/5) + 1/6*sin(10*t + 9/2) + 10/7*sin(11*t + 8/5) + 1/15*sin(12*t + 23/10) - 113)*step(99*math.pi - t)*step(t - 95*math.pi) + (-487/8*sin(11/7 - t) + 11/3*sin(2*t + 11/7) + 362/7*sin(3*t + 11/7) + 123/13*sin(4*t + 33/7) + 64/3*sin(5*t + 11/7) + 11/9*sin(6*t + 37/8) + 143/6*sin(7*t + 11/7) + 33/7*sin(8*t + 47/10) + 31/3*sin(9*t + 11/7) + 22/9*sin(10*t + 33/7) + 45/13*sin(11*t + 8/5) + 41/9*sin(12*t + 8/5) + 31/16*sin(13*t + 11/7) + 4*sin(14*t + 33/7) + 7/6*sin(15*t + 8/5) + 29/10*sin(16*t + 8/5) + 19/7*sin(17*t + 33/7) + 49/25*sin(18*t + 8/5) + 8/5*sin(19*t + 8/5) + 4/9*sin(20*t + 23/5) + 12/5*sin(21*t + 8/5) - 10319/12)*step(95*math.pi - t)*step(t - 91*math.pi) + (-5/8*sin(3/2 - 17*t) - 5/4*sin(14/9 - 13*t) - 6/5*sin(17/11 - 9*t) - 1/21*sin(2/3 - 8*t) - 65/8*sin(14/9 - 7*t) - 28/3*sin(14/9 - 6*t) - 39/8*sin(11/7 - 5*t) - 32/7*sin(11/7 - 4*t) - 344/15*sin(11/7 - 3*t) + 541/15*sin(t + 11/7) + 71/8*sin(2*t + 11/7) + 2/9*sin(10*t + 4/3) + 1/19*sin(11*t + 31/7) + 2/3*sin(12*t + 8/5) + 1/20*sin(14*t + 10/7) + 3/2*sin(15*t + 13/8) + 3/7*sin(16*t + 11/7) + 5251/7)*step(91*math.pi - t)*step(t - 87*math.pi) + (-418/3*sin(11/7 - t) + 17/7*sin(2*t + 33/7) - 2149/12)*step(87*math.pi - t)*step(t - 83*math.pi) + (-3/4*sin(3/2 - 12*t) - 7/5*sin(11/7 - 11*t) - 11/3*sin(3/2 - 10*t) - 167/5*sin(14/9 - 7*t) - 77/8*sin(14/9 - 4*t) - 257/6*sin(11/7 - 3*t) - 548/7*sin(11/7 - 2*t) - 1531/15*sin(11/7 - t) + 25/3*sin(5*t + 8/5) + 47/8*sin(6*t + 11/7) + 103/7*sin(8*t + 8/5) + 12/7*sin(9*t + 33/7) + 8053/13)*step(83*math.pi - t)*step(t - 79*math.pi) + (-6/5*sin(14/9 - 4*t) - 4*sin(11/7 - 2*t) + 295/2*sin(t + 11/7) + 55/4*sin(3*t + 11/7) + 4*sin(5*t + 11/7) + 5/6*sin(6*t + 33/7) + 19/8*sin(7*t + 11/7) + 2/7*sin(8*t + 14/3) + 18/11*sin(9*t + 8/5) + 1/11*sin(10*t + 33/7) + 11/9*sin(11*t + 11/7) + 1/12*sin(12*t + 19/11) + 931/2)*step(79*math.pi - t)*step(t - 75*math.pi) + (-1/2*sin(2/3 - 26*t) - 15/8*sin(3/4 - 23*t) - 11/6*sin(5/9 - 18*t) - 11/5*sin(6/5 - 15*t) - 12/5*sin(5/7 - 13*t) - 78/11*sin(12/13 - 8*t) - 203/10*sin(11/9 - 7*t) - 51/11*sin(7/11 - 4*t) - 145/6*sin(10/7 - 3*t) + 742/5*sin(t + 13/8) + 186/7*sin(2*t + 5/3) + 41/4*sin(5*t + 14/3) + 27/2*sin(6*t + 17/10) + 64/7*sin(9*t + 43/21) + 43/11*sin(10*t + 17/6) + 75/8*sin(11*t + 29/14) + 7/4*sin(12*t + 16/5) + 8/5*sin(14*t + 11/6) + 7/8*sin(16*t + 1) + 11/9*sin(17*t + 20/7) + 3/7*sin(19*t + 5/9) + 11/7*sin(20*t + 14/5) + 10/11*sin(21*t + 4) + 7/5*sin(22*t + 23/12) + 4/3*sin(24*t + 7/11) + 1/3*sin(25*t + 11/3) + 6/5*sin(27*t + 77/26) + 6/5*sin(28*t + 25/7) + 3/2*sin(29*t + 1/5) + 13/10*sin(30*t + 4/5) + 483/4)*step(75*math.pi - t)*step(t - 71*math.pi) + (-12/7*sin(11/7 - 5*t) - 13/4*sin(14/9 - 2*t) - 251/4*sin(11/7 - t) + 23/5*sin(3*t + 33/7) + 2/9*sin(4*t + 37/8) - 288/5)*step(71*math.pi - t)*step(t - 67*math.pi) + (274/5*sin(t + 33/7) + 83/3*sin(2*t + 33/7) + 11*sin(3*t + 11/7) + 187/8*sin(4*t + 33/7) + 37/8*sin(5*t + 33/7) + 22/5*sin(6*t + 11/7) + 33/8*sin(7*t + 11/7) + 139/28*sin(8*t + 33/7) + 15/4*sin(9*t + 33/7) + 13/9*sin(10*t + 11/7) + 6/5*sin(11*t + 11/7) + 2815/9)*step(67*math.pi - t)*step(t - 63*math.pi) + (-59/10*sin(20/13 - 11*t) - 112/15*sin(10/7 - 8*t) - 212/5*sin(3/2 - 7*t) - 449/18*sin(3/2 - 6*t) - 109/10*sin(13/9 - 5*t) - 271/5*sin(11/7 - 3*t) - 3359/21*sin(11/7 - t) + 1088/11*sin(2*t + 11/7) + 58/7*sin(4*t + 13/9) + 93/8*sin(9*t + 8/5) + 65/7*sin(10*t + 8/5) + 2/5*sin(12*t + 6/5) - 2466/7)*step(63*math.pi - t)*step(t - 59*math.pi) + (-1/5*sin(3/2 - 5*t) - 51/10*sin(11/7 - 3*t) + 1451/8*sin(t + 11/7) + 227/6*sin(2*t + 11/7) + 101/7*sin(4*t + 11/7) + 11/10*sin(6*t + 11/7) + 3652/9)*step(59*math.pi - t)*step(t - 55*math.pi) + (-91/45*sin(11/7 - 5*t) - 169/34*sin(11/7 - 4*t) - 31/9*sin(11/7 - 3*t) - 159/10*sin(11/7 - 2*t) - 1013/23*sin(11/7 - t) + 834/7)*step(55*math.pi - t)*step(t - 51*math.pi) + (-8/7*sin(13/9 - 38*t) - 5/3*sin(20/13 - 30*t) - 44/7*sin(17/11 - 26*t) - 13/5*sin(3/2 - 19*t) - 137/23*sin(3/2 - 17*t) - 2/5*sin(6/7 - 14*t) - 13/5*sin(10/7 - 12*t) - 19/6*sin(14/9 - 9*t) - 7/10*sin(3/2 - 6*t) - 85/13*sin(14/9 - 4*t) - 51/8*sin(14/9 - 2*t) + 1059/7*sin(t + 11/7) + 22/5*sin(3*t + 8/5) + 95/8*sin(5*t + 11/7) + 37/9*sin(7*t + 11/7) + 3/7*sin(8*t + 8/5) + 45/7*sin(10*t + 14/9) + 145/16*sin(11*t + 11/7) + 85/8*sin(13*t + 11/7) + 11/2*sin(15*t + 17/11) + 176/25*sin(16*t + 11/7) + 117/8*sin(18*t + 11/7) + 22/5*sin(20*t + 37/8) + 15/4*sin(21*t + 32/7) + 131/7*sin(22*t + 14/3) + 491/49*sin(23*t + 14/3) + 57/8*sin(24*t + 11/7) + 53/5*sin(25*t + 11/7) + 8/7*sin(27*t + 5/3) + 5/7*sin(28*t + 7/5) + 21/11*sin(29*t + 8/5) + 13/5*sin(31*t + 14/9) + 11/12*sin(32*t + 9/7) + 8/3*sin(33*t + 23/15) + 1/4*sin(34*t + 4/7) + 25/9*sin(35*t + 20/13) + 11/5*sin(36*t + 13/9) + 18/7*sin(37*t + 20/13) + 9147/17)*step(51*math.pi - t)*step(t - 47*math.pi) + (-2/3*sin(14/9 - 36*t) - 23/5*sin(10/7 - 35*t) - 40/11*sin(19/13 - 33*t) - 11/7*sin(7/5 - 32*t) - 36/7*sin(14/9 - 21*t) - 165/8*sin(3/2 - 20*t) - 38/7*sin(3/2 - 17*t) - 70/23*sin(14/9 - 16*t) - 31/6*sin(14/9 - 11*t) - 146/21*sin(14/9 - 10*t) - 61/6*sin(11/7 - 2*t) + 1014/5*sin(t + 11/7) + 22*sin(3*t + 11/7) + 1/6*sin(4*t + 34/9) + 27/8*sin(5*t + 8/5) + 12/13*sin(6*t + 12/7) + 141/35*sin(7*t + 8/5) + 83/11*sin(8*t + 8/5) + 9/8*sin(9*t + 5/3) + 3/2*sin(12*t + 13/8) + 117/29*sin(13*t + 13/8) + 72/11*sin(14*t + 8/5) + 36/5*sin(15*t + 8/5) + 33/5*sin(18*t + 13/8) + 9/8*sin(19*t + 41/9) + 115/6*sin(22*t + 18/11) + 77/8*sin(23*t + 8/5) + 47/12*sin(24*t + 5/3) + 38/5*sin(25*t + 5/3) + 2/3*sin(26*t + 37/8) + 4*sin(27*t + 5/3) + 35/12*sin(28*t + 9/5) + 20/7*sin(29*t + 13/8) + 1/7*sin(30*t + 6/7) + 23/7*sin(31*t + 7/4) + 37/7*sin(34*t + 5/3) + 53/26*sin(37*t + 17/10) - 2507/11)*step(47*math.pi - t)*step(t - 43*math.pi) + (-2/5*sin(14/9 - 30*t) - 13/8*sin(14/9 - 20*t) - 5/9*sin(14/9 - 12*t) - 66/7*sin(11/7 - 10*t) - 632/11*sin(11/7 - 2*t) + 477/17*sin(t + 11/7) + 109/4*sin(3*t + 33/7) + 215/11*sin(4*t + 33/7) + 63/8*sin(5*t + 33/7) + 1/21*sin(6*t + 2) + sin(7*t + 14/9) + 28/5*sin(8*t + 11/7) + 18/5*sin(9*t + 33/7) + 17/8*sin(11*t + 8/5) + 9/10*sin(13*t + 11/7) + 11/10*sin(14*t + 47/10) + 1/14*sin(15*t + 22/5) + 17/10*sin(16*t + 33/7) + 1/2*sin(17*t + 14/3) + 15/14*sin(18*t + 33/7) + 7/3*sin(19*t + 8/5) + 1/7*sin(21*t + 49/11) + 3/5*sin(22*t + 14/3) + 1/11*sin(23*t + 10/7) + 1/4*sin(24*t + 33/7) + 1/3*sin(25*t + 8/5) + 4/9*sin(26*t + 47/10) + 1/3*sin(28*t + 37/8) + 1/4*sin(29*t + 12/7) + 473/10)*step(43*math.pi - t)*step(t - 39*math.pi) + (-3/4*sin(20/13 - 21*t) - 5/7*sin(7/5 - 20*t) - 3/5*sin(13/9 - 19*t) - 6/5*sin(11/8 - 15*t) - 7/2*sin(13/9 - 14*t) - 49/6*sin(3/2 - 10*t) - 35/18*sin(20/13 - 9*t) - 19/3*sin(11/7 - 7*t) - 158/7*sin(14/9 - 4*t) - 334/11*sin(17/11 - 3*t) - 239/3*sin(11/7 - 2*t) + 254/7*sin(t + 11/7) + 11/4*sin(5*t + 17/10) + 8/5*sin(6*t + 12/7) + 17/7*sin(8*t + 12/7) + 12/5*sin(11*t + 8/5) + 16/17*sin(12*t + 15/8) + 22/15*sin(13*t + 13/8) + 1/56*sin(16*t + 2) + 1/2*sin(17*t + 12/7) + 5/11*sin(18*t + 9/5) + 5/6*sin(22*t + 9/5) + 1289/15)*step(39*math.pi - t)*step(t - 35*math.pi) + (-24/5*sin(1/6 - t) + 23/9*sin(2*t + 39/19) + 31/6*sin(3*t + 1/3) + 46/9*sin(4*t + 4/3) + 8/3*sin(5*t + 32/31) + 34/11*sin(6*t + 31/7) + 18/19*sin(7*t + 7/6) + 1/2*sin(8*t + 41/9) + 5/6*sin(9*t + 2/3) + 5/6*sin(10*t + 43/10) + 5/7*sin(11*t + 1/10) + 2/5*sin(12*t + 11/3) - 1346/7)*step(35*math.pi - t)*step(t - 31*math.pi) + (-2/5*sin(11/7 - 9*t) - 7/6*sin(23/15 - 6*t) - 61/7*sin(1/6 - t) + 4/9*sin(11*t) + 79/16*sin(2*t + 7/5) + 43/6*sin(3*t + 25/6) + 13/3*sin(4*t + 23/6) + sin(5*t + 12/7) + 3/7*sin(7*t + 26/9) + 19/20*sin(8*t + 45/11) + 3/8*sin(10*t + 25/7) + 1/5*sin(12*t + 79/20) + 3215/7)*step(31*math.pi - t)*step(t - 27*math.pi) + (205/4*sin(t + 11/8) - 967/5)*step(27*math.pi - t)*step(t - 23*math.pi) + (518/11*sin(t + 6/5) + 7073/15)*step(23*math.pi - t)*step(t - 19*math.pi) + (-1/10*sin(11/7 - 10*t) - 2/7*sin(14/9 - 4*t) + 402/5*sin(t + 3/2) + 3/8*sin(2*t + 30/7) + 25/3*sin(3*t + 13/9) + 62/21*sin(5*t + 11/8) + 2/9*sin(6*t + 38/9) + 17/11*sin(7*t + 11/9) + 1/12*sin(8*t + 101/25) + 8/9*sin(9*t + 9/8) + 4/7*sin(11*t + 17/16) + 1/7*sin(12*t + 13/3) + 2825/6)*step(19*math.pi - t)*step(t - 15*math.pi) + (507/5*sin(t + 11/7) + 10/11*sin(2*t + 25/6) + 65/6*sin(3*t + 5/3) + 5/9*sin(4*t + 11/3) + 23/6*sin(5*t + 17/10) + 2/5*sin(6*t + 19/5) + 15/8*sin(7*t + 7/4) + 1/3*sin(8*t + 7/2) + 8/7*sin(9*t + 9/5) + 1/6*sin(10*t + 16/5) + 6/7*sin(11*t + 7/4) + 1/6*sin(12*t + 17/5) - 1834/9)*step(15*math.pi - t)*step(t - 11*math.pi) + (-3/4*sin(3/5 - 11*t) + 547/4*sin(t + 11/7) + 14/3*sin(2*t + 23/7) + 41/10*sin(3*t + 23/10) + 25/4*sin(4*t + 14/5) + 13/7*sin(5*t + 69/34) + 29/8*sin(6*t + 26/11) + 13/8*sin(7*t + 20/13) + 11/10*sin(8*t + 13/7) + 4/5*sin(9*t + 4/7) + 3/7*sin(10*t + 21/11) + 3/5*sin(12*t + 25/6) + 251/3)*step(11*math.pi - t)*step(t - 7*math.pi) + (1524/7*sin(t + 20/13) + 61/11*sin(2*t + 59/15) + 22/3*sin(3*t + 9/4) + 41/7*sin(4*t + 25/6) + 5*sin(5*t + 11/6) + 51/10*sin(6*t + 19/5) + 3*sin(7*t + 12/7) + 53/13*sin(8*t + 22/7) + 29/9*sin(9*t + 11/7) + 12/7*sin(10*t + 38/15) + 16/5*sin(11*t + 13/12) + 7/11*sin(12*t + 9/7) + 484/7)*step(7*math.pi - t)*step(t - 3*math.pi) + (-9/4*sin(4/5 - 22*t) - 41/21*sin(7/6 - 21*t) - 16/5*sin(4/11 - 19*t) - 83/10*sin(8/15 - 10*t) + 7972/9*sin(t + 10/11) + 391/7*sin(2*t + 1/2) + 411/7*sin(3*t + 12/7) + 207/8*sin(4*t + 27/10) + 573/52*sin(5*t + 31/7) + 92/5*sin(6*t + 11/8) + 101/6*sin(7*t + 33/16) + 79/5*sin(8*t + 7/6) + 145/18*sin(9*t + 4/3) + 39/4*sin(11*t + 1/11) + 33/7*sin(12*t + 15/4) + 16/5*sin(13*t + 43/10) + 34/7*sin(14*t + 41/20) + 33/7*sin(15*t + 13/5) + 24/7*sin(16*t + 1/6) + 41/7*sin(17*t + 16/15) + 3/4*sin(18*t + 19/6) + 3/10*sin(20*t + 23/24) - 1013/10)*step(3*math.pi - t)*step(t + math.pi))*step(sqrt(sgn(sin(t/2))))

def y(t):
    return ((-3/10*sin(9/7 - 117*t) - 32/13*sin(1 - 98*t) - 7/4*sin(7/8 - 91*t) - 21/8*sin(16/11 - 84*t) - 29/6*sin(10/7 - 61*t) - 23/11*sin(9/8 - 55*t) - 269/7*sin(3/2 - 25*t) - 37/3*sin(11/7 - 19*t) - 113/5*sin(14/9 - 18*t) - 113/9*sin(3/2 - 10*t) - 163/54*sin(14/9 - 8*t) - 163/10*sin(11/7 - 6*t) - 2987/36*sin(11/7 - 2*t) + 254/5*sin(t + 11/7) + 310/7*sin(3*t + 11/7) + 297/7*sin(4*t + 33/7) + 47/3*sin(5*t + 14/9) + 19/2*sin(7*t + 33/7) + 43/8*sin(9*t + 17/11) + 28/9*sin(11*t + 21/5) + 25/3*sin(12*t + 9/2) + 81/7*sin(13*t + 14/3) + 82/7*sin(14*t + 14/3) + 120/7*sin(15*t + 32/7) + 147/11*sin(16*t + 32/7) + 27/2*sin(17*t + 14/3) + 25/3*sin(20*t + 13/3) + 193/11*sin(21*t + 23/5) + 128/7*sin(22*t + 50/11) + 87/10*sin(23*t + 16/7) + 175/11*sin(24*t + 31/7) + 241/8*sin(26*t + 6/5) + 1008/13*sin(27*t + 13/9) + 115/2*sin(28*t + 9/2) + 128*sin(29*t + 59/13) + 39/4*sin(30*t + 29/8) + 779/10*sin(31*t + 10/7) + 178/3*sin(32*t + 7/6) + 490/9*sin(33*t + 11/9) + 433/9*sin(34*t + 7/5) + 121/8*sin(35*t + 32/7) + 99/5*sin(36*t + 17/4) + 53/7*sin(37*t + 26/7) + 379/7*sin(38*t + 9/2) + 177/7*sin(39*t + 9/2) + 14/9*sin(40*t + 16/5) + 264/5*sin(41*t + 32/7) + 94/7*sin(42*t + 12/7) + 43/4*sin(43*t + 13/3) + 93/7*sin(44*t + 41/9) + 117/5*sin(45*t + 3/2) + 127/8*sin(46*t + 37/8) + 139/9*sin(47*t + 4/3) + 17/6*sin(48*t + 2/3) + 69/10*sin(49*t + 8/7) + 11/3*sin(50*t + 3/8) + 61/10*sin(51*t + 19/13) + 55/9*sin(52*t + 4/3) + 16/11*sin(53*t + 55/14) + 11/3*sin(54*t + 16/11) + 73/8*sin(56*t + 3/2) + 77/9*sin(57*t + 37/8) + 26/5*sin(58*t + 4) + 16/5*sin(59*t + 48/11) + 61/30*sin(60*t + 7/5) + 3/2*sin(62*t + 9/4) + 68/15*sin(63*t + 38/9) + 31/6*sin(64*t + 4) + 5/2*sin(65*t + 48/11) + 5/8*sin(66*t + 10/7) + 82/15*sin(67*t + 41/9) + 4/9*sin(68*t + 7/8) + 27/7*sin(69*t + 59/13) + 38/13*sin(70*t + 25/6) + 11/4*sin(71*t + 37/9) + 35/9*sin(72*t + 19/5) + 11/4*sin(73*t + 21/5) + 136/45*sin(74*t + 35/8) + 11/10*sin(75*t + 5/4) + 31/9*sin(76*t + 33/7) + 9/4*sin(77*t + 9/7) + 15/7*sin(78*t + 4/7) + 37/12*sin(79*t + 31/7) + 31/6*sin(80*t + 11/9) + 22/7*sin(81*t + 33/17) + 82/11*sin(82*t + 35/8) + 19/8*sin(83*t + 7/5) + 52/9*sin(85*t + 11/10) + 16/5*sin(86*t + 33/8) + 25/3*sin(87*t + 30/7) + 17/4*sin(88*t + 27/13) + 82/15*sin(89*t + 58/13) + 43/6*sin(90*t + 8/7) + 3/5*sin(92*t + 17/5) + 3*sin(93*t + 29/7) + 17/6*sin(94*t + 26/7) + 37/19*sin(95*t + 37/9) + 17/5*sin(96*t + 35/8) + 17/5*sin(97*t + 13/9) + 19/6*sin(99*t + 6/5) + 13/8*sin(100*t + 3/4) + 17/8*sin(101*t + 14/9) + 28/11*sin(102*t + 17/4) + 11/9*sin(103*t + 16/5) + 10/7*sin(104*t + 23/6) + 17/5*sin(105*t + 29/7) + sin(106*t + 11/6) + 3/10*sin(107*t + 7/6) + sin(108*t + 20/13) + 11/4*sin(109*t + 14/13) + 7/3*sin(110*t + 12/11) + 31/7*sin(111*t + 3/4) + 23/5*sin(112*t + 8/9) + sin(113*t + 1/2) + 9/5*sin(114*t + 6/7) + 5/8*sin(115*t + 3/2) + 7/6*sin(116*t + 47/46) + 9/7*sin(118*t + 13/6) + 9/7*sin(119*t + 30/7) + 23/6*sin(120*t + 73/18) + 4313/5)*step(155*math.pi - t)*step(t - 151*math.pi) + (-19/8*sin(11/7 - 4*t) - 32/5*sin(11/7 - 3*t) - 83/7*sin(11/7 - 2*t) - 697/10*sin(11/7 - t) - 21978/31)*step(151*math.pi - t)*step(t - 147*math.pi) + (-5/6*sin(11/7 - 4*t) - 57/10*sin(11/7 - 3*t) - 12/7*sin(11/7 - 2*t) - 532/9*sin(11/7 - t) - 12079/16)*step(147*math.pi - t)*step(t - 143*math.pi) + (-2/7*sin(7/5 - 49*t) - 7/8*sin(10/7 - 45*t) - 39/20*sin(3/2 - 43*t) - 40/11*sin(23/15 - 41*t) - 46/13*sin(17/11 - 39*t) - 81/20*sin(17/11 - 37*t) - 11/4*sin(3/2 - 35*t) - 11/8*sin(3/2 - 31*t) - 96/19*sin(14/9 - 26*t) - 41/7*sin(14/9 - 24*t) - 164/11*sin(11/7 - 8*t) - 541/6*sin(11/7 - 4*t) - 7791/10*sin(11/7 - 2*t) + 8001/25*sin(t + 11/7) + 565/6*sin(3*t + 33/7) + 782/27*sin(5*t + 33/7) + 279/5*sin(6*t + 33/7) + 41/4*sin(7*t + 8/5) + 109/6*sin(9*t + 33/7) + 4/5*sin(10*t + 48/11) + 63/4*sin(11*t + 33/7) + 51/8*sin(12*t + 37/8) + 115/11*sin(13*t + 47/10) + 16/3*sin(14*t + 14/3) + 47/10*sin(15*t + 8/5) + 53/10*sin(16*t + 33/7) + 13/5*sin(17*t + 5/3) + 23/3*sin(18*t + 47/10) + 7/6*sin(19*t + 32/7) + 23/11*sin(20*t + 33/7) + 4/3*sin(21*t + 59/13) + 8/7*sin(22*t + 14/3) + 35/8*sin(23*t + 8/5) + 29/8*sin(25*t + 13/8) + 12/5*sin(27*t + 11/7) + 1/6*sin(28*t + 12/7) + 17/7*sin(29*t + 47/10) + 20/9*sin(30*t + 13/8) + 3/2*sin(32*t + 13/8) + 13/6*sin(33*t + 33/7) + 4/11*sin(34*t + 8/5) + 37/10*sin(36*t + 8/5) + 23/7*sin(38*t + 13/8) + 21/5*sin(40*t + 8/5) + 23/10*sin(42*t + 13/8) + 17/11*sin(44*t + 8/5) + 1/9*sin(46*t + 37/11) + 13/10*sin(47*t + 14/3) + 7/5*sin(48*t + 8/5) + 5/7*sin(50*t + 8/5) + 7/8*sin(51*t + 14/3) + 2528/5)*step(143*math.pi - t)*step(t - 139*math.pi) + (-817/7*sin(11/7 - t) + 6/5*sin(2*t + 37/8) + 53/5*sin(3*t + 33/7) - 521/6)*step(139*math.pi - t)*step(t - 135*math.pi) + (-127/11*sin(11/7 - 2*t) + 44/3*sin(t + 11/7) + 206/5*sin(3*t + 11/7) + 84/5*sin(4*t + 11/7) - 3983/3)*step(135*math.pi - t)*step(t - 131*math.pi) + (-106/9*sin(11/7 - 3*t) - 287/9*sin(11/7 - t) + 7/6*sin(2*t + 8/5) + 29/7*sin(4*t + 11/7) - 8683/7)*step(131*math.pi - t)*step(t - 127*math.pi) + (1945/9*sin(t + 33/7) + 193/10*sin(2*t + 8/5) + 164/7*sin(3*t + 33/7) + 32/7*sin(4*t + 8/5) - 7269/7)*step(127*math.pi - t)*step(t - 123*math.pi) + (-295/42*sin(10/7 - 23*t) - 16/7*sin(9/7 - 22*t) - 31/8*sin(14/9 - 19*t) - 46/7*sin(10/7 - 17*t) - 21/4*sin(11/8 - 16*t) - 26/7*sin(10/7 - 15*t) - 14/5*sin(4/3 - 10*t) - 38/7*sin(4/3 - 9*t) - 131/5*sin(3/2 - 8*t) - 91/5*sin(3/2 - 7*t) - 43/8*sin(13/9 - 6*t) - 107/12*sin(14/9 - 4*t) - 41/5*sin(23/15 - 3*t) - 48/5*sin(3/2 - 2*t) - 935/8*sin(11/7 - t) + 7/6*sin(5*t + 7/5) + 1/2*sin(11*t + 2) + 33/7*sin(12*t + 19/11) + 5/4*sin(13*t + 21/5) + 50/7*sin(14*t + 8/5) + 10/9*sin(18*t + 7/6) + 1/30*sin(20*t + 19/5) + 35/12*sin(21*t + 17/11) + 1858/5)*step(123*math.pi - t)*step(t - 119*math.pi) + (-85/19*sin(11/7 - 23*t) - 27/8*sin(11/7 - 21*t) - 29/5*sin(14/9 - 19*t) - 15/7*sin(3/2 - 17*t) - sin(20/13 - 6*t) + 1973/10*sin(t + 11/7) + 71/8*sin(2*t + 20/13) + 119/5*sin(3*t + 11/7) + 38/37*sin(4*t + 13/10) + 77/13*sin(5*t + 14/9) + 91/15*sin(7*t + 11/7) + 10/9*sin(8*t + 7/5) + 14/3*sin(9*t + 11/7) + 55/6*sin(10*t + 14/3) + 77/6*sin(11*t + 14/3) + 47/10*sin(12*t + 32/7) + 123/7*sin(13*t + 47/10) + 107/5*sin(14*t + 33/7) + 55/3*sin(15*t + 8/5) + 28/5*sin(16*t + 14/9) + 11/6*sin(18*t + 14/9) + 64/13*sin(20*t + 13/8) + 22/15*sin(22*t + 13/8) + 8/9*sin(24*t + 5/3) - 2704/53)*step(119*math.pi - t)*step(t - 115*math.pi) + (-5/2*sin(14/9 - 31*t) - 136/27*sin(11/7 - 27*t) - 16/11*sin(10/7 - 23*t) - 4*sin(14/9 - 21*t) - 153/5*sin(11/7 - 8*t) - 43/5*sin(14/9 - 2*t) + 1369/8*sin(t + 11/7) + 1086/31*sin(3*t + 11/7) + 1/2*sin(4*t + 7/5) + 47/9*sin(5*t + 11/7) + 8*sin(6*t + 14/9) + 25/3*sin(7*t + 11/7) + 27/8*sin(9*t + 3/2) + 598/9*sin(10*t + 11/7) + 125/9*sin(11*t + 14/9) + 210/11*sin(12*t + 33/7) + 29/9*sin(13*t + 14/3) + 88/5*sin(14*t + 47/10) + 11/8*sin(15*t + 12/7) + 37/8*sin(16*t + 14/3) + 3/7*sin(17*t + 23/11) + 1/4*sin(18*t + 9/5) + 97/10*sin(19*t + 33/7) + 77/10*sin(20*t + 11/7) + 53/10*sin(22*t + 11/7) + 50/9*sin(24*t + 11/7) + 13/8*sin(25*t + 7/5) + 5/2*sin(26*t + 8/5) + 27/8*sin(28*t + 8/5) + 25/6*sin(29*t + 47/10) + 18/7*sin(30*t + 8/5) + 19/10*sin(32*t + 37/8) + 3417/10)*step(115*math.pi - t)*step(t - 111*math.pi) + (-223/14*sin(11/7 - 3*t) - 1303/9*sin(11/7 - t) + 1/3*sin(2*t + 24/23) + 1/6*sin(4*t + 5/8) - 1801/3)*step(111*math.pi - t)*step(t - 107*math.pi) + (82*sin(t + 11/7) + 37/6*sin(2*t + 11/7) + 8*sin(3*t + 11/7) + 3/5*sin(4*t + 11/7) + 13/4*sin(5*t + 11/7) - 13722/13)*step(107*math.pi - t)*step(t - 103*math.pi) + (215/3*sin(t + 11/7) + 112/5*sin(2*t + 11/7) + 29/4*sin(3*t + 11/7) - 11363/10)*step(103*math.pi - t)*step(t - 99*math.pi) + (-194/3*sin(11/7 - t) + 390/7*sin(2*t + 11/7) + 27/5*sin(3*t + 47/10) + 253/18*sin(4*t + 11/7) + 67/22*sin(5*t + 33/7) + 21/4*sin(6*t + 11/7) + 4/5*sin(7*t + 23/5) + 7/4*sin(8*t + 11/7) + 1/11*sin(9*t + 23/10) + 11/4*sin(10*t + 8/5) + 8/9*sin(11*t + 5/3) + 77/38*sin(12*t + 8/5) - 10118/9)*step(99*math.pi - t)*step(t - 95*math.pi) + (-35/9*sin(11/7 - 21*t) - 9/4*sin(11/7 - 18*t) - 21/5*sin(14/9 - 17*t) - 5/9*sin(22/15 - 16*t) - 52/5*sin(14/9 - 9*t) - 241/7*sin(11/7 - 5*t) - 185/3*sin(11/7 - 4*t) - 1791/14*sin(11/7 - 2*t) + 707/8*sin(t + 11/7) + 39/11*sin(3*t + 3/2) + 1592/27*sin(6*t + 11/7) + 51/2*sin(7*t + 8/5) + 20/7*sin(8*t + 8/5) + 67/4*sin(10*t + 8/5) + 9/5*sin(11*t + 23/5) + 83/15*sin(12*t + 8/5) + 27/5*sin(13*t + 11/7) + 23/4*sin(14*t + 8/5) + 1/5*sin(15*t + 43/10) + 18/7*sin(19*t + 11/7) + 6/5*sin(20*t + 3/2) - 1589/10)*step(95*math.pi - t)*step(t - 91*math.pi) + (-4/3*sin(3/2 - 17*t) - 29/28*sin(14/9 - 15*t) - 11/9*sin(19/13 - 14*t) - 19/8*sin(11/7 - 13*t) - 26/9*sin(14/9 - 11*t) - 25/8*sin(3/2 - 10*t) - 3*sin(14/9 - 9*t) - 8/15*sin(11/8 - 8*t) - 101/10*sin(14/9 - 7*t) - 3/8*sin(10/7 - 4*t) - 345/13*sin(11/7 - 3*t) + 433/11*sin(t + 11/7) + 914/9*sin(2*t + 11/7) + 17/10*sin(5*t + 13/8) + 5/6*sin(6*t + 11/7) + 3/4*sin(12*t + 17/11) + 1/13*sin(16*t + 8/7) - 7481/17)*step(91*math.pi - t)*step(t - 87*math.pi) + (-25/6*sin(11/7 - t) + 125/6*sin(2*t + 11/7) + 50)*step(87*math.pi - t)*step(t - 83*math.pi) + (-1/35*sin(11/8 - 12*t) - 49/11*sin(11/7 - 5*t) - 3/5*sin(17/11 - 4*t) - 247/9*sin(11/7 - t) + 92/7*sin(2*t + 11/7) + 1/3*sin(3*t + 23/5) + 97/7*sin(6*t + 8/5) + 27/5*sin(7*t + 8/5) + 29/9*sin(8*t + 8/5) + 5/6*sin(9*t + 5/3) + 4/5*sin(10*t + 13/8) + 37/12*sin(11*t + 8/5) + 5/3)*step(83*math.pi - t)*step(t - 79*math.pi) + (-2/7*sin(11/7 - 11*t) - 3/4*sin(11/7 - 10*t) - 1/49*sin(6/5 - 9*t) - 7/4*sin(11/7 - 8*t) - 5/6*sin(11/7 - 7*t) - 54/7*sin(11/7 - 4*t) - 77/3*sin(11/7 - 2*t) - 260/9*sin(11/7 - t) + 1/5*sin(3*t + 5/3) + 17/11*sin(5*t + 33/7) + 19/6*sin(6*t + 33/7) + 3/10*sin(12*t + 33/7) + 2395/21)*step(79*math.pi - t)*step(t - 75*math.pi) + (-4/5*sin(4/3 - 29*t) - 5/8*sin(1/5 - 27*t) - 9/8*sin(1/14 - 24*t) - 3/7*sin(17/11 - 23*t) - 12/7*sin(1/2 - 18*t) - 13/8*sin(2/9 - 17*t) - 19/6*sin(26/27 - 9*t) - 13/4*sin(1 - 8*t) + 3/10*sin(16*t) + 45/2*sin(t + 23/5) + 242/3*sin(2*t + 13/8) + 87/8*sin(3*t + 18/7) + 410/7*sin(4*t + 12/7) + 33/5*sin(5*t + 95/24) + 199/7*sin(6*t + 13/7) + 183/23*sin(7*t + 11/5) + 13/14*sin(10*t + 5/4) + 17/7*sin(11*t + 16/5) + 7*sin(12*t + 45/23) + 11/3*sin(13*t + 14/3) + 34/5*sin(14*t + 13/6) + 41/9*sin(15*t + 17/6) + 7/6*sin(19*t + 46/15) + 25/9*sin(20*t + 13/5) + 9/8*sin(21*t + 32/7) + 13/8*sin(22*t + 12/5) + 19/9*sin(25*t + 46/15) + 21/22*sin(26*t + 7/2) + 4/5*sin(28*t + 28/11) + 4/5*sin(30*t + 10/7) - 1836/7)*step(75*math.pi - t)*step(t - 71*math.pi) + (-7/2*sin(11/7 - 5*t) - 66/7*sin(11/7 - 3*t) - 67*sin(11/7 - t) + 40/11*sin(2*t + 11/7) + 1/5*sin(4*t + 5/3) - 1334/3)*step(71*math.pi - t)*step(t - 67*math.pi) + (-31/5*sin(11/7 - 3*t) + 142/9*sin(t + 11/7) + 732/5*sin(2*t + 11/7) + 8/7*sin(4*t + 11/7) + 24/7*sin(5*t + 11/7) + 66/5*sin(6*t + 11/7) + 3/2*sin(7*t + 33/7) + 17/5*sin(8*t + 11/7) + 4/5*sin(9*t + 8/5) + 32/9*sin(10*t + 11/7) + 14/13*sin(11*t + 33/7) - 551)*step(67*math.pi - t)*step(t - 63*math.pi) + (-29/8*sin(3/2 - 12*t) - 19/4*sin(19/13 - 10*t) - 35/4*sin(3/2 - 9*t) - 1/3*sin(2/5 - 8*t) - 31/2*sin(17/11 - 6*t) - 121/7*sin(14/9 - 4*t) - 132/19*sin(20/13 - 2*t) - 306/7*sin(11/7 - t) + 9/8*sin(3*t + 9/7) + 4*sin(5*t + 10/7) + 90/13*sin(7*t + 14/9) + 49/11*sin(11*t + 11/7) + 1187/8)*step(63*math.pi - t)*step(t - 59*math.pi) + (-16/7*sin(14/9 - 6*t) - 97/13*sin(11/7 - 5*t) - 596/17*sin(11/7 - 3*t) - 64*sin(11/7 - t) + 146/5*sin(2*t + 11/7) + 43/10*sin(4*t + 11/7) + 1837/8)*step(59*math.pi - t)*step(t - 55*math.pi) + (-49/10*sin(11/7 - 3*t) - 548/7*sin(11/7 - t) + 109/10*sin(2*t + 11/7) + 51/13*sin(4*t + 11/7) + 11/12*sin(5*t + 47/10) + 1439/5)*step(55*math.pi - t)*step(t - 51*math.pi) + (-55/27*sin(11/7 - 38*t) - 54/11*sin(3/2 - 26*t) - 19/18*sin(4/3 - 19*t) - 37/4*sin(20/13 - 17*t) + 387/8*sin(t + 33/7) + 68/9*sin(2*t + 47/10) + 27/4*sin(3*t + 33/7) + 41/21*sin(4*t + 47/10) + 16/15*sin(5*t + 11/7) + 37/11*sin(6*t + 11/7) + 13/5*sin(7*t + 20/13) + 46/7*sin(8*t + 11/7) + 69/14*sin(9*t + 23/15) + 75/7*sin(10*t + 14/9) + 113/11*sin(11*t + 14/9) + 3/8*sin(12*t + 5/9) + 93/11*sin(13*t + 11/7) + 5/7*sin(14*t + 4/3) + 21/10*sin(15*t + 19/13) + 86/9*sin(16*t + 11/7) + 222/17*sin(18*t + 11/7) + 1/5*sin(20*t + 17/9) + 17/6*sin(21*t + 13/8) + 58/5*sin(22*t + 33/7) + 23/7*sin(23*t + 14/3) + 31/7*sin(24*t + 20/13) + 85/9*sin(25*t + 11/7) + 45/13*sin(27*t + 8/5) + 3/8*sin(28*t + 10/11) + 14/5*sin(29*t + 8/5) + 4*sin(30*t + 33/7) + 1/3*sin(31*t + 13/6) + 15/7*sin(32*t + 14/3) + 55/28*sin(33*t + 23/5) + 5/2*sin(34*t + 37/8) + 3/4*sin(35*t + 31/7) + 9/7*sin(36*t + 14/3) + sin(37*t + 5/3) + 2239/9)*step(51*math.pi - t)*step(t - 47*math.pi) + (-7/5*sin(22/15 - 37*t) - 13/9*sin(10/7 - 31*t) - 15/8*sin(22/15 - 30*t) - 37/10*sin(3/2 - 29*t) - 45/13*sin(10/7 - 28*t) - 19/7*sin(13/9 - 27*t) - 14/11*sin(11/8 - 26*t) - 68/15*sin(16/11 - 25*t) - 17/4*sin(22/15 - 24*t) - 103/13*sin(3/2 - 23*t) - 97/13*sin(3/2 - 22*t) - 13/5*sin(23/15 - 18*t) - 27/8*sin(20/13 - 15*t) - 13/3*sin(17/11 - 14*t) - 9/8*sin(3/2 - 13*t) - 27/28*sin(3/2 - 12*t) - 59/9*sin(14/9 - 8*t) - 12/7*sin(3/2 - 7*t) - 53/5*sin(11/7 - 4*t) - 269/7*sin(11/7 - 2*t) + 198/5*sin(t + 11/7) + 79/6*sin(3*t + 11/7) + 11/8*sin(5*t + 3/2) + 16/9*sin(6*t + 8/5) + 43/9*sin(9*t + 8/5) + 32/9*sin(10*t + 8/5) + 74/25*sin(11*t + 8/5) + 16/9*sin(16*t + 18/11) + 3/2*sin(17*t + 5/3) + 23/8*sin(19*t + 8/5) + 109/11*sin(20*t + 13/8) + 12/7*sin(21*t + 8/5) + 1/8*sin(32*t + 7/8) + 24/23*sin(33*t + 5/3) + 5/9*sin(34*t + 8/5) + 1/4*sin(35*t + 41/9) + 3/5*sin(36*t + 12/7) + 1199/4)*step(47*math.pi - t)*step(t - 43*math.pi) + (-1/10*sin(10/7 - 28*t) - 15/14*sin(14/9 - 21*t) - 7/3*sin(17/11 - 18*t) - 7/4*sin(20/13 - 12*t) - 114/7*sin(11/7 - 9*t) + 95/6*sin(t + 33/7) + 7/8*sin(2*t + 47/10) + 13/6*sin(3*t + 14/9) + 52/7*sin(4*t + 11/7) + 48/7*sin(5*t + 11/7) + 72/7*sin(6*t + 11/7) + 33/17*sin(7*t + 14/9) + 17/3*sin(8*t + 8/5) + 52/7*sin(10*t + 11/7) + 58/9*sin(11*t + 11/7) + 3/5*sin(13*t + 14/3) + 7/11*sin(14*t + 14/3) + 19/13*sin(15*t + 14/9) + 1/4*sin(16*t + 3/2) + 5/3*sin(17*t + 8/5) + 19/13*sin(19*t + 11/7) + 12/7*sin(20*t + 11/7) + 1/9*sin(22*t + 8/5) + 3/11*sin(23*t + 14/9) + 3/8*sin(24*t + 17/11) + 1/6*sin(25*t + 10/7) + 4/11*sin(26*t + 8/5) + 1/12*sin(27*t + 4/3) + 2/5*sin(29*t + 11/7) + 1/12*sin(30*t + 15/11) - 4015/6)*step(43*math.pi - t)*step(t - 39*math.pi) + (-19/8*sin(10/7 - 21*t) - 29/8*sin(3/2 - 17*t) - 69/35*sin(7/5 - 16*t) - 1/8*sin(1 - 15*t) - 35/6*sin(3/2 - 11*t) - 53/10*sin(23/15 - 10*t) - 28/5*sin(11/7 - 8*t) - 8/3*sin(3/2 - 7*t) - 97/7*sin(14/9 - 5*t) - 104/19*sin(23/15 - 4*t) + 124/7*sin(t + 11/7) + 43/2*sin(2*t + 8/5) + 17/4*sin(3*t + 8/5) + 11/9*sin(6*t + 11/7) + 9*sin(9*t + 13/8) + 3/8*sin(12*t + 23/15) + 12/7*sin(13*t + 16/9) + 4/7*sin(14*t + 23/5) + 49/10*sin(18*t + 5/3) + 33/16*sin(19*t + 47/10) + 2/9*sin(20*t + 1/14) + 8/5*sin(22*t + 12/7) - 3479/6)*step(39*math.pi - t)*step(t - 35*math.pi) + (-3/7*sin(6/11 - 10*t) - 5/8*sin(1/11 - 8*t) + 1/12*sin(12*t) + 67/33*sin(t + 18/11) + 37/10*sin(2*t + 39/11) + 17/11*sin(3*t + 16/9) + 43/9*sin(4*t + 28/9) + 11/5*sin(5*t + 20/7) + 23/8*sin(6*t + 1/7) + 7/8*sin(7*t + 79/20) + 4/11*sin(9*t + 16/11) + 4/11*sin(11*t + 5/2) + 1216/7)*step(35*math.pi - t)*step(t - 31*math.pi) + (-2/9*sin(17/16 - 12*t) - 3/7*sin(17/11 - 10*t) - 2/7*sin(3/5 - 8*t) - 6/5*sin(4/5 - 6*t) - 30/7*sin(5/7 - 4*t) - 25/4*sin(2/7 - 3*t) + 7/2*sin(t + 7/4) + 26/5*sin(2*t + 52/15) + 4/5*sin(5*t + 27/10) + 2/3*sin(7*t + 29/11) + 4/7*sin(9*t + 13/6) + 2/7*sin(11*t + 5/2) + 454/5)*step(31*math.pi - t)*step(t - 27*math.pi) + (2099/12 - 266/13*sin(1/3 - t))*step(27*math.pi - t)*step(t - 23*math.pi) + (761/9 - 178/7*sin(6/11 - t))*step(23*math.pi - t)*step(t - 19*math.pi) + (-1/2*sin(3/8 - 11*t) - 5/9*sin(1/6 - 9*t) - 5/8*sin(1/5 - 7*t) - 3*sin(3/7 - 3*t) - 319/13*sin(2/7 - t) + 5/6*sin(2*t + 55/18) + 2/7*sin(4*t + 33/10) + 4/3*sin(5*t + 1/5) + 7/8*sin(6*t + 29/8) + 4/7*sin(8*t + 20/7) + 1/6*sin(10*t + 22/5) + 1/3*sin(12*t + 34/9) + 337/4)*step(19*math.pi - t)*step(t - 15*math.pi) + (-1/16*sin(5/7 - 12*t) - 1/13*sin(9/7 - 10*t) - 1/3*sin(4/9 - 9*t) - 10/9*sin(1/9 - 7*t) - 6/5*sin(1/2 - 5*t) - 185/9*sin(4/9 - t) + 114/23*sin(2*t + 43/10) + 9/7*sin(3*t + 14/3) + 19/8*sin(4*t + 13/3) + 3/2*sin(6*t + 32/7) + 2/3*sin(8*t + 63/16) + 7/13*sin(11*t + 3/10) + 4419/26)*step(15*math.pi - t)*step(t - 11*math.pi) + (-65/11*sin(7/9 - 5*t) + 496/5*sin(t + 49/16) + 95/8*sin(2*t + 15/14) + 69/10*sin(3*t + 3) + 57/14*sin(4*t + 31/7) + 11/12*sin(6*t + 37/8) + 16/15*sin(7*t + 23/10) + 5/6*sin(8*t + 32/9) + 2/3*sin(9*t + 19/7) + 11/7*sin(10*t + 70/23) + 8/9*sin(11*t + 40/9) + 1/5*sin(12*t + 23/7) - 608)*step(11*math.pi - t)*step(t - 7*math.pi) + (-2/3*sin(41/40 - 10*t) - 15/8*sin(10/7 - 9*t) - 5*sin(4/3 - 5*t) - 69/8*sin(5/7 - 3*t) + 727/4*sin(t + 94/31) + 23/8*sin(2*t + 22/9) + 38/7*sin(4*t + 40/11) + 7/3*sin(6*t + 13/10) + 16/17*sin(7*t + 30/7) + 9/7*sin(8*t + 46/15) + sin(11*t + 37/9) + 11/9*sin(12*t + 9/4) - 5780/9)*step(7*math.pi - t)*step(t - 3*math.pi) + (-137/7*sin(16/15 - 7*t) - 180/7*sin(8/7 - 4*t) + 2590/3*sin(t + 23/9) + 2399/15*sin(2*t + 1) + 207/2*sin(3*t + 27/7) + 515/7*sin(5*t + 11/7) + 894/19*sin(6*t + 10/3) + 67/2*sin(8*t + 19/20) + 32/11*sin(9*t + 48/11) + 68/7*sin(10*t + 1/6) + 125/9*sin(11*t + 4/3) + 35/3*sin(12*t + 71/18) + 44/7*sin(13*t + 68/15) + 4/3*sin(14*t + 19/7) + 45/7*sin(15*t + 10/3) + 32/7*sin(16*t + 26/9) + 31/6*sin(17*t + 7/8) + 16/3*sin(18*t + 25/24) + 24/7*sin(19*t + 5/4) + 7/3*sin(20*t + 1/9) + 41/20*sin(21*t + 14/3) + 39/7*sin(22*t + 161/40) - 3017/9)*step(3*math.pi - t)*step(t + math.pi))*step(sqrt(sgn(sin(t/2))))

def dist(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

pi_count = 156
div_const = 4
steps_per_pi = 50


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