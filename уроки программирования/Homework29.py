# /// эта задача сдана///

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(first_strings[i]) for i in range(len(first_strings)) if len(first_strings[i]) >= 5]
print(first_result)

second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
print(second_result)

third_result = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}
print(third_result)



# def func_1(x):
#     return x**2
#
# def func_2(x):
#     return x % 2
#
# result = map(func_1, filter(func_2, my_numbers))
# print(list(result))

my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = [x**2 for x in my_numbers if x % 2]
print(result)