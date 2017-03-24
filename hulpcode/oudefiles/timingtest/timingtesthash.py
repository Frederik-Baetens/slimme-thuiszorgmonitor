import pyb, uhashlib
b=bytearray(16)

def timerhash():
	start = pyb.micros()
	c=uhashlib.sha256(b).digest()
	return c, pyb.elapsed_micros(start)
	
