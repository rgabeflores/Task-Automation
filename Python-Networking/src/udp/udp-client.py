import socket

target_host = "127.0.0.1"
target_port = 80

def main():
	# Create Socket Object
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Send Data
	client.sendto("AAABBBCCC".encode(), (target_host, target_port))
	# Receive Data
	data, addr = client.recvfrom(4096)

	print(data)

if __name__ == "__main__":
	main()