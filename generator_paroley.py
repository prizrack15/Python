from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def generaciya(chars):
    cyfri = input('Включать ли цифры 0123456789 в пароль (да/нет)\n')
    propisy = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (да/нет)\n')
    strocnye = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz (да/нет)\n')
    symvoly = input('Включать ли символы !#$%&*+-=?@^_ (да/нет)\n')
    neod_symvoly = input('Исключать ли неоднозначные символы il1Lo0O ? (да/нет)\n')
    if cyfri.lower() == 'да':
        chars += digits
    if propisy.lower() == 'да':
        chars += uppercase_letters
    if strocnye.lower() == 'да':
        chars += lowercase_letters
    if symvoly.lower() == 'да':
        chars += punctuation
    if neod_symvoly.lower() == 'да':
        for i in 'il1Lo0O':
            chars = chars.replace(i, '')
    kolichestvo_parolei(chars, kol_paroley)

def kolichestvo_parolei(chars, kol_paroley):
    for _ in range(kol_paroley):
        sozdanie_parolya(dlina_parolya, chars)

def sozdanie_parolya(dlina_parolya, chars):
    parol = ''
    for _ in range(dlina_parolya):
        parol += choice(chars)
    print(parol, len(parol))


chars = ''
kol_paroley = int(input('Укажите количество паролей\n'))
dlina_parolya = int(input('Укажите длину одного пароля\n'))

generaciya(chars)



















