from client import User
import socket
import unittest


class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.user = User('TestUser')

    def test_client_name(self):
        self.assertEqual(self.user.name, 'TestUser')

    def test_socket_creating(self):
        self.assertEqual(type(self.user.client), socket.socket)

    # Как проверять такие функции? Exception вылетает только в случает если соединение
    # не удалось установить, а если удалось, то тест проваливается
    def test_connect(self):
        with self.assertRaises(ConnectionRefusedError):
            self.user.connect()
        # Можно ли за один заход проверить вернул ли метод Exception
        # или что-то, что можно проверить следующим тестом
        # self.assertEqual(self.user.connect(), {'response': 200, 'alert': 'OK'})


if __name__ == "__main__":
    unittest.main()