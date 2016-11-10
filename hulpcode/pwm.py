import pyb 
timer = pyb.Timer(2, freq=1)
ch3 = timer.channel(3, pyb.Timer.PWM, pin=pyb.Pin.board.X3, pulse_width_percent=50)
