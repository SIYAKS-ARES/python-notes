from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("green")
jimmy.forward(130)
jimmy.right(90)
jimmy.forward(130)
jimmy.right(90)
jimmy.forward(130)
jimmy.right(90)
jimmy.forward(130)
jimmy.shapesize(2, 2)

my_screen = Screen()

print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()
