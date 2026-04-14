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

if __name__ == "__main__":
    for line in read_file_generator("input.txt", 30):
        print(line)