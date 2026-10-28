import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numsides=8
sidelength=20
angle=360.0/numsides
for i in range(numsides):
    polygon.forward(sidelength)
    polygon.right(angle)


turtle.done()
























































