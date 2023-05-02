a,c = [i for i in input()],[]
kek = ''
for i in range(len(a)):
    if a[i].isdigit() == True:
        kek += a[i]
    elif a[i].isalpha() == True:
        if kek!='':
            c.append(a[i] * int(kek))
            kek = ''
        else:
            c.append(a[i])
print(*c, sep='')