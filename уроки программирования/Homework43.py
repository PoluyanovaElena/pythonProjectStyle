import numpy as np
# создание массива:
arr_a = np.array([20, 24, 42, 56])
arr_b = np.arange(2, 9, 2)
arr_c = np.arange(5)
arr_d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_a)
print(arr_b)
print(arr_c)
print(arr_d)

# математические операции выполняются поэлементно:
print(arr_a + arr_b)
print(arr_a - arr_b)
print(arr_a * arr_b)
print(arr_a / arr_b)
print(arr_a ** arr_b)
print(arr_a % arr_b)
print(arr_c + 5)
print(arr_d + 1)

# унарные операции:
print(arr_d.sum())
print(arr_d.min())
print(arr_d.max())