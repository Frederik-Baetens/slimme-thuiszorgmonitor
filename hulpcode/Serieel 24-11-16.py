import serial
message=''
decrypted_message=()
ser=serial.Serial('/dev/rfcomm0')
ekgfile = open('/home/frederik/Documents/ekgfile.txt','a')
pofile = open ('/home/frederik/Documents/pofile.txt' ,'a')


while True:
    data = str(ser.read(),'utf-8')
    if data == ':':         #zorgt voor start met :
        while True:
            data = str(ser.read(),'utf-8')
            if data != ':':
                message += data
            else:
                decrypted_message = DECRYPT(dereform(message))
                
                for i in range(0, 8):
                    print(decrypted_message[i]) + '\n')
                    ekgfile.write(str(decrypted_message[i]) + '\n')

                for i in range(8, 12):
                    print(decrypted_message[i]) + '\n')
                    pofile.write(str(decrypted_message[i] + '\n')
  
                message= ''
                

                
                
                
