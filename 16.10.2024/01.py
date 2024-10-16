"""Написать функцию для генерации строки из n строчных латинских букв"""
import  random

def generate_string(n):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    return  ' '.join(random.choice(lowercase_letters) for _ in range(n))

string = generate_string(8)
print(f"Генерированная строка длины {len(string)}:")
print(string)