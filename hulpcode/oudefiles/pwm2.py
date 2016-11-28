import pyb

timer = pyb.Timer(9, freq=64)
ch2 = timer.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.X3, pulse_width_percent=50)
ch3 = timer.channel(2, pyb.Timer.PWM_INVERTED, pin=pyb.Pin.board.X4, pulse_width_percent=50)
