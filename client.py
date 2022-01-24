import socket
import json
import os


HOST, PORT = 'localhost', 8080

class Sender:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

    def send_data(self):
        data = 'new_file.txt'
        self.client.sendall(data.encode('utf-8'))
        received_data = self.client.recv(1024).decode('utf-8')
        print(received_data)

    def close(self):
        self.client.close()


if __name__ == '__main__':
    client = Sender()
    client.send_data()
    client.close()