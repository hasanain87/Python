from turtle import *

def setup(width, height):
	"""Set up parameters for the graph, x between -WIDTH/2 and WIDTH/2, y between -HEIGHT/2 and HEIGHT/2 """
	setworldcoordinates(-width/2,-height/2,width/2,height/2,)
	speed("fastest")
	colormode(1)
	color(1,1,1)
	bgcolor("black")

setup(600, 600)

pu()
goto(-250,250)
pd()
for _ in range(4):
	fd(25)
	rt(90)
pu()

goto(-250,150)
pd()
for _ in range(4):
	fd(100)
	rt(90)
pu()

goto(-250,-50)
pd()
for _ in range(4):
	fd(200)
	rt(90)
pu()

def draw_square(length):
	pd()
	for _ in range(4):
		fd(length)
		rt(90)
	pu()

color(1,1,0)
goto(10,250)
draw_square(25)
goto(10,150)
draw_square(100)
goto(10,-50)
draw_square(200)

done()
