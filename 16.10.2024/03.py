'''Написать функцию для генерации строки из n строчных и заглавных латинских букв, а также числе и символов

Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
А если параметр use_uppercase не указан при использовании функции, то генерируем строку только из строчных букв.
По тому же сценарию добавляем контроль использования цифр и символов'''

from random import randint
from random import choice
from string import ascii_uppercase, ascii_lowercase, punctuation,digits

def generate_string(n,use_uppercase=False,use_digits=False,use_punctuation=False):
    chars = ascii_lowercase
    if use_uppercase:
        chars+=ascii_uppercase
    if use_digits:
        chars+=digits
    if use_punctuation:
        chars+=punctuation
    return ''.join(choice(chars) for _ in range(n))

string = generate_string(randint(1,50),
                         use_uppercase=randint(0,1),
                         use_digits=randint(0,1),
                         use_punctuation=randint(0,1))

print(f"Генерированная строка длины {len(string)}:")
print(string)