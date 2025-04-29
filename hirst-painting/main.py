import colorgram
import turtle as turtle_module
import random

"""

colors = colorgram.extract('image.jpg', 30)
rgb_colors = []
for color in colors:
    #rgb_colors.append(color)
    r = color.rgb.r
    g = color.rgb.g
    b  = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
"""

turtle_module.colormode(255)

screen = turtle_module.Screen()
tim = turtle_module.Turtle()
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

number_of_dots = 50
i = 0
for x in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    i += 1
    tim.forward(50)
    if i == 5:
        tim.setheading(180)
        tim.forward(250)
        tim.setheading(90)
        tim.forward(50)
        i = 0
        tim.setheading(0)


screen.exitonclick()



