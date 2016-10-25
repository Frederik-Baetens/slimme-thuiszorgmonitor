## IMPORTS ##
import pyb, time


## CONSTANTEN ##
FREQ = 128              #frequentie waaraan gemeten wordt
NB_READINGS = 4

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
uart = pyb.UART(4,9600)
tim = pyb.Timer(1, freq = FREQ)   #frequentie moet gewoon FREQ worden
tim.callback(lambda t: read(NB_READINGS))
sw = pyb.Switch()                   #misschien switch niet nodig
sw.callback(lambda:pyb.LED(2).toggle())
lst=[0,]*3*NB_READINGS
t=0

## FUNCTIES ##
def reform_lst(lst):
    #de . scheid de waarden
    #deze functie is waarschijnlijk onnodig in dit bestand
    #encryptie heeft deze functie  nodig
    return '.'.join([str(i) for i in lst])

def encrypt(lst):
    #er wordt een lijst terug verwacht, dat bevat:
    #de 3 geencrypteerde waarden
    #de tag
    #de counter, ongeencrypteerd
    enclst = lst
    return enclst

def read(NB_READINGS):
    global t
    lst[0+t]= ecg_pin.read()
    lst[1+t]= po_pin.read()
    lst[2+t]= pressure_pin.read()//16
    switch_leds()
    if t == NB_READINGS*3-3:
        t = 0
    else: t += 3
    return 

def send(message):
    uart.write(message)
    return

def switch_leds():
    pin_red_led.toggle()
    pin_infrared_led.toggle()

def read_and_send():
    # read the values of the sensor pins, switch the LEDs, encrypt the message, send the message via Bluetooth 
    enclst = encrypt(lst)
    message = reform_lst(enclst)
    send(message)
    print(message)
    
    #ENCRYPTIE: encrypted_message = encrypt(message)
    #BLUETOOTH: send(encrypted_message)

#timer, voorlopig voor tests
def timer():
    start = time.ticks_us()
    read(NB_READINGS)
    return time.ticks_diff(start,time.ticks_us())

print (timer())


##LOOP##
# alles wat het bordje moet weten: functies variabelen etc moet hiervoor
# wat hierna komt wordt nooit geevalueerd.
while True:
    if tim.counter()==15 and t==NB_READINGS*3-3 and pyb.Pin('A14').value()==1:
        read_and_send()



"""
def encrypt(message):
    pass
def send(encrypted_message):
    pass
"""
