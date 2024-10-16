'''Написать функцию для генерации строки из n строчных и заглавных латинских букв
Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
А если параметр use_uppercase не указан при использовании функции,
то генерируем строку только из строчных букв.'''


from random import randint
from random import choice
from string import ascii_letters, ascii_lowercase

def generate_string(n,use_uppercase=False):
    if use_uppercase == True:
        return  ''.join(choice(ascii_letters) for _ in range(n))
    else:
        return ''.join(choice(ascii_lowercase) for _ in range(n))

string = generate_string(randint(1,50),randint(0,1))
print(f"Генерированная строка длины {len(string)}:")
print(string)