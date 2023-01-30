import socket
import random

while(True):
	random_ports = [100, 101, 102, 103, 104, 105, 106, 987, 432, 654]

	UDP_IP = "159.253.42.6"
	UDP_PORT = random.choice(random_ports)
	MESSAGE = b"ping 127.0.0.1"

	print("Target IP: " + UDP_IP)
	print("Target Port: " + str(UDP_PORT))

	sock = socket.socket(socket.AF_INET,
				socket.SOCK_DGRAM)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
