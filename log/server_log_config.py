import logging.handlers
import os

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
SERVER_LOG_FOLDER = os.path.join(ABS_PATH, 'server_logs')

server_logger = logging.getLogger('server')
# хэндлер всёего
server_handler = logging.handlers.TimedRotatingFileHandler(
    os.path.join(SERVER_LOG_FOLDER, 'server.log'),
    encoding='utf-8',
    when='d'
)
# хэндлер ошибок
server_error_handler = logging.FileHandler(
    os.path.join(SERVER_LOG_FOLDER, 'server_error.log'),
    encoding='utf-8'
)
server_error_handler.setLevel(logging.ERROR)

server_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

server_handler.setFormatter(server_formatter)

server_logger.addHandler(server_handler)
server_logger.addHandler(server_error_handler)

server_logger.setLevel(logging.INFO)
