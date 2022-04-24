# sierpinski triangle
from turtle import *
def sierpinski(length, level):
    speed(0)
    if level == 0:
        return
    begin_fill()
    color('red')
    for i in range(3):
        sierpinski(length / 2, level - 1)
        fd(length)
        lt(120) #left turn 120deg
    end_fill()
    
        
        
        
        
