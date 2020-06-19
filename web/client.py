import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    user_says = input('Input command: ')
    client.sendall(user_says.encode())
    data = client.recv(1024)
    if user_says == 'exit':
        break
    print(data.decode())

client.shutdown(socket.SHUT_RDWR)
client.close()
