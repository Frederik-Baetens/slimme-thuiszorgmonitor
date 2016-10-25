import pyb 
tim=pyb.Timer(2, freq=0.5) 
ch=tim.channel(2, pyb.Timer.PWM, pin=pyb.Pin.board.X2) 
ch.pulse_width_percent(50)
~                             
