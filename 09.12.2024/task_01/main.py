def seporator(string:str,seporator:str) -> list[str]:
    return string.split(seporator)

if __name__ == '__main__':
    print(seporator("Разделяет строку по заданному разделителю и возвращает список полученных частей"," "))