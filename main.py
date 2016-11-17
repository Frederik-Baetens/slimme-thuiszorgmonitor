## IMPORTS ##
import pyb, time, EncryptieCode


## CONSTANTEN ##
FREQ = 128              #frequentie waaraan gemeten wordt
NB_READINGS = 4
NB_SENSORS = 2

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
message = ''
a=0
counter = 0
pin_red_led.on()
pin_infrared_led.off()
uart = pyb.UART(4, 1382400)
tim1 = pyb.Timer(1, freq = FREQ)
tim1.callback(lambda t: read(NB_READINGS))      #lezen
tim2 = pyb.Timer(2, freq = FREQ/NB_READINGS)
tim2.callback(lambda t: uart.write(message))    #versturen
tim7 = pyb.Timer(7, freq = FREQ/NB_READINGS)    
tim7.callback(lambda t: toggle_a())             #encrypt en reform
sw = pyb.Switch()
sw.callback(lambda:pyb.LED(2).toggle())
lst=[0,]*NB_SENSORS*NB_READINGS
t=0

## FUNCTIES ##
def reform_list2(tup):
    #zet alle waarden van een tuple die een matrix, een integer en een matrix bevat om naar 1 lange string
    #de waarden worden van elkaar geslpitst met een punt
    #op het einde van de string staat ook een punt
    output = str()

    boodschap = [str(i) for l in tup[0] for i in l]
    counter = str(tup[1])
    tag = lst =[str(i) for l in tup[2] for i in l]

    output += '.'.join(boodschap) + '.' + counter + '.' + '.'.join(tag) + ':'

    return output

def encrypt(lst):
    #er wordt een lijst terug verwacht, dat bevat:
    #de 3 geencrypteerde waarden
    #de tag
    #de counter, ongeencrypteerd
    enclst = EncryptieCode.Vercijfering(12,lst)
    return enclst

def read(NB_READINGS):
    global t
    lst[0+t]= ecg_pin.read()
    lst[1+t]= po_pin.read()
    #lst[2+t]= pressure_pin.read()//16
    switch_leds()
    if t == (NB_READINGS-1)*NB_SENSORS:
        t = 0
    else: t += NB_SENSORS
    return 

def switch_leds():
    pin_red_led.toggle()
    pin_infrared_led.toggle()

    return

def read_and_send():
    # read the values of the sensor pins, switch the LEDs, encrypt the message, send the message via Bluetooth 
    enclst = encrypt(lst)
    global message
    message = reform_lst(enclst)
    print(message)



EncryptieCode.Vercijfering(12,[1,2,3,4,5,6,7,8])
#timer, voorlopig voor tests
def timer():
    start = time.ticks_us()
    EncryptieCode.Vercijfering(12,[1,2,3,4,5,6,7,8])
    return time.ticks_diff(start,time.ticks_us())

print (timer())

def toggle_a():
    global a
    a=1

##LOOP##
# alles wat het bordje moet weten: functies variabelen etc moet hiervoor
# wat hierna komt wordt nooit geevalueerd.
while True:
    if a and t==(NB_READINGS-1)*NB_SENSORS and pyb.Pin('A14').value()==1:
        a=0
        read_and_send()
