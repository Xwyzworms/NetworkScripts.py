"""
	Script for creating TCP Garbage, sending dummy data to a server.	
	"""

import socket 


targetHost : str = "YOUR IP"
targetPort : int = 9997

# Create A Socket
# AF_INET = Address Family, IPv4
# SOCK_STREAM = TCP
# SOCK_DGRAM = UDP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the TArget

client.connect((targetHost, targetPort))
#Send data using byte
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive data
response = client.recv(4096)

print(response.decode())

client.close()