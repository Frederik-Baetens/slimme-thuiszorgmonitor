import serial
message=''
ser=serial.Serial('/dev/rfcomm0',)
ekgfile = open('/home/frederik/Documents/ekgfile.txt','a')
pofile = open ('/home/frederik/Documents/pofile.txt' ,'a')
filelijst = [ekgfile,pofile]

while True:
    data = str(ser.read(),'utf-8')
    if data == ':'
        filecounter = 0
    elif data != '.':
        message+=(data)
    else: # als .
        print (message)
        message+='\n'
        filelijst[filecounter].write(message)
        filecounter = 1 - filecounter
        message = ''


