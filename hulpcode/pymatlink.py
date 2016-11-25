import socket

sock = socket.socket(socket.AF_INET, socket.DGRAM)
sock.bind(('', 5000))

