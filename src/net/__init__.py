import threading
import json
from socket import *

BUFFER_SIZE = 4096

HOST_ADDRESS = ""
PORT = 8008

TARGET_ADDRESS = "localhost"

SERVER_PREFIX = "[SERVER]"
CLIENT_PREFIX = "[CLIENT]"

class GameNetwork(threading.Thread):

	def MakeServer():
		server = GameNetwork()
		server.type = "server"
		return server

	def MakeClient():
		client = GameNetwork()
		server.type = "client"
		return client

	def __init__(self):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.running = True

	def init_server(self):
		s = socket(AF_INET, SOCK_STREAM)
		s.bind((HOST_ADDRESS, PORT))
		s.listen(2)
		print(SERVER_PREFIX, "Waiting for connection")
		self.socket, addr = s.accept()
		print(SERVER_PREFIX, "Connected with", addr)

	def init_client(self):
		self.socket = socket(AF_INET, SOCK_STREAM)
		print(CLIENT_PREFIX, "Attemping connection")
		self.socket.connect((TARGET_ADDRESS, PORT))
		print(CLIENT_PREFIX, "Connection Successful. Connected to", (TARGET_ADDRESS, PORT))

	def run(self):
		if self.type == "server":
			self.init_server()
		elif self.type == "client":
			self.init_client()
		else:
			return

		while self.running:
			pack = self.socket.recv(BUFFER_SIZE)
			try:
				data = json.loads(pack.decode("utf-8"))
			except ValueError as e:
				print("Invald packet format:\n", pack.decode("utf-8"))
				continue
			getattr(self, data[0])(data[1::])

	def print_data(self, data):
		print(data)