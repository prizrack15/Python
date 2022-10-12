def calculator(n, d):
    print('Введите одну из следующих математических операций: + - * / % // **. ',
          'Введите R, если хотите поменять числа местами или N, чтобы ввести новые', sep='\n')
    chel = input()
    while True:
        if chel == 'R':
            n, d = d, n
            chel = input()
        if chel == 'N':
            print('Новые числа:')
            n, d = int(input()), int(input())
            print('Математическая операция:')
            chel = input()
        if chel == '+':
            print(n + d)
            chel = input()
        elif chel == '-':
            print(n - d)
            chel = input()
        elif chel == '*':
            print(n * d)
            chel = input()
        elif chel == '/':
            print(n / d)
            chel = input()
        elif chel == '%':
            print(n % d)
            chel = input()
        elif chel == '//':
            print(n // d)
            chel = input()
        elif chel == '**':
            print(n ** d)
            chel = input()
        elif chel == '.':
            return 'Пока'
        else:
            print('Введите одну из следующих математических '
                  'операций: + - * / % // **')
            chel = input()

print('Добро пожаловать в мини-калькулятор.', 'Введи любые два числа:', sep='\n')

n, d = int(input()), int(input())
print(calculator(n, d))

