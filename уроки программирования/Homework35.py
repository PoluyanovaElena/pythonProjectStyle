from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    time_start = datetime.now()
    print("Какое-то слово № <номер слова по порядку>")


variable = Thread(target=write_words, args=(arg1, arg2,))


