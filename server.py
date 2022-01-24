import socket
import sys


def handle_client(client_socket, addr):
    file_name = client_socket.recv(1024).decode('utf-8')
    print('Received file name: ' + str(file_name))
    response = 'Accepted'
    client_socket.sendall(response.encode('utf-8'))


if __name__ == '__main__':
    HOST, PORT = 'localhost', 8080

    with socket.create_server(address=(HOST, PORT), family=socket.AF_INET) as server:
        server.listen()
        server.settimeout(5.0)
        
        try:
            try:
                print('Socket waits for a connection... ')
                client_socket, addr = server.accept()
                handle_client(client_socket, addr)
                print(f'socket with addr: {addr} connected')
            except TimeoutError as te:
                print('Timeout reached!')
        except KeyboardInterrupt as kyi:
            print('Keyboard Interrupt')
            server.close()