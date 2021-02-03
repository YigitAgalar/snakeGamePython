from turtle import Turtle


class Snake:

    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

# adding segment to snake
    def add_segment(self,position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
# creating snake
    def create_snake(self):
        for positions in self.starting_positions:
            self.add_segment(positions)


# moving snake forward

    def moving(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
# directions

    def turn_right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)

    def go_up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)

    def turn_left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)

    def go_down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)