from turtle import Turtle , Screen
from random import randint
from random import random
#import colorgram


tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red")
tim.pencolor("black")

"""
#square
for x in range(4):
    tim.forward(100)
    tim.right(90)

"""
"""
#dashed line
for x in range(15):    
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
"""

"""
#Drawing different shapes
num_sides = 3
while num_sides < 10 :
    angle = 360 / num_sides
    for x in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        #tup = (randint(0,1), randint(0,1), randint(0,1))


    tup = (random(), random(), random())
    tim.pencolor(tup)
    num_sides += 1
"""

"""
#Drawing different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for x in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,11):
    draw_shape(shape_side_n)
    tup = (random(), random(), random())
    tim.pencolor(tup)

"""



#Generate a Random Walk
"""


def random_color():
    r = randint(0,255)
    g = randint(0, 255)    
    b = randint(0, 255)
    random_color = (r,g,b)
    return random_color

tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    x = randint(1, 4)

    if(x == 2):
        tim.right(90)
    if(x == 3):
        tim.left(90)
    if(x == 4):
        tim.right(90)
        tim.right(90)

    tim.forward(30)
    #tim.pensize(i * 2)
    tup = (random(), random(), random())
    tim.pencolor(tup)

"""


"""
#draw a spirograph
def random_color():
    r = random()
    g = random()
    b = random()
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap) ):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 5)



tim.speed("fastest")
draw_spirograph(5)
"""








screen.exitonclick()

