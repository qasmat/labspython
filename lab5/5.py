from typing import Generator  # явно показываем, что функция возвращает генератор

def process_line(line: str, limit: int) -> str:
    line = line.rstrip("\n")  # убираем \n, чтобы не влиял на длину и вывод

    if len(line) > limit:
        line = line[:limit]  # ограничиваем длину строки по условию

    words = line.split()  # разбиваем строку на слова
    return " ".join(reversed(words))  
    # reversed без list → экономим память, join умеет работать с итератором

def read_file_generator(file_path: str, limit: int) -> Generator[str, None, None]:
    with open(file_path, "r", encoding="utf-8") as f:  
        # with гарантирует закрытие файла

        for line in f:  # читаем файл построчно (лениво)
            yield process_line(line, limit)  
            # yield отдаёт результат сразу → не храним весь файл в памяти


for line in read_file_generator("input.txt", 30):  
        # генератор даёт строки по одной
        
    print(line)  
        # выводим сразу, без накопления