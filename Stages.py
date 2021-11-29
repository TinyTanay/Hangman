from time import sleep
import turtle


def stages(tries):
    window = turtle.Screen()
    window.bgpic("turtle_background.png")
    window.setup(width=800, height=600, startx=1100, starty=0)
    turtle.pensize(15)
    if tries == 1:
        global running
        turtle.circle(50)
        turtle.right(45)
        turtle.forward(150)
        turtle.backward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.backward(150)
        turtle.left(45)
        turtle.forward(200)
        turtle.right(45)
        turtle.forward(100)
        turtle.backward(100)
        turtle.left(90)
        turtle.forward(100)
        sleep(1)
        turtle.reset()
    elif tries == 2:
        global running
        turtle.circle(50)
        turtle.right(45)
        turtle.forward(150)
        turtle.backward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.backward(150)
        turtle.left(45)
        turtle.forward(200)
        turtle.right(45)
        turtle.forward(100)
        sleep(1)
        turtle.reset()
    elif tries == 3:
        global running
        turtle.circle(50)
        turtle.right(45)
        turtle.forward(150)
        turtle.backward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.backward(150)
        turtle.left(45)
        turtle.forward(200)
        sleep(1)
        turtle.reset()
    elif tries == 4:
        global running
        turtle.circle(50)
        turtle.right(45)
        turtle.forward(150)
        turtle.backward(150)
        turtle.right(45)
        turtle.forward(150)
        sleep(1)
        turtle.reset()
    elif tries == 5:
        global running
        turtle.circle(50)
        turtle.right(90)
        turtle.forward(150)
        sleep(1)
        turtle.reset()
    elif tries == 6:
        global running
        turtle.circle(50)
        sleep(1)
        turtle.reset()
    elif tries == 100:
        global running
        style = ('Courier', 30, 'italic')
        turtle.write('POSITION THIS', font=style, align='center')
        turtle.reset()
