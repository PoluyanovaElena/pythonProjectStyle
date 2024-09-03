# это 13 задача
N = int(input())
summ = 0

for n in range(1, N+1):
    if n % 2 == 0:
        summ -= 1 + 0.1 * n
    else:
        summ += 1 + 0.1 * n
print(summ)


# 1.3 + 1.3 + 1.3 + 1.3
# это 15 задача
# A = float(input())
# N = int(input())
# multy = 1
# for i in range(N):
#     A = i
#     multy *= A
# print(multy)

 # это задача 17
# n = int(input())
# summ = 0
# for i in range(n):
#     summ += n**(n-1)
# print(summ)


# a = int(input())
# if 5 <= a <= 10:
#     print('Утро')
# if 12 <= a <= 17:
#     print('День')
# if 18 <= a <= 22:
#     print('Вечер')
# if 22 <= a <= 4:
#     print('Ночь')
# else:
#     print('Ошибка')



