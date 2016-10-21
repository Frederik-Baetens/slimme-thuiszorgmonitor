## IMPORTS ##
import pyb, time


## CONSTANTEN ##
FREQ = 128              #frequentie waaraan gemeten wordt
LENGTH_ELEMENT = 12     #constanten voor omzetten naar binair
LENGTH_MESSAGE = 128    #lengte totale boodschap voor aes encryptie


## PIN-NUMMERS ##
PO_PIN_NB = 'X19'           #nummer van de pulse-oximeter pin
ECG_PIN_NB = 'X20'          #nummer van de electrocardiogram pin
PRESSURE_PIN_NB = 'X21'     #nummer van de druksensor pin
PIN_RED_LED_NB = 'X9'       #nummer van de rode led pin
PIN_INFRARED_LED_NB = 'X10' #nummer van de infrarode led pin


## PINNEN AANMAKEN ##
po_pin = pyb.ADC(PO_PIN_NB)
ecg_pin = pyb.ADC(ECG_PIN_NB)
pressure_pin = pyb.ADC(PRESSURE_PIN_NB)
pin_red_led = pyb.LED(3)        #voorlopig voor test, moet een pin worden
pin_infrared_led = pyb.LED(4)   #voorlopig voor test, moet een pin worden


## INITIALIZATIE ##
pin_red_led.on()
pin_infrared_led.off()
tim = pyb.Timer(1, freq=FREQ/128)   #frequentie moet gewoon FREQ worden
sw.callback(lambda: switch_leds())  #probeersel voor interrupt
sw = pyb.Switch()                   #misschien switch niet nodig

## FUNCTIES ##
def reform_list(list):
    # returns a message from a list in binary that is 128 characters long
    for i in range(len(list)):
        list[i] = bin(list[i])[2:]
    for i in range(len(list)):
        if len(list[i]) < LENGTH_ELEMENT:
            list[i] = (LENGTH_ELEMENT-len(list[i]))*'0' + list[i]
    message = ''
    for i in list:
        message += i
    if len(message) < LENGTH_MESSAGE:
        message += (LENGTH_MESSAGE-len(message))*'0'
    return message


def read_and_send():
    # read the values of the sensor pins, switch the LEDs, encrypt the message, send the message via Bluetooth
    list = []
    list.append(ecg_pin.read())
    list.append(po_pin.read())
    list.append(pressure_pin.read())
    switch_leds() 
    
    message = reform_list(list)
    print(message)
    
    #ENCRYPTIE: encrypted_message = encrypt(message)
    #BLUETOOTH: send(encrypted_message)


def switch_leds():
    pin_red_led.toggle()
    pin_infrared_led.toggle()


#timer, voorlopig voor tests
def timer(function):
    start=time.ticks_us()
    function
    stop=time.ticks_us()
    return time.ticks_diff(start,stop)
##LOOP##
# alles wat het bordje moet weten: functies variabelen etc moet hiervoor
# wat hierna komt wordt nooit geevalueerd.
while True:
    if tim.counter()==0:
        read_and_send()



"""
def encrypt(message):
    pass
def send(encrypted_message):
    pass
"""
