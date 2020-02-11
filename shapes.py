import turtle
import math

# Create the world, and a turtle to put in it
# bob = turtle.Turtle()

# Get moving, turtle!
# bob.fd(100)

# Wait for the user to close the window
# turtle.mainloop()

#------------------------------------------------------------------------------
# Make some shapes
#   Work through exercises 1-4 in Chapter 4.3.
#------------------------------------------------------------------------------

def square(t, l):
    """
    Draw a square with side length l using Turtle t

    >>> don = turtle.Turtle()
    >>> square(don, 100)
    """
    for i in range(4):
        t.fd(l)
        t.lt(90)

    turtle.mainloop()

def polygon(t, l, n):
    """
    Draw an n-sided polygon with side length l using Turtle t

    >>> don = turtle.Turtle()
    >>> polygon(don, 100, 6)
    """
    for i in range(n):
        t.fd(l)
        t.lt(360/n)

    turtle.mainloop()

def circle(t, r):
    """
    Draw an approximate circle with radius r using Turtle t

    >>> don = turtle.Turtle()
    >>> circle(don, 50)
    """
    circumference = 2 * math.pi * r
    n = 50
    l = circumference / n
    polygon(t, l, n)

#------------------------------------------------------------------------------
# Make some art
#   Complete *at least one of* Exercise 2, 3, 4, or 5 in `shapes.py`.
#------------------------------------------------------------------------------

# Exercise 3

def pie(t, r, num_segments):
    """
    Draw a pie given a number of pie segments

    t: Turtle
    r: radius
    num_segments: number of pie segments
    """
    angle = 180-(180-(360/num_segments))/2

    for i in range(num_segments):
        t.fd(r)
        t.lt(angle)

    turtle.mainloop()

    # i tried my best and spent many hours on this assignment but could not figure it out... might try again later

if __name__ == "__main__":

    bob = turtle.Turtle()
    # square(bob, 200)
    # polygon(bob, 100, 6)
    # circle(bob, 50)
    pie(bob, 100, 5)
