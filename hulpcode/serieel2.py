import serial, struct
message = ''
ser = serial.Serial('/dev/rfcomm0',)

while True:
    data = str(ser.read(),'utf-8')
    print (data)
