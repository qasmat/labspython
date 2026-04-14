Задание.py
-----
### Генератор для построчного чтения файла. Если длина строки превышает заданный предел - возвращает подстроку допустимого размера. Переверните слова в строках, возращаемых генератором.

```python
from typing import Generator
from functools import partial  # чтобы передать limit без lambda

def process_line(line: str, limit: int) -> str:
    line = line.rstrip("\n")  # убираем перенос строки

    if len(line) > limit:
        line = line[:limit]  # ограничиваем длину

    words = line.split()
    return " ".join(reversed(words))  
    # reversed без list → экономия памяти

def read_file_generator(file_path: str, limit: int) -> Generator[str, None, None]:
    with open(file_path, "r", encoding="utf-8") as f:  
        # partial "фиксирует" limit → функция принимает только line
        func = partial(process_line, limit=limit)

        yield from map(func, f)  
        # map применяет функцию к каждой строке
        # yield from отдаёт результаты по одному


for line in read_file_generator("input.txt", 30):  
        # генератор даёт строки по одной
        
    print(line)  
        # выводим сразу, без накопления
```
### Результат:
<img width="758" height="48" alt="image" src="https://github.com/user-attachments/assets/81024996-eec3-4003-9f76-3422a3cab72d" />
