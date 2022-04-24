#fractal tree
from turtle import *
setheading(90)
penup()
setpos(0, -250) #bottom of page.
pendown()
def fractal_tree_color(length, level):
    pensize(length / 10)
    if length < 20:
        pencolor('green') #green leaves
    else:
        pencolor('brown') #branch + trunk
    speed(0)
    if level > 0:
        fd(length)
        rt(30)
        fractal_tree_color(length * 0.7 , level - 1)
        lt(90)
        fractal_tree_color(length * 0.5 , level - 1)
        rt(60)
    penup()
    bk(length)
    pendown()
    
        
