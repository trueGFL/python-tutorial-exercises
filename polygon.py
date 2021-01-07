#polygon


import turtle
def draw_poly (t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.right(360/n)

wn = turtle.Screen()
wn.bgcolor("black")

tess = turtle.Turtle()
tess.color("white")
tess.pensize(3)
tess.speed(20)

nb = input("Nb de faces ?")
n = int(nb)
size = input("Longueur des faces ?")
sz = int(size)



for i in range(n):
    tess.forward(sz)
    tess.right(360/n)

wn.mainloop
