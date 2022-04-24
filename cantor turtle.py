#plant a cantor fractal set.
#run the module

from turtle import * #import all functions from turtle library
def cantor(x, y, length):
    if length >=5:
        speed(1) #speed of turtle
        penup()
        pensize(3)
        pencolor('red')
        setpos(x, y)
        pendown()
        fd(length) #move turtle forward
        y -= 30 #y = y - 30
        cantor(x, y , length / 3)
        cantor(x + 2* length / 3, y, length / 3)
        penup()
        setpos(x, y + 30)
        
        
        
        
        
    
