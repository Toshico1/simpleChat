import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9092))
sock.listen(20)


list_of_conn = []


class client_info():
	def __init__(self, conn, add):
		self.conn = conn
		self.add = add
		self.data: bytes
		self.th = threading.Thread(target=self.send_circle)
		self.th.start()

	def send_circle(self):
		while True:
			self.conn.setblocking(True)
			self.data = self.conn.recv(1024)
			for client in list_of_conn:
				client.conn.send(self.data)



def s_acc():
	while True:
		conn, add = sock.accept()
		print("lol")
		list_of_conn.append(client_info(conn, add))


th = threading.Thread(target=s_acc)
th.start()

while True:
	try:
		pass
	except KeyboardInterrupt:
		sock.close()
		break


