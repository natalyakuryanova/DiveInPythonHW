# -*- coding: utf8 -*-
import argparse

# Создание парсера аргументов
parser = argparse.ArgumentParser(prog='ArgParse',
                                 description='Процессинг числа и строки с опциями.',
                                 epilog="That's it.",
                                 prefix_chars='-/')

# Добавление обязательных аргументов
parser.add_argument('number', type=int, help='Число для вывода')
parser.add_argument('text', type=str, help='Строка для вывода')

# Добавление опций
parser.add_argument('-v', '/v', '--verbose', action='store_true', help='Вывод дополнительной информации')
parser.add_argument('-r', '/r', '--repeat', type=int, default=1, help='Количество повторений строки (default: 1)')

# Парсинг аргументов
args = parser.parse_args()

# Вывод дополнительной информации, если опция verbose установлена
if args.verbose:
    print(f'Полученные аргументы: number={args.number}, text="{args.text}", repeat={args.repeat}')

# Вывод строки, повторенной указанное количество раз
print(f'Число: {args.number},\nСтрока: {(args.text+"\n") * args.repeat}')
