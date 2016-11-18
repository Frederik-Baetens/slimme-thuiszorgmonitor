## IMPORTS ##
import pyb, time, EncryptieCode


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


## INITIALIZATIE ##

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
tim7 = pyb.Timer(7, freq = FREQ/NB_READINGS)    
tim7.callback(lambda t: toggle_enable_reading())    #encrypt en reform
sw = pyb.Switch()
sw.callback(lambda:pyb.LED(2).toggle())

tim9 = pyb.Timer(9, freq=64)
pwm1 = tim9.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.X3, pulse_width_percent=50) 
pwm2 = tim9.channel(2, pyb.Timer.PWM_INVERTED, pin=pyb.Pin.board.X4, pulse_width_percent=50)

lst = [0,]*NB_READINGS*NB_SENSORS
lste = [0,]*NB_READINGS
lstp = [0,]*(NB_READINGS//2)


## FUNCTIES ##
def reform_list(tup):
    #zet alle waarden uit een tuple: (lijst, getal, lijst)
    #in 1 lage string, de waarden zijn gesplitst door punten met op het einde een dubbelpunt
    return '.'.join([str(i) for i in tup])

def encrypt(lst):
    enclst = lst
    print (lst)
    global message
    message = reform_list(enclst)
    return

def read(NB_READINGS):
    global read_counter
    lst[0+read_counter] = ecg_pin.read()
    #if po_counter = 
    lst[1+read_counter]= po_pin.read()
    #lst[2+read_counter]= pressure_pin.read()
    switch_leds()                       #overbodig, vervangen door pwm
    if read_counter == (NB_READINGS-1)*NB_SENSORS:
        read_counter = 0
    else: read_counter += NB_SENSORS
    return 

def switch_leds():
    pin_red_led.toggle()
    pin_infrared_led.toggle()
    return

lijst1=[0,4095,1555,1489,2098,255,1023,1024]
lijst2=[0,255,16,15]


def timer():
    start = time.ticks_us()
    #reform_list(([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],15,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
    #EncryptieCode.Vercijfering(12,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    
    lijst2_1 = [hex(i)[2:] for i in lijst2]
    lijst2_2 = [i if len(i)==2 else '0'+i for i in lijst2_1]
    lijst2_3 = [i for string in lijst2_2 for i in string]
    lijst2_4 = [eval('0x'+i) for i in lijst2_3]
    '''
    print (lijst2_1)
    print (lijst2_2)
    print (lijst2_3)
    print (lijst2_4)
    '''
    lijst1_1 = [hex(i)[2:] for i in lijst1]
    lijst1_2 = ['0'*(3-len(i))+i for i in lijst1_1]
    lijst1_3 = [i for string in lijst1_2 for i in string]
    lijst1_4 = [eval('0x'+i) for i in lijst1_3]
    '''
    print (lijst1_1)
    print (lijst1_2)
    print (lijst1_3)
    print (lijst1_4)
    '''

    totlijst=lijst1_4+lijst2_4
    
    return time.ticks_diff(start,time.ticks_us())

def toggle_enable_reading():
    global enable_reading
    enable_reading = 1

##LOOP##
# alles wat het bordje moet weten: functies variabelen etc moet hiervoor
# wat hierna komt wordt nooit geevalueerd.
while True:
    if enable_reading and read_counter==(NB_READINGS-1)*NB_SENSORS and pyb.Pin('A14').value() == 1:
        enable_reading = 0
        encrypt(lst)
