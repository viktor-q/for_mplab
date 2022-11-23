"""Тестовое задание для MP LAB."""


#1
import re
def to_camel_case(text):
    return ''.join(word.title() for word in re.split('_|-', text)[0::])
print(to_camel_case("this_is_camel_case"))

#2
class SingletonMeta(type):
    _instances = {}

    def str(cls, *args, **kwargs):
        if cls in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
            return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    pass

logger1 = Logger()
print(logger1)

#3
count_bits = lambda n: bin(n).count('1')
print(count_bits(4))

#4
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int,str(n))))
print(digital_root(31))

#5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
print(even_or_odd(1))

