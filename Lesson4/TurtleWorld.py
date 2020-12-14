import turtle
bob = turtle.Turtle()
alice = turtle.Turtle()
print(bob)
print(alice)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def square (a, length):
    for m in range(4):
        a.fd(length)
        a.lt(100)


square(bob, 100)
square(alice, 500)
turtle.mainloop()

# Modify the body so length  of the sides is length




# Write a function 'call' that passes bob to the function

