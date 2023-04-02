def find_Smallest(arr): # Нахождение наименьшего символа
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    smallest = ()
    for i in range(len(arr)):
        smallest = arr.index(min(arr))
        print(smallest)
        newArr.append(arr.pop(smallest))
    return newArr

c = [int(i) for i in input().split()]

print(c[find_Smallest(c)], 'kek')
print(selectionSort(c))
#Немного переделал код для сортировки выбором в 'Грокаем алгоритмы'
