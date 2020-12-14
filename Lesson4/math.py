import turtle
import math
bob = turtle.Turtle()
print(bob)

def polygon(a, b, c):
    ...

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)



circle(bob, 100)
turtle.mainloop()
