#mecbourré

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
drunkenpath = [160, -43, 270, -97, -43, 200, -940, 17, -86]
finaldir = 0
direction = 0

for f in drunkenpath :
    tess.forward(100)
    tess.right(f)
    finaldir = finaldir + f

direction = finaldir % 360
print("Le mec bourré se dirige selon un angle de", direction, "degrés.")
wn.mainloop()
