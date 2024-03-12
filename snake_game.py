from turtle import Turtle, Screen
import time
import random

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in POSITION:
            self.add_Segment(i)

    def extend(self):
        self.add_Segment(self.segment[-1].position())


    def add_Segment(self, i):
        turt = Turtle("square")
        turt.color("white")
        turt.penup()
        turt.goto(i)
        self.segment.append(turt)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            last_pos_x = self.segment[seg - 1].xcor()
            last_pos_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(last_pos_x, last_pos_y)
        self.head.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turnright(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turnleft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 290)
        self.score = 0
        self.color("white")
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.write(f"score : {self.score} ", align="center", font=("Arial", 24, "normal"))
    def inc_score(self):
        self.score+=1
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.hideturtle()

        self.write("game over ", align="center", font=("Arial", 24, "normal"))


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomx = random.randint(a=-280, b=280)
        randomy = random.randint(a=-280, b=280)
        self.goto(randomx, randomy)


food = Food()
screen = Screen()

screen.title("snake game")
screen.screensize(canvwidth=300, canvheight=300, bg="black")

screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.turnright, "d")
screen.onkey(snake.turnleft, "a")
scoreboard = Scoreboard()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.inc_score()
        snake.extend()
    if snake.head.xcor() > 375 or snake.head.ycor() > 300 or snake.head.xcor() < -375 or snake.head.ycor() < -300:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:

        if snake.head.distance(segment) < 5 :
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
