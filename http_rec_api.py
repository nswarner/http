#!/usr/bin/python3

class HTTP_REC_API:

	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __del__(self):
		pass

	def listen(host, port):
		self.sock.connect((host, port))
		received_part = []
		received_amt = 0
		size = 0
		tmp = ""
		while(received_amt < 20):
			tmp += self.sock.recv(20)
			received_amt += len(tmp)
			received_part.append(tmp)
		received_amt = 0
		str_expected = ''.join(received_part)
		num_expected = int(str_expected)
		received_part = []

		while(bytes_recd < num_expected):
			received_part.append(self.sock.recv())
			

if (__name__ == '__main__'):
	print("Running HTTP_REC_API.")
	http = HTTP_REC_API()
	http.listen('127.0.0.1', 80)
