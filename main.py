## IMPORTS ##
import pyb, utime


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
sw = pyb.Switch()                   #misschien switch niet nodig
sw.callback(lambda: switch_leds())  #probeersel voor interrupt

## FUNCTIES ##
def reform_lst(lst):
    # returns a message from a list in binary that is 128 characters long
    for i in range(len(lst)):
        lst[i] = "{0:b}".format(i)      
    for i in range(len(lst)):
        if len(lst[i]) < LENGTH_ELEMENT:
            lst[i] = (LENGTH_ELEMENT-len(lst[i]))*'0' + lst[i]
    message = ''
    for i in lst:
        message += i
    #if len(message) < LENGTH_MESSAGE:
    #    message += (LENGTH_MESSAGE-len(message))*'0'
    return message

def read():
    lst = []
    lst.append(ecg_pin.read())
    lst.append(po_pin.read())
    lst.append(pressure_pin.read())
    return lst 

def switch_leds():
    pin_red_led.toggle()
    pin_infrared_led.toggle()

def read_and_send():
    # read the values of the sensor pins, switch the LEDs, encrypt the message, send the message via Bluetooth
    switch_leds() 
    lst=read()
    message = reform_lst(lst)
    print(message)
    
    #ENCRYPTIE: encrypted_message = encrypt(message)
    #BLUETOOTH: send(encrypted_message)

#timer, voorlopig voor tests
def timer():
    start=utime.ticks_us()
    read_and_send()
    return utime.ticks_diff(start,utime.ticks_us())

print (timer())

##LOOP##
# alles wat het bordje moet weten: functies variabelen etc moet hiervoor
# wat hierna komt wordt nooit geevalueerd.
while False:
    if tim.counter()==0:
        read_and_send()


"""
def encrypt(message):
    pass
def send(encrypted_message):
    pass
"""
