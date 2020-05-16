import socket
import json
global client
def connect(b,address, port_number):
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((address, int(port_number)))
    while True:
        print("Connecting to the game server...")
        create_board_ui(b)
        send_info_to_server(b)
        data = client.recv(1024)
        data1 = json.loads(data.decode())
        b=data1.get("board")
        w=data1.get("win")
        if w!="":
            break
        print(data1)

def create_board_ui(b):
    print(b[0][0] + " | " + b[0][1] + " | " + b[0][2] + " | ")
    print("-------------")
    print(b[1][0] + " | " + b[1][1] + " | " + b[1][2] + " | ")
    print("-------------")
    print(b[2][0] + " | " + b[2][1] + " | " + b[2][2] + " | ")
    print("")
    print("")
def input_coordinats():
    inp = input("select a place of the board, for ex.(1,1): ")
    return [int(i) for i in inp.split(',')]
def send_info_to_server(b):
    input_data=input_coordinats()
    data = json.dumps({"board": b, "row": input_data[0],"col": input_data[1],"exception":"","win":False})
    client.send(data.encode())
def main():
    ip_addr='127.0.1.1'
    port= 8000
    b = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    connect(b,ip_addr,port)

if __name__ == "__main__":
    main()