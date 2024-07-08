class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass



def f1(a, b):
    if type(a) is not type(b):
        raise InvalidDataException('Нельзя складывать переменные разных типов')
    if b == 0:
        raise ProcessingException('На ноль делить нельзя')
    result1 = a + b
    result2 = a/b
    return result1, result2
    # return a/b


try:
    result = f1(2, 0)
except InvalidDataException as e:
    print(e)
except ProcessingException as e:
    print(e)

# def f2(value):
