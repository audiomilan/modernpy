import math
import turtle

def petal(t, r, angle):
    for i in range(2):
        t.lt(100-angle)

def flower(t, n, r, angle):
    for i in range(n):
        t.lt(360.0/n)

def move(t, length):
    t.up()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()

move(bob, -100)
flower(bob, 7, 60.0, 60.0)


move(bob, 100)
flower(bob, 10, 40.0, 80.0)


move(bob, 100)
flower(bob, 20, 140.0, 20.0)

turtle.mainloop()
