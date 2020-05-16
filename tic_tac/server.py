import socket
import json
import random
def check_valid_info(r,c):
    if r in range(1,4) and c in range(1,4):
        return True
    else:
        return False
def client_new_pos(arr,r,c):
    arr[r-1][c-1] = "X"
    return arr
def gen_new_pos(arr):
    while True:
        r=random.randint(0,2)
        c=random.randint(0,2)
        if arr[r][c]==" ":
            arr[r][c]="O"
            break
    return arr
def check_win(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " " or board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != " " or board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != " ":
        return True
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != " " or board[0][1] == board[1][1] and board[1][1] == \
            board[2][1] and board[2][1] != " " or board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != " ":
        return True
    elif board[0][0] == board[1][1] and board[2][2] == board[1][1] and board[0][0] != " " or board[0][2] == board[1][1] and board[1][1] == \
            board[2][0] and board[0][2] != " ":
        return True
def connect(IP,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((IP, PORT))
        sock.listen(1)
        print(f'Accepting incoming connection on port {PORT}')
        conn, addr = sock.accept()
        with conn:
            data = conn.recv(1024)
            data = json.loads(data.decode())
            arr = data.get("board")
            row = data.get("row")
            col=data.get("col")
            w = ""  # winer is noone
            print(data)
            if check_valid_info(row,col): #is coordinats from client is valid
                arr=client_new_pos(arr,row,col)
                if check_win(arr): # if client winn
                    w = "Client Win"
                else:
                    arr = gen_new_pos(arr)  # new pos from server
                    if check_win(arr): #if server win
                        w = "Server Win"
                d=""
            else:
                d = "Error of input"
            data = json.dumps({"board": arr, "row": row,"col": col,"exception":d,"win":w})
            print("dataa2",data)
            conn.sendall(data.encode())


def main():
    ip_addr='127.0.1.1'
    port= 8000
    connect(ip_addr,port)

if __name__ == "__main__":
    main()