#many_squares


import turtle
def draw_square (t, sz):
    for i in range (4):
        t.forward(sz)
        t.right(90)

wn = turtle.Screen() 
wn.bgcolor("black")

tess = turtle.Turtle()
tess.color("white")
tess.pensize(3)
tess.speed(20)

size = 20
for i in range (5):
    tess.pendown()
    size = size + 20
    draw_square(tess, size)
    tess.penup()
    tess.right(180)
    tess.forward(10)
    tess.right(90)
    tess.forward(10)
    tess.right(90)
