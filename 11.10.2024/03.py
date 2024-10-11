import random
def randon_number():
    return random.randint(1, 20)

def split_text_by_separators(text: str, seps: list[str]) -> list[str]:
    result: list[str] = ['']
    r_num=randon_number()
    i=0

    for symbol in text:
        if r_num == len(result[i]):
                result.append('')
                i+=1
        result[-1] += symbol

    return result

if __name__ == "__main__":
    separators: list[str] = [';', '.', '!', '?']
    test_string =  "Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.. "
    print(split_text_by_separators(test_string, separators))