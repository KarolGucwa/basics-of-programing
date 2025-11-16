import turtle

def draw_square(length):
    """Funkcja rysująca kwadrat o zadanej długości boku."""
    pen = turtle.Turtle()
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
    pen.hideturtle()

def draw_triangle(length):
    """Funkcja rysująca trójkąt równoramienny o zadanej długości boku."""
    pen = turtle.Turtle()
    for _ in range(3):
        pen.forward(length)
        pen.left(120)  
    pen.hideturtle()

def draw_rectangle(length_a, length_b):
    """Funkcja rysująca prostokąt o bokach a i b."""
    pen = turtle.Turtle()
    for _ in range(2):
        pen.forward(length_a)
        pen.left(90)
        pen.forward(length_b)
        pen.left(90)
    pen.hideturtle()
