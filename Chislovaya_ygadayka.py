from random import *


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100


def preparation():
    while True:
        polzov = input()
        if is_valid(polzov):
            return int(polzov)
        else:
            print('Нужно ввести число от 1 до 100?')

def continue_game():
    zapros = input('Ещё раз? Да или Нет\n')
    while True:
        if zapros == 'Да':
            return True
        elif zapros == 'Нет':
            return False
        else:
            print('Введите Да или Нет')
            zapros = input()

def sama_igra():
    print('Введите число от 1 до 100')
    kek = randint(1, 100)
    total = 1
    while True:
        polzov = preparation()
        if kek > polzov:
            print('Слишком мало, попробуйте еще раз')
            total += 1
        elif kek < polzov:
            print('Слишком много, попробуйте еще раз')
            total += 1
        elif kek == polzov:
            print('Молодец.' f'Ты угадал с {total} попытки')
            break


def game():
    print('Добро пожаловать в числовую угадайку')
    while True:
        sama_igra()
        if continue_game():
            continue
        else:
            break

game()


















