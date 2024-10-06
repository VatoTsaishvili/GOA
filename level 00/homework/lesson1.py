from turtle import *


#we want to paint a house

#step 1: draw a square

speed(50)
width(7)
color("cyan")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(90)     #height of the door
right(90)
forward(60)
right(90)
forward(90)
end_fill()

penup()
goto(200, 200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("black")
right(180)
forward(200)
right(120)
forward(200)
left(180)
forward(200)
right(120)

color("red")
begin_fill()
forward(250)
right(60)
forward(200)
right(120)
forward(250)
end_fill()

color("cyan")
begin_fill()
right(180)
forward(250)
right(90)
forward(200)
right(90)
forward(250)
end_fill()

color("black")
right(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(450)
left(90)
forward(200)
left(30)
forward(200)
left(60)
forward(250)
left(120)
forward(200)
left(60)
forward(250)

penup()
goto(170, 170)
pendown()

color("black")
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
left(180)
forward(25)
left(90)
forward(40)
left(180)
forward(20)
left(90)
forward(20)
right(180)
forward(50)

penup()
goto(25, 170)
pendown()

color("black")
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
left(180)
forward(20)
left(90)
forward(50)
right(180)
forward(25)
right(90)
forward(20)
right(180)
forward(40)

penup()



exitonclick()