propis_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

propis_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
stroch_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
isklyucheniya = '!#$%&*+-=?@^_0123456789,.""'''



s = input('Введите текст\n').split()
sdvig = input('шаг сдвига: влево или вправо(вл/вп)\n')
res = ''
for i in range(len(s)):
    for j in range(len(s[i])):
        dlina_slova = ''
        for k in range(len(s[i])):
            if s[i][k] not in isklyucheniya:
                dlina_slova += s[i][j]


        if s[i][j] in propis_eng:
            if sdvig == 'вл' and propis_eng.find(s[i][j]) - len(dlina_slova) < 0:
                res += propis_eng[propis_eng.find(s[i][j]) - len(dlina_slova) + 26]
            elif sdvig == 'вп' and propis_eng.find(s[i][j]) + len(dlina_slova) > 25:
                res += propis_eng[propis_eng.find(s[i][j]) + len(dlina_slova) - 26]
            elif sdvig == 'вл':
                res += propis_eng[propis_eng.find(s[i][j]) - len(dlina_slova)]
            elif sdvig == 'вп':
                res += propis_eng[propis_eng.find(s[i][j]) + len(dlina_slova)]


        if s[i][j] in propis_rus:
            if sdvig == 'вл' and propis_rus.find(s[i][j]) - len(dlina_slova) < 0:
                res += propis_rus[propis_rus.find(s[i][j]) - len(dlina_slova) + 33]
            elif sdvig == 'вп' and propis_rus.find(s[i][j]) + len(dlina_slova) > 32:
                res += propis_rus[propis_rus.find(s[i][j]) + len(dlina_slova) - 33]
            elif sdvig == 'вл':
                res += propis_rus[propis_rus.find(s[i][j]) - len(dlina_slova)]
            elif sdvig == 'вп':
                res += propis_rus[propis_rus.find(s[i][j]) + len(dlina_slova)]


        elif s[i][j] == ' ':
            res += ' '
        elif s[i][j] in isklyucheniya:
            res += s[i][j]


        elif s[i][j] in alphabet:
            if sdvig == 'вл' and alphabet.find(s[i][j]) - len(dlina_slova) < 0:
                res += alphabet[alphabet.find(s[i][j]) - len(dlina_slova) + 26]
            elif sdvig == 'вп' and alphabet.find(s[i][j]) + len(dlina_slova) > 25:
                res += alphabet[alphabet.find(s[i][j]) + len(dlina_slova) - 26]
            elif sdvig == 'вл':
                res += alphabet[alphabet.find(s[i][j]) - len(dlina_slova)]
            elif sdvig == 'вп':
                res += alphabet[alphabet.find(s[i][j]) + len(dlina_slova)]


        elif s[i][j] in stroch_rus:
            if sdvig == 'вл' and stroch_rus.find(s[i][j]) - len(dlina_slova) < 0:
                res += stroch_rus[stroch_rus.find(s[i][j]) - len(dlina_slova) + 33]
            elif sdvig == 'вп' and stroch_rus.find(s[i][j]) + len(dlina_slova) > 32:
                res += stroch_rus[stroch_rus.find(s[i][j]) + len(dlina_slova) - 33]
            elif sdvig == 'вл':
                res += stroch_rus[stroch_rus.find(s[i][j]) - len(dlina_slova)]
            elif sdvig == 'вп':
                res += stroch_rus[stroch_rus.find(s[i][j]) + len(dlina_slova)]
    res += ' '
   
print(res)
