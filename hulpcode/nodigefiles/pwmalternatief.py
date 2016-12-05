import pyb, time
FREQ=128

pin = pyb.Pin(pyb.Pin.board.X6, pyb.Pin.OUT_PP)

tim1 = pyb.Timer(10, freq = FREQ/2)
tim1.callback(lambda t: switch_pins())

def switch_pins():
    if pin.value()==0:
        pin.value(1)
    else:
        pin.value(0)
