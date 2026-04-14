from typing import Generator, Iterable

def line_generator(file_path: str, max_length: int) -> Generator[str, None, None]:
    # читаем файл построчно, чтобы не грузить весь файл в память
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            clean_line = line.rstrip('\n')   # убираем перенос строки
            yield clean_line[:max_length]    # обрезаем строку до лимита

def reverse_word(word: str) -> str:
    # вынесли отдельно вместо lambda для читаемости
    return word[::-1]

def reverse_words(line: str) -> str:
    # используем map для переворота каждого слова
    return ' '.join(map(reverse_word, line.split()))

def process_file(file_path: str, max_length: int) -> Iterable[str]:
    # лениво применяем обработку к строкам генератора
    return map(reverse_words, line_generator(file_path, max_length))


file_path = "input.txt"
max_length = 20

    # выводим строки по мере обработки
for processed_line in process_file(file_path, max_length):
    print(processed_line)

with open("input.txt", "r", encoding="utf-8") as f:
    gen = (line.rstrip('\n')[:5] for line in f)  

    for line in gen:
        print(line)