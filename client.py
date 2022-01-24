import socket
import json
import os


HOST, PORT = 'localhost', 8080

class Sender:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

    def send_data(self):
        request_text = (
            b'GET /index.html HTTP/1.1\r\n'
            b'Host: cm.bell-labs.com\r\n'
            b'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n'
            b'Accept: text/html;q=0.9,text/plain\r\n'
            b'\r\n'
        )

        self.client.sendall(request_text)
        received_data = self.client.recv(1024).decode('utf-8')
        print(received_data)

    def close(self):
        self.client.close()


if __name__ == '__main__':
    client = Sender()
    client.send_data()
    client.close()