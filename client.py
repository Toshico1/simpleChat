import socket
import tkinter as tk 
import threading as th

class window():
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(('', 8888))

		self.mainwindow = tk.Tk()
		self.mainwindow.title('Chat v0.1')
		self.chat_list = tk.Listbox()
		self.text_box = tk.Text(height = 1, width = 10)
		self.send_button = tk.Button(text = 'Send', command = self.send_data)
		self.conn_button = tk.Button(text='Connect', command = self.get_conn)

		self.text_box.grid(row=1, column=0)
		self.chat_list.grid(row=0, )
		self.send_button.grid(row=1, column=1)
		self.conn_button.grid(row=1, column=2)
		self.mainwindow.mainloop()

	def send_data(self):
		self.txt = self.text_box.get("1.0",'end-1c')
		self.sock.send(bytes(self.txt, 'utf-8'))

	def recv_data(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data != 0:
					print(data.decode('utf-8'))
					self.chat_list.insert(self.chat_list.size(), data.decode('utf-8'))
			except socket.error:
				self.send_data()

	def get_conn(self):
		try:
			self.sock.connect(('127.0.0.1', 9092))
		except Exception:
			self.chat_list.insert(self.chat_list.size(), 'Connection failed')
			self.sock.close()
		else:
			self.chat_list.insert(self.chat_list.size(), 'Connection succed')
			self.sock.send(b'I am there!')
			self.recv_thread = th.Thread(target=self.recv_data)
			self.recv_thread.start()



window()
