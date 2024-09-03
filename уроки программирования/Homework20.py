from pprint import pprint

file_name = 'poetry.txt'
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
pprint(file_content)


# name = 'example.txt'
# file = open(name, 'r')
# pprint(file.read())





