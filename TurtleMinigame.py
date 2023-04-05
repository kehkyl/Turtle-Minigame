from turtle import *

move_dist = 20
speed(0)

bgcolor("#D2691E")
penup()
goto(100, 200)
pendown()
color("blue")
begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

penup()
goto(-200, 0)
color("green")
shape("turtle")

def check_goal ():
  if xcor() > 100:
    hideturtle()
    color("White")
    write("YOU WIN")
    onkey(None,"Up")
    onkey(None, "Down")
    onkey(None, "Left")
    onkey(None, "Right")

def move_up():
  setheading(90)
  forward(move_dist)
  check_goal()

def move_left():
  setheading(180)
  forward(move_dist)
  check_goal()

def move_down():
  setheading(270)
  forward(move_dist)
  check_goal()

def move_right():
  setheading(0)
  forward(move_dist)
  check_goal()


  
#move keys
onkey(move_up,"Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()
