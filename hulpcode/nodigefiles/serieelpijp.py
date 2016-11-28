import serial
import Decryptie
import os

last_counter = -1
message=''
decrypted_message=()
ser=serial.Serial('/dev/rfcomm0')
ekgfile = os.open('ekgpipe', os.O_WRONLY)
pofile = os.open('popipe', os.O_WRONLY)

def dereform(string):
    """
    Maakt van de ontvangen vlakke string ('aaa.bbb.ccc. ... .zzz') opnieuw tupple van een lijst, een nummer en een lijst.
    """

    #herwerk de string tot een lijst van afzonderlijke waarden
    list = []
    check_new_point = 1
    index_last_point = -1
    while check_new_point < len(string):
        if string[check_new_point] == '.':
            list.append(int(string[index_last_point + 1:check_new_point]))
            index_last_point = check_new_point
        check_new_point += 1

    list.append(int(string[index_last_point+1:-1]))
    return list[:16], list[16], list[17:]

while True:
    data = str(ser.read(),'utf-8')
    if data == ':':
        #zorgt voor start met :
        while True:
            data = str(ser.read(),'utf-8')
            if data != ':':
                message += data
                
            else:
                dereformed_message = dereform(message)  #zet de string terug om naar: ([16], counter, [16])
                current_counter = dereformed_message[1] #onthoud de counter voor later te vergelijken met de vorige 
                decrypted_message = Decryptie.Ontcijfering(dereform(message))
                
                if decrypted_message!= None and (current_counter > last_counter):
                    #Als de gedecrypteerde waarde een fout bezit, wordt hij None,om te voorkomen dat het programma
                    #foutloopt en stopt zorgt dit ervoor dat de None waarde genegeerd wordt
                    #Als de huidige counter niet groter is dan die van het vorige pakket moet dit pakket overgeslagen worden
                    for i in range(0, 8):
                        print(str(decrypted_message[i]) + '\n')
                        os.write(ekgfile, str(decrypted_message[i]).encode('utf-8') + b'\n')
                    for i in range(8, 12):
                        print(str(decrypted_message[i]) + '\n')
                        os.write(pofile, str(decrypted_message[i]).convert('utf-8') + b'\n')
                    last_counter = current_counter
