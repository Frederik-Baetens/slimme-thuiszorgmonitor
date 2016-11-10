import serial
message=''
ser=serial.Serial('/dev/rfcomm0',)
f=open(
while True:    
    data=str(ser.read(),'utf-8')
    if data!='.':
        message+=(data)
    else:
        print (message)

        message=''


