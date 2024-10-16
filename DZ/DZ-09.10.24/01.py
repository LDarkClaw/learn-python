def split_text_by_separators(text: str, seps: list[str]) -> list[str]: # Функция для разделения текста по указанным разделителям
    result: list[str] = ['']  # Инициализация списка результатов с пустой строкой
    waiting_for_separator: bool = True  # Флаг для отслеживания ожидания разделителя

    for symbol in text: # Цикл по символам в тексте
        if waiting_for_separator: # Если ожидается разделитель
            if symbol in seps: # Если текущий символ - разделитель, устанавливаем флаг в False
                waiting_for_separator = False
        else: # Если не ожидается разделитель
            if not symbol in seps and symbol != ' ':  # Проверка, не является ли символ разделителем или пробелом, если символ не разделитель и не пробел, добавляем новую пустую строку в результат
                result.append('')
                waiting_for_separator = True  # Устанавливаем флаг обратно в True
        result[-1] += symbol  # Добавляем символ к последней строке в результате
    return result  # Возвращаем список частей текста

if __name__ == "__main__":
    separators: list[str] = [';', '.', '!', '?']  # Список разделителей
    test_string = "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.."
    print(split_text_by_separators(test_string, separators))