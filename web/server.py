import socket
import datetime

IP = '127.0.0.1'
PORT = 8000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((IP, PORT))
    sock.listen(1)
    print(f'Accepting incoming connection on port {PORT}')
    conn, addr = sock.accept()
    with conn:
        print('Connected by', addr)
        now = datetime.datetime.now()
        while True:
            data = conn.recv(1024)
            if data == b'day':
                d = '{:02d}'.format(now.day)
            elif data == b'month':
                d = '{:02d}'.format(now.month)
            elif data == b'year':
                d = '{:02d}'.format(now.year)

            elif data == b'time':
                d = '{:02d}'.format(now.hour), '-', '{:02d}'.format(now.minute)
            elif data == b'exit':
                break
            else:
                d = 'Incorrect command'
            conn.sendall(d.encode())
