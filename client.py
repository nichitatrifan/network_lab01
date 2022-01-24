import socket
import json
import os
import string
import datetime


HOST, PORT = 'localhost', 9999

class Sender:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

    def send_data(self):
        data = 'Hi'
        self.client.sendall(data.encode())

    def close(self):
        self.client.close()


if __name__ == '__main__':
    client = Sender()
    client.send_data()
    client.close()