def seporator(string:str,seporators: list[str]) -> list[str]:
    return string.split(seporators)

if __name__ == '__main__':
    separators: list[str] = [';', '.', '!', '?']
    test_string = "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.."

    print(seporator( test_string,separators))