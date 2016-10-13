# info =>
#
# bemonsteren                 => Tom, Arnout
#
# 'encryptie'                => Siebe, Ruben
#
# => doorsturen (bluetooth)  => Jarno
#
# 'decryptie'

## BRONNEN
# http://docs.micropython.org/


## INTERFACE
# analoog_object = pyb.ADC(analoge_pin)           # create an analog object from a pin
# val = analoog_object.read_timed(buffer, freq)   # read an analog value
#                                                 # val = een pakktetje informatie
#
# adc = pyb.ADCAll(resolution)               # create an ADCAll object
# val = analoog_object.read_channel(channel) # read the given channel
# val = analoog_object.read_core_temp()      # read MCU temperature
# val = analoog_object.read_core_vbat()      # read MCU VBAT
# val = analoog_object.read_core_vref()      # read MCU VREF
#
#
# adc = pyb.ADC(pyb.Pin.board.X19)    # create an ADC on pin X19
# tim = pyb.Timer(6, freq=10)         # create a timer running at 10Hz
# buf = bytearray(100)                # creat a buffer to store the samples
# adc.read_timed(buf, tim)            # sample 100 values, taking 10s


import pyb

PO_PIN_NB = ''
ECG_PIN_NB = ''
PRESSURE_PIN_NB = ''
FREQ = 128

PO_PIN = pyb.ADC(PO_PIN_NB)
ECG_PIN = pyb.ADC(ECG_PIN_NB)
PRESSURE_PIN = pyb.ADC(PRESSURE_PIN_NB)

PIN_RED_LED = pyb.Pin('X1', Pin.OUT_PP)            #X1 (naam van de pin) aanpassen!
PIN_INFRARED_LED = pyb.PIN('X2', Pin.OUT_PP)       #X2 (naam van de pin) aanpassen!

current_led = PIN_RED_LED
next_led = PIN_INFRARED_LED

def switch_leds(current_led,next_led):
    current_led.low()
    next_led.high()
    current_led, next_led = next_led, current_led


def send(message):    #Jarno



def encrypt(list):    #Siebe, Ruben

    return encrypted_message


def read_and_send():

    value_ecg = ECG_PIN.read()
    value_PO = PO_PIN.read()
    value_pressure = PRESSURE_PIN.read()
    switch_leds(current_led, next_led)


    list = [value_ecg, value_PO, value_pressure]

    def reform(list)
        return message = [(12 cijfers) * 3, 92 0'en]  ' \


    encrypted_message = encrypt(message)

    send(message) #Jarno



tim = pyb.Timer(4, freq=FREQ)
tim.callback(read_and_send())
