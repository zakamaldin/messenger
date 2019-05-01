from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import dict_to_bytes, byte_to_dict


class Server:

    def __init__(self):
        self.server = socket(AF_INET, SOCK_STREAM)

    def run_server(self, ip='', port=7777):
        self.server.bind((ip, port))
        self.server.listen(5)
        self.client, self.addr = self.server.accept()
        print('Получен запрос на соединение от:', self.addr)
        while True:
            message = self.get_message()
            print(message)
            if not 'action' in message:
                self.send_message(400, 'Incorrect response')

            if message['action'] == 'presence':
                self.send_message()

            if message['action'] == 'msg':
                self.send_message()

    def get_message(self):
        message = self.client.recv(1024)
        return byte_to_dict(message)

    def send_message(self, code=200, alert='OK'):
        packet = {
            'response': code,
            'alert': alert
        }
        self.client.send(dict_to_bytes(packet))


server = Server()
server.run_server()
