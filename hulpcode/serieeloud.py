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
    if data == ':':
        print (message)
        message+='\n'
        filelijst[1].write(message)
        message=''
        filecounter = 0
    elif data != '.':
        message+=(data)
    else:
        print (message)
        message+='\n'
        filelijst[filecounter].write(message)
        message=''
        filecounter = 1 - filecounter

