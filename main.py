import time
import turtle
from turtle import *
drawing_area = turtle.Screen()
drawing_area.bgcolor('black')
drawing_area.setup(width=1280,height=720)

speed(50)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

time.sleep(3)