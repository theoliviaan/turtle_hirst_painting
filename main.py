
import turtle as t
import colorgram
import random
#
colors = colorgram.extract('image.jpeg', 15)
tim = t.Turtle()

t.colormode(255)
# new_list = []

# for i in range(10)
#     first_color = colors[i]
#     rgb = first_color.rgb
#     new_list.append(rgb)
# print(new_list)

# extract the colours
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     new_list.append(new_colour)
# print(new_list)

color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162), (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36)]

tim.speed("fastest")
tim.hideturtle()
tim.penup()

# make the turtle start from down
tim.goto(-300, -200)

# put the pen back down
tim.pendown()


def a_line():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)


def go_back():
    for _ in range(10):
        tim.forward(50)


for _ in range(10):
    a_line()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    go_back()
    tim.right(180)


screen = t.Screen()
screen.exitonclick()

