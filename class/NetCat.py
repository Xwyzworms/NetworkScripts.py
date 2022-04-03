import socket
class NetCat:
	def __init__(self, args, buffer=None):
		self.args = args
		self.buffer = buffer
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
