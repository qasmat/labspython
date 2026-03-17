import itertools

def count_code_words():

    first_letters = ['X', 'Y', 'Z']
    other_letters = ['A', 'B', 'C', 'D']

    # Генерируем все возможные комбинации для позиций 2-4
    total_count=0
    for letter2 in other_letters:
        for letter3 in other_letters:
            for letter4 in other_letters:
            


                total_count += 1

    

    return total_count

result = count_code_words()
print(f"Количество различных кодовых слов: {result}")