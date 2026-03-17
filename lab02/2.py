def solve():
    value = 9 **8 + 3 ** 5 - 9

    digits = []
    n = value
    while n > 0:
        digits.append(n % 3)
        n //= 3
    return digits.count(2)


print(solve())