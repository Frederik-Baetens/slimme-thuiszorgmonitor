import pyb
def timernot():
	start = pyb.micros()
	x=0
	for i in range(10000):
		x+=1
	return pyb.elapsed_micros(start)

@micropython.native
def timernative():
	start = pyb.micros()
	x=0
	for i in range(10000):
		x+=1
	return pyb.elapsed_micros(start)
