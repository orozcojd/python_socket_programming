import socket

target_host = "0.0.0.0"
target_port = 9999

#AF_INET indicates using standard ipv4 address
#SOCK_STREAM indicates this will be TCP client

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send("hello there buddy!", (target_host, target_port))

response = client.recv(4096)

print response

