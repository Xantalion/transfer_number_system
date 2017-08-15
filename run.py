'''
Пример:
перевод десятеричного числа 10: python run.py -dec 10
перевод двоичного числа 0110: python run.py -bin 0110
перевод двоичного числа с пробелом 0110 1001: python run.py -bin "0110 1001"
перевод восьмиричного  числа 45: python run.py -oct 45
перевод шеснадцатиричного числа 2b3c : python run.py -hex 2b3c
'''
__author__ = "Xantalion"
__version__ = "1.0.0"
__email__ = "xantalion@mail.ru"

import sys
import argparse
            
# Переводим число в другую систему исчисления 2, 8, 16, 10
def tns(n, ins, outs):
    n = n.replace(" ", "")
    n = int(n, ins)
    if outs == 2:
        return bin(n).lstrip("0b")
    elif outs == 8:
        return oct(n).lstrip("0o")
    elif outs == 10:
        return str(n)
    elif outs == 16:
        return hex(n).lstrip("0x")
    else:
        return 0

# Вывод результата
def res(n, ins):
    print("bin: " + tns(n, ins, 2))
    print("oct: " + tns(n, ins, 8))
    print("hex: " + tns(n, ins, 16))
    print("dec: " + tns(n, ins, 10))

# Задаем настройки парсера ключей
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-bin', type=str, help='двоичная система ввода')
    parser.add_argument('-oct', type=str, help='восьмиричная система ввода')
    parser.add_argument('-hex', type=str, help='шеснадцатиричная система ввода')
    parser.add_argument('-dec', type=str, help='десятеричная система ввода')
    return parser

# Считываем первый ключ и его значение
def first_item_parser():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:3])
    return namespace

# Посдтавляем первое значение ключа в функцию
def run():
    try:
        namespace = first_item_parser()
        if namespace.bin:
            res(namespace.bin, 2)
        elif namespace.oct:
            res(namespace.oct, 8)
        elif namespace.hex:
            res(namespace.hex, 16)
        elif namespace.dec:
            res(namespace.dec, 10)
    except ValueError:
        print ("Неверное значение системы счисления", sys.exc_info()[1])

if __name__ == "__main__":
    run()
