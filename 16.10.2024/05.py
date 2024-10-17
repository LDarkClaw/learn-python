'''Переделайте функцию в класс RandomGenerator, в конструктор он принимает то же, что и функция в 4-й задаче.
Объект генерирует строку в методе get_string().
Также у него должен быть метод генерирующий строку только строчных букв, только заглавных букв, только цифр и только символов.'''

import random
from random import randint
from random import choice
from string import ascii_uppercase, ascii_lowercase, punctuation,digits

class RandomGenerator:
    def __init__(self,n,use_uppercase=False,use_digits=False,use_punctuation=False,duplicate=False):
        self.n=n
        self.use_uppercase=use_uppercase
        self.use_digits=use_digits
        self.use_punctuation=use_punctuation
        self.duplicate=duplicate
        self.chars=self.get_chars()


    def get_chars(self):
        chars = ascii_lowercase
        if self.use_uppercase:
            chars+=ascii_uppercase
        if self.use_digits:
            chars+=digits
        if self.use_punctuation:
            chars+=punctuation
        return chars

    def get_string(self):
        if self.duplicate:
            return ''.join(choice(self.chars) for _ in range(self.n))
        else:
            return ''.join(random.sample(self.chars, self.n))

    def get_lowercase_only(self):
        return ''.join(random.choice(ascii_lowercase) for _ in range(self.n))
    def get_uppercase_only(self):
        return ''.join(random.choice(ascii_uppercase) for _ in range(self.n))
    def get_digits_only(self):
        return ''.join(random.choice(digits) for _ in range(self.n))
    def get_punctuation_only(self):
        return ''.join(random.choice(punctuation) for _ in range(self.n))


string = RandomGenerator(randint(1,50),
                         use_uppercase=randint(0,1),
                         use_digits=randint(0,1),
                         use_punctuation=randint(0,1),
                         duplicate=randint(0,1))

print(f"Генерированная строка длины {len(string.get_string())}:")
print(string.get_string())