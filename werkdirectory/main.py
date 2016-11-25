## IMPORTS ##
import pyb, time, Encryptie


## CONSTANTEN ##
FREQ = 128              #frequentie waaraan gemeten wordt
NB_READINGS = 8
NB_SENSORS = 2

## PIN-NUMMERS ##
PO_PIN_NB = 'X19'           #nummer van de pulse-oximeter pin
ECG_PIN_NB = 'X20'          #nummer van de electrocardiogram pin
PRESSURE_PIN_NB = 'X21'     #nummer van de druksensor pin
PIN_RED_LED_NB = 'X3'       #nummer van de rode led pin
PIN_INFRARED_LED_NB = 'X4'  #nummer van de infrarode led pin


## PINNEN AANMAKEN ##
po_pin = pyb.ADC(PO_PIN_NB)
ecg_pin = pyb.ADC(ECG_PIN_NB)
pressure_pin = pyb.ADC(PRESSURE_PIN_NB)
pin_red_led = pyb.LED(3)        #moet weg, wordt nu met pwm gedaan
pin_infrared_led = pyb.LED(4)   #voorlopig nog om leds te laten branden


## INITIALISATIE ##
pin_red_led.toggle()

read_counter = 0
message = ''
enable_reading = 0
po_counter = 0
encryptie_counter = 0

uart = pyb.UART(4, 1382400)
tim1 = pyb.Timer(1, freq = FREQ)
tim1.callback(lambda t: read(NB_READINGS))          #lezen
tim2 = pyb.Timer(2, freq = FREQ/NB_READINGS)
tim2.callback(lambda t: uart.write(message))        #versturen
tim7 = pyb.Timer(7, freq = FREQ/(NB_READINGS))    
tim7.callback(lambda t: toggle_enable_reading())    #encrypt en reform
sw = pyb.Switch()
sw.callback(lambda:pyb.LED(2).toggle())

tim9 = pyb.Timer(9, freq=64)
pwm1 = tim9.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.X3, pulse_width_percent=50) 
pwm2 = tim9.channel(2, pyb.Timer.PWM_INVERTED, pin=pyb.Pin.board.X4, pulse_width_percent=50)

lst_ecg = [0,]*NB_READINGS
lst_po = [0,]*(NB_READINGS//2)


## FUNCTIES ##
def reform_list(tup):
    #zet alle waarden uit een tuple: (lijst, getal, lijst)
    #in 1 lage string, de waarden zijn gesplitst door punten met op het einde een dubbelpunt
    return '.'.join([str(i) for i in tup[0]])  + '.' + str(tup[1]) + '.' + '.'.join([str(i) for i in tup[2]]) + ':'

def encrypt(lst):
    print (lst)
    global encryptie_counter
    encryptie_counter += 1
    enclst = Encryptie.Vercijfering(encryptie_counter,lst)
    global message
    message = reform_list(enclst)
    return

def read(NB_READINGS):
    global read_counter

    lst_ecg[read_counter] = ecg_pin.read()
    if read_counter % 2 == 0:
        lst_po[read_counter//2] = po_pin.read()//16

    if read_counter == NB_READINGS - 1:
        read_counter = 0
    else:
        read_counter += 1
    return

def switch_leds():
    pin_red_led.toggle()
    pin_infrared_led.toggle()
    return

def timer():
    start = time.ticks_us()
    #reform_list(([1,2,3,4,5,6,7,8,9,10,11,12],15,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
    Encryptie.Vercijfering(12,[3095,255,1,0,4095,4095,1000,0,0,255,144,255])
    #read(NB_READINGS)
    return time.ticks_diff(time.ticks_us(),start)

def toggle_enable_reading():
    global enable_reading
    enable_reading = 1

##LOOP##
# alles wat het bordje moet weten: functies variabelen etc moet hiervoor
# wat hierna komt wordt nooit geevalueerd.
while True:
    if enable_reading and read_counter == NB_READINGS-1 and pyb.Pin('A14').value() == 1:
        enable_reading = 0
        encrypt(lst_ecg + lst_po)
        switch_leds()
