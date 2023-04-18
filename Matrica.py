def matrix(n=None,m=None,value=0):
    if n == None and m == None:
        n,m = 1,1
    elif m == None:
        m=n
    kek = [[value for i in range(m)] for j in range(n)]
    return kek

kek = []

print(matrix())
print(matrix(3))
print(matrix(2, 5))
print(matrix(3, 4, 9))