Задание.py
-----
### Генератор для построчного чтения файла. Если длина строки превышает заданный предел - возвращает подстроку допустимого размера. Переверните слова в строках, возращаемых генератором.

```python
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
```
### Результат:

<img width="690" height="44" alt="image" src="https://github.com/user-attachments/assets/ca18210d-5781-4cc7-afd0-c6ad3effbf7a" />


[Генераторы в питон](https://python-teach.ru/python-dlya-nachinayushhih/generatory-v-python/)
