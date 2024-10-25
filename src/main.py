from src.logger import Logger
from level_enum import Level
from threading import Thread
from faker import Faker
from pathlib import Path
import random
import os
import time

fake = Faker()

path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(path, '..'))
base_path = Path(parent_path)
file_path = base_path / "logs"


def thread_func():
    """Создаёт в нескольких потоках логгеры и записывает в них сообщения"""
    for i in range(3):
        logger = Logger(dir_path=file_path)

        message = fake.text(max_nb_chars=20)
        level = random.choice(list(Level))

        logger.log(message, level)
        time.sleep(random.randrange(0, 2))


if __name__ == "__main__":
    threads = []
    for _ in range(10):
        thread = Thread(target=thread_func, args=())
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


