from turtle import Turtle

CORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for cord in CORDS:
            self.add_segment(cord)

    def extend(self):
        self.add_segment((self.segments[-1].xcor() - 20, self.segments[-1].ycor()))

    def add_segment(self, position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            self.segments[n].goto(self.segments[n - 1].xcor(), self.segments[n - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)