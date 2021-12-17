import turtle
import math
import random
Tr=turtle.Screen()
Tr.bgcolor('black')
Al=turtle.Turtle()
Al.speed(0)
Al.color('white')
rotate=int(360)
def Circles(n,size):
    for i in range(10):
        n.circle(size)
        size=size-4
def Special(n,size,repeat):
    for i in range(repeat):
        Circles(n,size)
        n.right(360/repeat)
Special(Al,100,10)
St=turtle.Turtle()
St.speed(0)
St.color('yellow')
rotate=int(90)
def Circles(n,size):
    for i in range(4):
        n.circle(size)
        size=size-10
def Special(n,size,repeat):
    for i in range(repeat):
        Circles(n,size)
        n.right(360/repeat)
Special(St,100,10)
Br=turtle.Turtle()
Br.speed(0)
Br.color('blue')
rotate=int(80)
def Circles(n,size):
    for i in range(4):
        n.circle(size)
        size=size-5
def Special(n,size,repeat):
    for i in range(repeat):
        Circles(n,size)
        n.right(360/repeat)
Special(Br,100,10)
Ter=turtle.Turtle()
Ter.speed(0)
Ter.color('orange')
rotate=int(90)
def Circles(n,size):
    for i in range(4):
        n.circle(size)
        size=size-19
def Special(n,size,repeat):
    for i in range(repeat):
        Circles(n,size)
        n.right(360/repeat)
Special(Ter,100,10)
Wl=turtle.Turtle()
Wl.speed(0)
Wl.color('pink')
rotate=int(90)
def Circles(n,size):
    for i in range(4):
        n.circle(size)
        size=size-20
def Special(n,size,repeat):
    for i in range(repeat):
        Circles(n,size)
        n.right(360/repeat)
Special(Wl,100,10)
turtle.getscreen()._root.mainloop()
