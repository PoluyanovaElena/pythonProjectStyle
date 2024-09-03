# обычный цикл for
for i in range(5):
    print(i, end=" ")
print()

# обычный while
ind2 = 0
while ind2 < 5:
    print(str(ind2), end=" ")
    ind2 += 1
print()

mas = [0, 5, 3, 4, 7, 6, 0, 9]

# проход массива по индексам с помощью range
for i in range(len(mas)):
    print(mas[i], end=" ")
print()  # принт для переноса (параметр end='\n' по умолчанию), так как перед этой строкой end = " "

# проход массива по элементам
for item in mas:
    print(item, end=" ")
print()

# проход массива по индексам с помощью while
ind3 = 0
while ind3 < len(mas):
    print(mas[ind3], end=" ")
    ind3 += 1
print()

string2 = 'hwdfmlg'

# перебор всех возможных пар символов строки (также работает для массивов, так как строка это массив char элементов)
for i in range(len(string2)):
    for j in range(i+1, len(string2)):
        print(string2[i] + string2[j], end="; ")
print()

# перебор всех возможных пар символов строки в обратном порядке
for i in range(len(string2)-1, -1, -1):
    for j in range(len(string2)-1, i, -1):
        print(string2[j] + string2[i], end="; ")