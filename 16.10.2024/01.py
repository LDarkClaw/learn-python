"""Написать функцию для генерации строки из n строчных латинских букв"""
import  random
from random import randint


def generate_string(n):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    return  ''.join(random.choice(lowercase_letters) for _ in range(n))

string = generate_string(randint(1,50))
print(f"Генерированная строка длины {len(string)}:")
print(string)