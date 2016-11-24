import serial
message=''
ser=serial.Serial('/dev/rfcomm0')
ekgfile = open('/home/frederik/Documents/ekgfile.txt','a')
pofile = open ('/home/frederik/Documents/pofile.txt' ,'a')
filelijst = [ekgfile,pofile]
position = 0
filecounter = 0

while True:
    data = str(ser.read(),'utf-8')
    if data == ':':         #zorgt voor start met :
        while True:
            data = str(ser.read(),'utf-8')
            if data != '.' and data != ':':
                message += data
            else:
                print (message)
                message += '\n'
                filelijst[filecounter].write(message)
                message = ''
                position += 1
                if position == 8:
                    filecounter = 1
                elif position == 12:
                    filecounter = 0
                    position = 0
