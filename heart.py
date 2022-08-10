from turtle import *
from colorsys import *

def curve():
	for i in range(200):
		right(1)
		forward(1)

tracer(10)
delay(0)
speed(0)
pensize(3)
bgcolor("lightblue")

left(140)

cycle_number=2
for _ in range(cycle_number):
	s=1
	for i in range(36):
		color("#fa056d",hsv_to_rgb(0.92,s,1))
		begin_fill()
		forward(111.65)
		curve()
		left(120)
		curve()
		forward(111.65)
		end_fill()
		hideturtle()
		right(90)
		s-=0.02
done()
