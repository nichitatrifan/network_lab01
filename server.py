import socket
import sys
import os
import logging

from datetime import datetime


class Logger:
    def __init__(self) -> None:
        logging.basicConfig()
        self.logger = logging.getLogger('TCPLogger')
        self.logger.setLevel(logging.INFO)


def handle_client(client_socket, addr, logger:Logger):
    date_obj = datetime.now()
    date = str(date_obj.day) + '_' + str(date_obj.month)  + \
            '_' + str(date_obj.year) + '_' + str(date_obj.hour) + '_' + str(date_obj.minute) +\
            '_' + str(date_obj.second)
    
    request = client_socket.recv(1024).decode('utf-8')
    headers = request.split('\n')
    get_resource = headers[0].split(' ')[1]
    resource_path = os.path.abspath(os.getcwd()).replace('\\','/') + get_resource

    logger.logger.info(headers[0])
    logger.logger.info('[SERVER] resource requested: ' + str(get_resource))
    logger.logger.info('[SERVER] resource path: ' + str(resource_path))
    
    try:
        with open(resource_path, 'r') as resource:
            resource_text = resource.read()
        status_code = '200 OK'

    except FileNotFoundError as fne:
        logger.logger.warning('[SERVER] Resource Not Found!')
        status_code = '404 Not Found'
        with open('file_not_found_404.html', 'r') as file_404:
            resource_text = file_404.read()

    except Exception as ex:
        logger.logger.warning(' [SERVER] Something went wrong!')
        logger.logger.warning(' [SERVER] Exception: ' + str(ex))
        status_code = '400 Bad Request'
        with open('bad_request_400.html', 'r') as file_400:
            resource_text = file_400.read()
        
    
    content_len = len(resource_text.encode('utf-8'))
    response = f'HTTP/1.1 {status_code}\r\n' +\
        f'Date: {date}\r\n' +\
        'Server: localhost\r\n' +\
        f'Content-Length: {content_len}\r\n' +\
        'Connection: Closed\r\n' +\
        'Content-Type: text/html\r\n'+\
        '\r\n' # need an empty line in between headers and data
    
    response += resource_text
    client_socket.sendall(response.encode('utf-8'))
    

if __name__ == '__main__':
    logger = Logger()

    if len(sys.argv) > 1:

        if sys.argv[1] in ('-h', '--help'):
            print(f'Usage: {sys.argv[0]}')
            sys.exit(0)
        else:
            PORT = int(sys.argv[1])
            HOST = 'localhost'
    else:
        HOST, PORT = 'localhost', 8080

    with socket.create_server(address=(HOST, PORT), family=socket.AF_INET) as server:
        server.listen()
        server.settimeout(5.0)
        
        try:
            try:
                addr = server.getsockname()
                logger.logger.info(f' [SERVER] listens on {addr}')
                client_socket, addr = server.accept()
                logger.logger.info(f' [SERVER] socket with addr: {addr} connected')
                handle_client(client_socket, addr, logger)

            except TimeoutError as te:
                logger.logger.warning(' [SERVER] Timeout Reached!')

        except KeyboardInterrupt as kyi:
            logger.logger.warning(' [SERVER] Keyboard Interrupt')
            server.close()
