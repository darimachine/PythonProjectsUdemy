import colorgram
colors = colorgram.extract('image_2.jpg', 10)
list_tuples = []
for i in colors:
    tuple = (i.rgb)
    real_tuple = (tuple.r,tuple.g,tuple.b)
    list_tuples.append(real_tuple)

print(list_tuples)
import turtle as t
from random import choice
color_list = list_tuples
#color_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64)]
dots = t.Turtle()
t.colormode(255)
t.setup(600,700)
t.title("Hirst Painting")
dots.speed("fastest")
dots.hideturtle()
dots.penup()
y = -250
dots.goto(-230,y)
for j in range(10):
    for i in range(10):
        dots.dot(20,choice(color_list))
        dots.forward(50)
    y+=50
    dots.goto(-230,y)






screen = t.Screen()
screen.exitonclick()