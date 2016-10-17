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


##INITIALIZATIE

#Imports
import pyb

#Constanten
FREQ = 128              #frequentie waaraan gemeten wordt
LENGHT_ELEMENT = 12
LENGHTH_MESSAGE = 128

#Pin nummers
PO_PIN_NB = ''              #nummer van de pulse-oximeter pin
ECG_PIN_NB = ''             #nummer van de electrocardiogram pin
PRESSURE_PIN_NB = ''        #nummer van de druksensor pin
PIN_RED_LED_NB = 'X1'       #X1: naam van de pin, naam van deze pin moet nog aangepast worden
PIN_INFRARED_LED_NB = 'X2'  #X2: naam van de pin, naam van deze pin moet nog aangepast worden

#Timer
#mogelijke code voor timer, moet getest worden
tim = pyb.Timer(4, freq=FREQ)
tim.callback(read_and_send())

#Naam geven aan de pinnen en sensoren 
po_pin = pyb.ADC(PO_PIN_NB)
ecg_pin = pyb.ADC(ECG_PIN_NB)
pressure_pin = pyb.ADC(PRESSURE_PIN_NB)
pin_red_led = pyb.Pin(PIN_RED_LED_NB, Pin.OUT_PP)           #X1 (naam van de pin) aanpassen!
pin_infrared_led = pyb.Pin(PIN_INFRARED_LED_NB, Pin.OUT_PP) #X2 (naam van de pin) aanpassen!
accel = pyb.Accel()

#Initializatie current_led en next_led
current_led = pin_red_led
next_led = pin_infrared_led


##FUNCTIES

def switch_leds(current_led,next_led):
    current_led.low()
    next_led.high()
    current_led, next_led = next_led, current_led


def send(message):    #Jarno
    return


def encrypt(message):
    return encrypted_message


def reform_list(list):
    #returns a message in binary that is 128 characters long
    for i in len(list):
        a[i] = str(bin(a[i]))
    for i in range(len(list)):                                          
        if len(list[i]) < LENGHT_ELEMENT:
            list[i] = (LENGTH_ELEMENT-len(list[i]))*'0' + list[i]
    message = ''
    for i in list:
        message += i
    if len(message) < LENGTH_MESSAGE:
        message += (LENGTH_MESSAGE-len(message))*'0'
    return message


def read_and_send():
    value_ecg = ecg_pin.read()
    value_po = po_pin.read()
    value_pressure = pressure_pin.read()
    switch_leds(current_led, next_led)

    list = [value_ecg, value_po, value_pressure]
    
    message = reform_message(list)
    encrypted_message = encrypt(message)

    send(encrypted_message) #Jarno

