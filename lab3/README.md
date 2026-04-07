Напишите две функции для решения задач своего варианта - с использованием рекурсии и без.

### Функция для расчёта суммы вложенных списков.

# Функции для расчёта $a_k = 1/2 ((\sqrt{ b_{k-1}})+ 1/2 (\sqrt {a_{k-1}}))$, $b_k = 3/2 (\sqrt{ b_{k-1}}) + 1/2 a_{k-1}^2$, $a_1=b_1=1$ 

# Функция считает сумму всех чисел во вложенном списке с помощью рекурсии
```python
import math

def sum_nested_recursive(lst):

    total = 0  # переменная для хранения суммы

    for x in lst:  # перебираем каждый элемент списка
        if type(x) == list:  # если элемент — это список
            total += sum_nested_recursive(x)  # рекурсивно считаем сумму внутри него
        else:
            total += x  # если число — добавляем к сумме

    return total  # возвращаем итоговую сумму
```

# Функция считает сумму всех чисел во вложенном списке без рекурсии (через стек)
```python
def sum_nested_iterative(lst):

    total = 0  # итоговая сумма
    stack = lst[:]  # создаём копию списка (будем использовать как стек)

    while stack:  # пока стек не пуст
        x = stack.pop()  # берём последний элемент

        if type(x) == list:  # если это список
            stack.extend(x)  # добавляем его элементы в стек
        else:
            total += x  # если число — добавляем к сумме

    return total  # возвращаем сумму
```

# Функция вычисляет значения a_k и b_k рекурсивно по заданным формулам
```python
def seq_recursive(k):

    if k == 1:
    
        return 1, 1  # базовый случай: начальные значения

    a_prev, b_prev = seq_recursive(k - 1)  # находим предыдущие значения

    # вычисляем текущее значение a_k по формуле
    a = 0.5 * (math.sqrt(b_prev) + math.sqrt(a_prev))

    # вычисляем текущее значение b_k по формуле
    b = 1.5 * math.sqrt(b_prev) + 0.5 * a_prev**2 - 1

    return a, b  # возвращаем пару значений
```

# Функция вычисляет значения a_k и b_k без рекурсии (через цикл)
```python
def seq_iterative(k):

    a, b = 1, 1  # начальные значения a_1 и b_1

    for i in range(2, k + 1):  # идём от 2 до k
        # считаем новые значения по формулам
        a_new = 0.5 * (math.sqrt(b) + math.sqrt(a))
        b_new = 1.5 * math.sqrt(b) + 0.5 * a**2 - 1

        a, b = a_new, b_new  # обновляем значения

    return a, b  # возвращаем результат
```


# Результат
<img width="819" height="186" alt="image" src="https://github.com/user-attachments/assets/3aff16e7-3df6-4123-b0da-374276a1c316" />

Справочник:
[Самоучитель по Python для начинающих. Часть 13: Рекурсивные функции - proglib.io](https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23)
