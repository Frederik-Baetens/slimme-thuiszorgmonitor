import pyb
FREQ=128

PIN_RED_LED_NB = 'X9'       
PIN_INFRARED_LED_NB = 'X10'

pin_red_led = pyb.Pin(PIN_RED_LED_NB, pyb.Pin.OUT_PP)
pin_infrared_led = pyb.Pin(PIN_INFRARED_LED_NB, pyb.Pin.OUT_PP)

tim8 = pyb.Timer(1, freq = FREQ)
tim8.callback(lambda t: switch_leds())

def switch_leds():
    if pin_red_led.value([])== 0:
        pin_red_led.value([1])
        pin_infrared_led.value([0])
    else:
        pin_red_led.value([0])
        pin_infrared_led.value([1])
  
