import turtle
from turtle_shape import arc, circle, move, polygon


alex = turtle.Turtle()
alex.speed(0)

# large circle
circle(alex, 100)

# two arcs
move(alex, 0, 100)
alex.setheading(180)
arc(alex, 50, 180)

move(alex, 0, 100)
alex.setheading(0)
arc(alex, 50, 180)

# small circles
move(alex, 0, 50 + 100 / 6)
circle(alex, 100 / 6)

move(alex, 0, 150 + 100 / 6)
circle(alex, 100 / 6)

turtle.mainloop()
