#######################
## ~~~  SCHOEN  ~~~  ##
#######################


## IMPORTS ##
import pyb, time, Encryptie


## CONSTANTEN ##
FREQ = 100                           #frequentie waaraan gemeten wordt
NB_READINGS = 8
NB_SENSORS = 2


## PIN-NUMMERS ##
SCHOEN_VOORAAN_NB = 'X19'           #nummer van de druksensor in de schoen vooraan pin
SCHOEN_ACHTERAAN_NB = 'X20'         #nummer van de druksensor in de schoen achteraan pin


## PINNEN AANMAKEN ##
schoen_vooraan_pin = pyb.ADC(SCHOEN_VOORAAN_NB)
schoen_achteraan_pin = pyb.ADC(SCHOEN_ACHTERAAN_NB)


## INITIALISATIE ##
read_counter = 0
message = ''
enable_encryption = 0
po_counter = 0
encryptie_counter = 0

uart = pyb.UART(4, 1382400)
tim1 = pyb.Timer(1, freq = FREQ)
tim1.callback(lambda t: read(NB_READINGS))          #lezen
tim2 = pyb.Timer(2, freq = FREQ/NB_READINGS)
tim2.callback(lambda t: uart.write(message))        #versturen
tim7 = pyb.Timer(7, freq = FREQ/(NB_READINGS))    
tim7.callback(lambda t: toggle_enable_encryption())    #encrypt en reform
sw = pyb.Switch()
sw.callback(lambda:pyb.LED(2).toggle())

lst_vooraan = [0,]*NB_READINGS
lst_achteraan = [0,]*NB_READINGS


## FUNCTIES ##
def REFORM_LIST(tup):

    return '.'.join( [str(i) for lst in tup[0] for i in lst] ) + '.' +\
        str(tup[1]) + '.' + '.'.join( [str(i) for lst in tup[2] for i in lst] ) + ':'


def encrypt(lst):
    print (lst)
    global encryptie_counter
    encryptie_counter += 1
    enclst = Encryptie.Vercijfering(encryptie_counter,lst)
    global message
    message = REFORM_LIST(enclst)
    return


def read(NB_READINGS):
    global read_counter

    lst_vooraan[read_counter] = schoen_vooraan_pin.read()//16
    lst_achteraan[read_counter] = schoen_achteraan_pin.read()//16

    if read_counter == NB_READINGS - 1:
        read_counter = 0
    else:
        read_counter += 1
    return


def toggle_enable_encryption():
    global enable_encryption
    enable_encryption = 1


##LOOP##
# alles wat het bordje moet weten: functies variabelen etc moet hiervoor
# wat hierna komt wordt nooit geevalueerd.
while True:
    if enable_encryption and read_counter == NB_READINGS-1 and pyb.Pin('A14').value() == 1:
        enable_encryption = 0
        encrypt(lst_vooraan + lst_achteraan)
 








