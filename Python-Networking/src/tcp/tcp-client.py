import socket

target_host = "www.rgabrielflores.com"
target_port = 80

def main():
	# Create Socket Object
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect to the client
	client.connect((target_host,target_port))
	# Send Data
	client.send("GET / HTTP/1.1\r\nHost: rgabrielflores.com\r\n\r\n".encode())
	# Receive Data
	response = client.recv(4096)

	print(response)

if __name__ == "__main__":
	main()