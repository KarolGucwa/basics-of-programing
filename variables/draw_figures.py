import turtle
from figures import draw_square, draw_triangle, draw_rectangle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

pen.penup()
pen.goto(-100, 100) 
pen.pendown()
draw_square(100)


pen.penup()
pen.goto(-200, 100) 
pen.pendown()
draw_triangle(100)

pen.penup()
pen.goto(200, 200) 
pen.pendown()
draw_rectangle(150, 75)

pen.hideturtle()
window.mainloop()
