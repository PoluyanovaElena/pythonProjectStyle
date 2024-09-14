
from threading import Thread
from time import sleep

def numbers():
    for num in range(1, 11):
        print(num)
        sleep(1)

def letters():
    line = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for let in range(len(line)):
        print(line[let])
        sleep(1)


t1 = Thread(target=numbers)
t2 = Thread(target=letters)

t1.start()
t2.start()

t1.join()
t2.join()