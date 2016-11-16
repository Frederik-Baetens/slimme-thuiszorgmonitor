import serial
message=''
ser=serial.Serial('/dev/rfcomm0',)
f= open('/home/frederik/Documents/test.txt','a')
while True:
    data=str(ser.read(),'utf-8')
    if data!='.':
        message+=(data)
    else:
        print (message)
        message+='\n'
        f.write(message)
        message=''


