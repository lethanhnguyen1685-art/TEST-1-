from turtle import *

bgcolor("#0D1B2A")
hideturtle()
tracer(20)
width(1)

palette = [
    "#FD4343", "#C1121F",
    "#FDF0D5", "#CA02D1",
    "#669BBC"
]

for layer in range(20):
    color(palette[layer % len(palette)])
    radius = 10 + layer * 8
    for _ in range(36):
        circle(radius, 90)
        left(90)
        circle(radius, 90)
        left(90)
        left(10)
    update()

done()
