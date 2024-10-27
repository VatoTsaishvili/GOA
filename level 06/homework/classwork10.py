#10) ნებისმიერ საკითხზე შექმენით ნამუშევარი პითონის turtle ბიბლიოთეკით

from turtle import*

speed(400)
#drawing footballer
penup()
goto(50,0)
pendown()
color("black")
begin_fill()

#head
circle(50)
end_fill()
right(90)
#body

width(10)
forward(200)
right(25)
forward(200)
right(180)
forward(200)
right(130)
forward(200)
right(180)
forward(200)
right(25)
forward(150)
left(150)
forward(120)
right(180)
forward(120)
right(120)
forward(120)

#drawing a ball

penup()
goto(-100,-400)
pendown()
color("cyan")
begin_fill()
circle(50)
end_fill()


exitonclick()
