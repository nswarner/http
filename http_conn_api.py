#!/usr/bin/python3

class HTTP_CONN_API:

	def __init__(self):
		pass

	def __del__(self):
		pass

	def request(self, URL, port, json):

		self.sock = socket.socet(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((URL, port))
		length = len(json)
		sent = 0
		counter = 0

		try:
			while(sent < length):
				sent += self.sock.send(msg[sent:])
				if (sent == 0):
					print("Finished sending. Awaiting reply.")	
				counter += 1
				if (counter >= 200):
					raise RuntimeError("Counter >= 200. Ending loop.")
		except RuntimeError as err:
			print(err)


if (__name__ == '__main__'):
	print("Running HTTP_CONN_API.")
	URL = input("URL: ")
	port = input("Port: ")
	json = input("JSON String: ")
	http = HTTP_CONN_API()
	http.request(URL, port, json)
