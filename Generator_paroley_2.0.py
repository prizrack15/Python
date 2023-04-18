from random import *
from string import *
def generate_password(length):
    kek = (ascii_letters + (digits))
    for i in 'lI1oO0':
        kek = kek.replace(i, '')
    lol = [choice(kek[:24])] + [choice(kek[24:48])]\
          + [choice(kek[49:])] + sample(kek, m - 3)
    shuffle(lol)
    lol = (''.join(str(i) for i in lol))
    return lol

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')




