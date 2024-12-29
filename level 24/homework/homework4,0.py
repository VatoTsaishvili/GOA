from turtle import*


speed(500)
penup()
goto(100, 100)
pendown()

for i in range(4):
    forward(200)
    left(90)


penup()
goto(-300, 100)
pendown()

for i in range(4):
    forward(200)
    left(90)


penup()
goto(-300, -300)
pendown()

for i in range(4):
    forward(200)
    left(90)


penup()
goto(100, -300)
pendown()

for i in range(4):
    forward(200)
    left(90)

exitonclick()
