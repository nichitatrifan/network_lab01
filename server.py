import socket
import sys
import os


def handle_client(client_socket, addr):
    request = client_socket.recv(1024).decode('utf-8')
    headers = request.split('\n')
    get_resource = headers[0].split(' ')[1]
    resource_path = os.path.abspath(os.getcwd()).replace('\\','/') + get_resource

    print(headers[0])
    print('resource path: ' + str(resource_path))

    response = 'HTTP/1.1 200 OK\r\n' +\
        'Date:\r\n' +\
        'Server: localhost\r\n' +\
        'Content-Length: 1024\r\n' +\
        'Connection: Closed\r\n' +\
        'Content-Type: text/html\r\n'+\
        '\r\n' # need an empty line in between headers and data
    
    try:
        with open(resource_path, 'r') as resource:
            resource_text = resource.read()
            response += resource_text
    except FileNotFoundError as fne:
        print('Resource Not Found!')
        response += 'None'

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