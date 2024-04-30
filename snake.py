from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.spawn()
        self.head = self.segments[0]

    def spawn(self):
        for num in range(3):
            seg = Turtle(shape="square")
            seg.penup()
            seg.speed("fastest")
            seg.color("white")
            self.segments.append(seg)

    def grow(self):
        seg0 = Turtle(shape="square")
        seg0.penup()
        seg0.speed("fastest")
        seg0.goto(340, 340)
        self.segments.append(seg0)
        self.segments[len(self.segments) - 1].color("white")

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            nex_x = self.segments[n - 1].xcor()
            nex_y = self.segments[n - 1].ycor()
            self.segments[n].goto(nex_x, nex_y)
        self.head.forward(20)

    def restart(self):
        for seg in self.segments:
            seg.goto(340, 340)
        self.segments.clear()
        self.spawn()
        self.head = self.segments[0]

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
