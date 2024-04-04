#extrating colors
"""import colorgram
rgb=[]
colours = colorgram.extract('photo.jpg', 30)
for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb.append(new_color)

print(rgb)
""" ''''''

import turtle as t
import random


t.colormode(255)
tim= t.Turtle()
colorz=[(149, 79, 102), (161, 151, 148), (176, 164, 169), (163, 104, 130), (133, 87, 83), (10, 13, 24), (118, 35, 51), (162, 163, 168), (154, 108, 105), (62, 25, 23), (88, 94, 105), (106, 42, 39), (162, 166, 165) , (56, 61, 77), (131, 128, 121), (123, 125, 137), (88, 92, 90), (117, 131, 135), (64, 64, 61), (51, 68, 73), (15, 19, 18), (201, 186, 193), (119, 131, 129)]

tim.speed("fastest")
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(350)
tim.setheading(0)
tim.backward(50)




def colorex():
    for i in range (13):
        tim.dot(20,random.choice(colorz))
        tim.penup()
        tim.forward(50)
        tim.pendown()


for i in range (11):
    colorex()
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(650)
    tim.setheading(0)

screen =t.Screen()
screen.exitonclick()