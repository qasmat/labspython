import math

# --- 1. Сумма вложенных списков (рекурсия) ---
def sum_recursive(lst):
    total = 0
    for x in lst:
        if type(x) == list:
            total += sum_recursive(x)
        else:
            total += x
    return total


# --- 2. Сумма вложенных списков (без рекурсии) ---
def sum_nested_iterative(lst):
    total = 0
    stack = lst[:]

    while stack:
        x = stack.pop()
        if type(x) == list:
            stack.extend(x)
        else:
            total += x

    return total


#3. Последовательности (рекурсия) ---
def seq_recursive(k):
    if k == 1:
        return 1, 1

    a_prev, b_prev = seq_recursive(k - 1)

    a = 0.5 * (math.sqrt(b_prev) + math.sqrt(a_prev))
    b = 1.5 * math.sqrt(b_prev) + 0.5 * a_prev**2 - 1

    return a, b


# --- 4. Последовательности (без рекурсии) ---
def seq_iterative(k):
    a, b = 1, 1

    for i in range(2, k + 1):
        a_new = 0.5 * (math.sqrt(b) + math.sqrt(a))
        b_new = 1.5 * math.sqrt(b) + 0.5 * a**2 - 1
        a, b = a_new, b_new

    return a, b



data = [1, [2, [3, 4, [5]]]]

print(">>> Рекурсия([1, [2, [3, 4, [5]]]])")
print(sum_recursive(data))

print("\n>>> Без рекурсии([1, [2, [3, 4, [5]]]])")
print(sum_nested_iterative(data))

k = 5

print("\n>>> seq_recursive(5)")
print(seq_recursive(k))

print("\n>>> seq_iterative(5)")
print(seq_iterative(k))