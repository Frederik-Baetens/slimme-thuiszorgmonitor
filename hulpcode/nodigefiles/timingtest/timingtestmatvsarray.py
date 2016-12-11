import pyb

mat= [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],15,[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

lst = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]

bytearr= bytearray([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])

def timerbyte():
	start=pyb.micros()
	for i in range(1000):
		bytearr[4]
	return pyb.elapsed_micros(start)

def timermat():
	start=pyb.micros()
	for i in range(1000):
		mat[2][1][0]
	return pyb.elapsed_micros(start)

def timerlst():
	start=pyb.micros()
	for i in range(1000):
		lst[4]
	return pyb.elapsed_micros(start)

