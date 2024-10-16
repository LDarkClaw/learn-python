'''Добавьте в генератор опцию, которая будет контролировать
    разрешены ли в строке повторяющиеся символы.
    И если не разрешены, то нельзя допускать повторяющихся символов в строке.'''
import random
from random import randint
from random import choice
from string import ascii_uppercase, ascii_lowercase, punctuation,digits

def generate_string(n,use_uppercase=False,use_digits=False,use_punctuation=False,duplicate=False):
    chars = ascii_lowercase
    if use_uppercase:
        chars+=ascii_uppercase
    if use_digits:
        chars+=digits
    if use_punctuation:
        chars+=punctuation
    if duplicate:
        return ''.join(choice(chars) for _ in range(n))
    else:
        return ''.join(random.sample(chars,n))

string = generate_string(randint(1,50),
                         use_uppercase=randint(0,1),
                         use_digits=randint(0,1),
                         use_punctuation=randint(0,1),
                         duplicate=randint(0,1))

print(f"Генерированная строка длины {len(string)}:")
print(string)