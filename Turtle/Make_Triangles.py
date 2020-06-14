# ----To install TURTLE run the below commands-----

# sudo apt-get install -y python3-wxgtk4.0
# python3 -m pip install --user PythonTurtle

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out_png = '/content/out_file.png'

from turtle import *
number_of_shapes = 3
playground = Screen() 
playground.screensize(100, 150)
playground.title("Turtle Plot")

tom = Turtle()             
tom.color("black")
tom.setposition(0, 0)
tom.speed("fastest")
tom.color("black")

for shape in range(1, number_of_shapes + 1):
    forward(shape * 10)
    for _ in range(2):
        left(120)
        forward(shape * 20)
    left(120)
    forward(shape * 10)

    right(90)
    penup()
    forward(7)
    pendown()
    left(90)
    p = tom.pos()              
    tom.write(str(p), True)     
    tom.penup()

# print(p) 
