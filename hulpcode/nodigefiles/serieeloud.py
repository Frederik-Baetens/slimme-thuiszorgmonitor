import serial, os

message=''
ser=serial.Serial('/dev/rfcomm0')
ekgfile = os.open('ekgpipe', os.O_WRONLY)
pofile = os.open('popipe', os.O_WRONLY)
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
        os.write(fileijst[filecounter], message.encode('utf-8'))
        message=''
        filecounter = 1 - filecounter

