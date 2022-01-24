import socket
import sys

def handle_client(client_socket, addr):
    pass


if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST,PORT))
        server.listen()
        # add timeout
        
        try:
            print('Socket waits for a connection... ')
            client_socket, addr = server.accept()
            print(f'socket with addr: {addr} connected')
        except KeyboardInterrupt as kyi:
            server.close()