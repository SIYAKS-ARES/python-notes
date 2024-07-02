from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("green")
jimmy.forward(130)

my_screen = Screen()

print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()
