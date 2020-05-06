import socket
import subprocess
from Handler import Handler

def receiver(conn):
        while True:
            request = conn.recv(4096)
            Handler(request)
            data = "received"
            conn.send(data)

def sub_server(address, backlog=1):
    try:
        s = socket.socket()
        s.bind(address)
        s.listen(backlog)
        print("server on, listening...")
    except socket.error as error:
        print("error, re-starting the server")
        print(error)
        sub_server(address, backlog=1)
    conn, client_address = s.accept()
    print("connection to the server stable:", client_address)
    receiver(conn)

if __name__ == '__main__':
    sub_server(("",15000))
