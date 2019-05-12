from server import Server
import socket
import unittest


class TestServer(unittest.TestCase):

    def setUp(self) -> None:
        self.server = Server()

    # Уходит в бесконечный запуск
    def test_server_create(self):
        self.assertEqual(type(self.server), socket.socket)

