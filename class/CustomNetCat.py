import socket
## Hre's the documentation :https://www.gnu.org/software/libc/manual/html_node/Socket_002dLevel-Options.html#Socket_002dLevel-Options
class NetCat:
	"""
	Custom Netcat :v
	"""
	def __init__(self, args, buffer=None):
		self.args = args # args is the object returned by parser.parse_args() 
		self.buffer = buffer # All commands that are written by you will be stored in buffer
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket for TCP connection
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Intinya Ini bisa Menggunakan ADDR yang sama ( SOL_SCOKET maksudnya biar bisa setting SO_REUSEADDR)
	def run(self):
		if self.args.listen:
			self.listen()
		else:
			self.send()

	def send(self):
		self.socket.connect((self.args.target, self.args.port))	# Connect to target
		if self.buffer: # if not empty
			self.socket.send(self.buffer) # Kirim buffernya ke target ( Buffer ini command yang sebelumnya dibuat oleh heker)
		
		try:
			while True:
				recv_len = 1
				response = ""
				while recv_len:
					# Inti di while loop ini ngambil semua data yang masuk dari socket :v
					data = self.socket.recv(4096) # Batas Maksimal Data yang masuk ( Keknya ini Bytes deh wkwkk)
					recv_len = len(data)
					response = response + data.decode()
					if recv_len < 4096: # Nanti si recv_len bisa < 4096 ( Karena pasti ada sisa di network itu) dan itu pasti data terakhir
						break
				if response:
					print(response)
					buffer = input("> ")
					buffer += "\n"
					self.socket.send(buffer.encode())
		except KeyboardInterrupt:
			print("Keyboard Intterupt")
			self.socket.close()
			sys.exit()

	def listen(self) :
		"""
		ExECUTE As A LISTENER ( DO YOU KNOW LISTENEr RIGHT ?)
		"""
		self.socket.bind((self.args.target, self.args.port))
		self.socket.listen(5) # Listen 5 request

		while True:
			client_socket, _ = self.socket.accept()
			client_handler = threading.Thread(target= self.handle, args=(client_socket))
			client_handler.start()

	def handle(self, client_socket):
		"""
		All operations we will do to the target
		will run on background ( TODO : Make the implementation of this function)
		"""

		if self.args.execute:
			pass
		elif self.args.upload:
			pass
		elif self.args.command:
			pass
		else:
			pass

