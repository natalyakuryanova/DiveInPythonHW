# -*- coding: utf8 -*-

import os
import logging
from collections import namedtuple
import argparse

# Определение namedtuple для хранения информации о файле/каталоге
DirFileInfo = namedtuple('DirFileInfo', ['name',
                                                             'extension',
                                                             'is_directory',
                                                             'parent_directory'])

# Настройка логирования
logging.basicConfig(filename='dir_contents.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def collect_info(dir):
    """
    Собирает информацию о содержимом директории и сохраняет в лог.

    :param dir: Полный путь до папки
    :return: Ничего не возвращает. Записывает содержимое папки в txt лог

    """

    if not os.path.isdir(dir):
        raise ValueError(f"Указанный путь {dir} не является директорией.")

    # Получаем родительский каталог
    pdir = os.path.basename(os.path.abspath(dir))

    # Перебираем содержимое директории
    for entry in os.listdir(dir):
        entry_path = os.path.join(dir, entry)

        # Проверяем, является ли элемент директорией
        if os.path.isdir(entry_path):
            dir_file_info = DirFileInfo(name=entry,
                                        extension=None,
                                        is_directory=True,
                                        parent_directory=pdir)
        else:
            (name, extension) = os.path.splitext(entry)
            dir_file_info = DirFileInfo(name=name,
                                        extension=extension.lstrip('.'),
                                        is_directory=False,
                                        parent_directory=pdir)

        # Запись в лог
        logging.info(f'{dir_file_info.name} | '
                     f'{dir_file_info.extension if dir_file_info.extension else "N/A"} | '
                     f'{"Directory" if dir_file_info.is_directory else "File"} | '
                     f'{dir_file_info.parent_directory}')


parser = argparse.ArgumentParser(description="Сбор информации о содержимом директории и запись в лог.")

parser.add_argument('directory', type=str, help="Путь до директории для анализа")
args = parser.parse_args()

dir_path = args.directory

try:
    collect_info(dir_path)
    print(f'Информация о содержимом директории "{dir_path}" успешно добавлена в файл "dir_contents.log".')
except ValueError as e:
    print(e)
