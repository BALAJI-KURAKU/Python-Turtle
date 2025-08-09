from turtle import *

title('JAI SHREE RAM')
bgcolor('black')
pensize(6)
pencolor("orange")

Ram_naam = ["जय श्री राम"] * 50

angle = 360 / len(Ram_naam)
penup()
sety(-1)
for i in range(len(Ram_naam)):
    left(angle)
    forward(260)
    write(Ram_naam[i], align='right', font=('Arial', 12, "bold"))
    backward(260)

penup()
goto(-40, -20)
pendown()
write("|| राम ||", font=("Arial", 60, "normal"), align="center")
hideturtle()
done()
