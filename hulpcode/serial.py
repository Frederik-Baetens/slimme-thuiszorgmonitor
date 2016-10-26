import serial, struct

ser=serial.Serial('/dev/rfcomm0')
data=ser.read()
boodschap=struct.unpack('!B',data)

