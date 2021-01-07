#rosace



import turtle
def draw_square (t, sz):
    for i in range (4):
        t.forward(sz)
        t.right(90)

wn = turtle.Screen() 
wn.bgcolor("black")

tess = turtle.Turtle()
tess.color("white")
tess.pensize(2)
tess.speed(20)

size = 20
for i in range (20):
    draw_square(tess, 100)
    tess.right(18)

wn.mainloop

