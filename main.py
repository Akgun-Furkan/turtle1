import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen().bgcolor("black")
t.speed(1000)
n=70
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(1)
        t.circle(100)
