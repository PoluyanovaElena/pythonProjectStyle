first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(pair[0])-len(pair[1]) for pair in zip(first, second) if len(pair[0]) != len(pair[1]))
print(list(first_result))

second_result = (True if len(first[i]) == len(second[i]) else False for i in range(len(first)))
print(list(second_result))
