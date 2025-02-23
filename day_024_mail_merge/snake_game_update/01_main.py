from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Make head
snake_head = Turtle("square")
snake_head.color("white")
snake_head.penup()
# Create first body
snake_body = Turtle("square")
snake_body.color("white")
snake_body.penup()
snake_body.setx(snake_head.pos()[0] - 20)
# Create tail
snake_tail = Turtle("square")
snake_tail.color("white")
snake_tail.penup()
snake_tail.setx(snake_body.pos()[0] - 20)

screen.exitonclick()
