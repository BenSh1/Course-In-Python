from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x, new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(new_x, new_y)



