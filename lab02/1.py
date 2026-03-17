import itertools

def count_code_words():

    first_letters = ['X', 'Y', 'Z']
    other_letters = ['A', 'B', 'C', 'D']

    # Генерируем все возможные комбинации для позиций 2-4
    other_combinations = list(itertools.product(other_letters, repeat=3))

    total_count = 0

    for first in first_letters:
        # Для каждой первой буквы добавляем все комбинации остальных
        total_count += len(other_combinations)

    return total_count

result = count_code_words()
print(f"Количество различных кодовых слов: {result}")