from turtle import *
from math import cos, pi

def setup(width, height):
	"""Set up parameters for the graph, x between -WIDTH/2 and WIDTH/2, y between -HEIGHT/2 and HEIGHT/2 """
	setworldcoordinates(-width/2,-height/2,width/2,height/2)
	speed("fastest")
	colormode(1)
	color(1,1,1)
	bgcolor("black")

setup(500, 500)

### Four line drawing routines

def draw_line(length):
	pd()
	fd(length)
	pu()

def draw_dashed_line(length):
	pen_down = True
	for _ in range(5):
		pd() if pen_down else pu()
		fd(length/5)
		pen_down = not pen_down
	pu()

def draw_wiggly_line(length):
	pen_down, angle = 0, 10
	dist = (length/12) / cos(angle * (pi/180)) ### distance along line
	pd()
	for _ in range(12):
		lt(angle) if (pen_down == 0 or pen_down == 3) else rt(angle)
		fd(dist)
		rt(angle) if (pen_down == 0 or pen_down == 3) else lt(angle)
		pen_down = (pen_down + 1) % 4
	pu()

### Three squares with no abstraction

pu()
goto(-200,200)
for _ in range(4):
	draw_line(100)
	rt(90)

goto(-200,50)
for _ in range(4):
	draw_dashed_line(100)
	rt(90)

goto(-200,-100)
for _ in range(4):
	draw_wiggly_line(100)
	rt(90)

### Three squares WITH abstraction!

def draw_100_square(line_drawer):
	pd()
	for _ in range(4):
		line_drawer(100)
		rt(90)
	pu()

color(1,1,0)
goto(100,200)
draw_100_square(draw_line)
goto(100,50)
draw_100_square(draw_dashed_line)
goto(100,-100)
draw_100_square(draw_wiggly_line)

done()