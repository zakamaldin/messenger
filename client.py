from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import dict_to_bytes, byte_to_dict
import time


class User:

    def __init__(self, name='Guest'):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.name = name

    def connect(self, ip='127.0.0.1', port=7777):
        self.client.connect((ip, port))
        packet = {
            'action': 'presence',
            'time': time.time()
        }
        self.send_packet(packet)
        response = self.get_message()
        print(response)
        if not response['response'] == 200:
            raise Exception('Connection Error')
        return response

    def send_message(self, to=None, msg=None):
        if to is not None and msg is not None:
            packet = {
                'action': 'msg',
                'time': time.time(),
                'from': self.name,
                'to': to,
                'msg': msg
                }
            self.send_packet(packet)
        else:
            raise Exception('Incorrect args')

    def get_message(self):
        message = self.client.recv(1024)
        return byte_to_dict(message)

    def send_packet(self, packet):
        self.client.send(dict_to_bytes(packet))

    def disconnect(self):
        self.client.close()


user1 = User('DrZak')
# user1.connect()
# while True:
#     time.sleep(1)
#     user1.send_message('admin', 'RTFM')
#     message = user1.get_message()
#     print(message)

