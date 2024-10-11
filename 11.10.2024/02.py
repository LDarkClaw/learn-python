def split_text_by_separators(texts: list[str], seps: list[str]) -> list[list[str]]:
    result: list[str] = []

    for text in texts:
        temp_result: list[str] = ['']
        waiting_for_separator: bool = True

        for symbol in text:
            if waiting_for_separator:
                if symbol in seps:
                    waiting_for_separator = False
            else:
                if not symbol in seps and symbol != ' ':
                    temp_result.append('')
                    waiting_for_separator = True

            temp_result[-1] += symbol

        result.append(temp_result)

    return result


if __name__ == "__main__":
    separators: list[str] = [';', '.', '!', '?']
    test_string = ["Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.."]
    print(*split_text_by_separators(test_string, separators))