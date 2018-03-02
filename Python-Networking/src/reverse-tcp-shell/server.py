import socket
import sys

# Create socket
def socket_create():
	try:
		global host
		global port
		global s
		host = 'localhost'
		port = 9997
		s = socket.socket()
	except socket.error as msg:
		print("Socket creation error: " + str(msg))

# Bind socket to port
def socket_bind():
	try:
		global host
		global port
		global s
		print("Binding socket to port: " + str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		socket_bind()

# Establish a connection with client (socket must be listening)
def socket_accept():
	conn, address = s.accept()
	print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
	send_commands(conn)
	conn.close()

# Send Commands
def send_commands(conn):
	while True:
		cmd = input()
		if cmd == "quit":
			conn.close()
			s.close()
			sys.exit()
			break
		if len(str.encode(cmd)) > 0:
			# Encoding is always necessary when sending over network
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(2048), "utf-8")
			print(client_response, end="")

def main():
	socket_create()
	socket_bind()
	socket_accept()

if __name__ == "__main__":
	main()