import serial
import Decryptie
import os

last_counter = -1
message=''
ser=serial.Serial('/dev/rfcomm0')
ekgfile = os.open('ekgpipe', os.O_WRONLY)
pofile = os.open('popipe', os.O_WRONLY)


def string_naar_lijst(string):
	lijst_waarden= []
	current_number = ''
	for i in range(len(string)):
		if string[i] != '.' and string[i] != ':':
			current_number += string[i]
		else:
			lijst_waarden.append(int(current_number))
			current_number = ''

	return lijst_waarden

def dereform(string):
	waarden = string_naar_lijst(string)
	matrix_1 = [ [waarden[i] for i in range(4)], [waarden[i] for i in range(4, 8)], [waarden[i] for i in range(8, 12)], [waarden[i] for i in range(12, 16)] ]
	counter = waarden[16]
	matrix_2 = [ [waarden[i] for i in range(17, 21)], [waarden[i] for i in range(21, 25)], [waarden[i] for i in range(25, 29)], [waarden[i] for i in range(29, 33)] ]

	return (matrix_1, counter, matrix_2)

while True:
	data = str(ser.read(),'utf-8')
	if data == ':':			#zorgt voor start met :
		while True:
			data = str(ser.read(),'utf-8')
			if data != ':':
				message += data
			else:
				message += data
				dereformed_message = dereform(message)
				#print ('deref ', dereformed_message)
				current_counter = dereformed_message[1]
				decrypted_message = Decryptie.Ontcijfering(dereformed_message)
				#print (decrypted_message)
				message = ''
				if decrypted_message!=None and (current_counter > last_counter):
					for i in range(0, 12):
						print(str(decrypted_message[i]) + '\n')
						os.write(ekgfile, str(decrypted_message[i]).encode('utf-8') + b'\n')
					for i in range(12, 16):
						print(str(decrypted_message[i]) + '\n')
						os.write(pofile, str(decrypted_message[i]).encode('utf-8') + b'\n')
					last_counter = current_counter
				else:
					print ('PROBLEEM PROBLEEM PROBLEEM PROBLEEM')
					print (decrypted_message)
					print (current_counter, last_counter)
