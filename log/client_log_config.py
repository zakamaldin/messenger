import logging
import os
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
CLIENT_LOG_FOLDER = os.path.join(ABS_PATH, 'client_logs')

# логгер
client_logger = logging.getLogger('client')
client_logger.setLevel(logging.INFO)
# хэндлер всего
client_handler = logging.FileHandler(os.path.join(CLIENT_LOG_FOLDER, 'client.log'), encoding='utf-8')
client_handler.setLevel(logging.INFO)
# хэндлер ошибок
client_error_handler = logging.FileHandler(os.path.join(CLIENT_LOG_FOLDER, 'client_error.log'), encoding='utf-8')
client_error_handler.setLevel(logging.ERROR)

client_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

client_handler.setFormatter(client_formatter)
client_error_handler.setFormatter(client_formatter)

client_logger.addHandler(client_handler)
client_logger.addHandler(client_error_handler)
