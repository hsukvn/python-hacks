import socket

target_host = "localhost"
target_port = 9999

# AF_INET: ipv4, SOCK_STREAM: TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send("hello~")

response = client.recv(4096)

print response
