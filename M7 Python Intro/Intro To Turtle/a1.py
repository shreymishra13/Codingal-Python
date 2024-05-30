import turtle

# creating canvas
turtle.Screen().bgcolor("Red")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(2):
    board.forward(100)
    board.left(90)
    board.forward(200)
    board.left(90)
	


turtle.done()
