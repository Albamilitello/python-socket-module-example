import socket
import sys

def send_instructions(s):
    while True:
        instruction = input(">")
        if instrucyion == "ESC":
            print("closing the connection with the server")
            s.close()
            sys.exit()
        else:
            s.send(instruction.encode())
            data = s.recv(4096)
            print(str(data,"utf-8"))

def conn_sub_server(server_address):
    try:
        s = socket.socket()
        s.connect(server_address)
        print("Connection with the server stable:", indirizzo_server)
    except socket.error as error:
        print("error:")
        print(error)
        sys.exit()
    send_instructions(s)

if __name__ == '__main__':
    conn_sub_server(("YOUR IP HERE", 15000))
