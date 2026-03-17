def solve():
    result = []
    candidates_p = [3, 5, 7, 11, 13]

    for p in candidates_p:
        m = p ** 4
        k = 0
        while True:
            N = (2**k) * m
            if N > 50000:
                break
            if N >= 40000:
                result.append(N)
            k += 1

    return sorted(result)

numbers = solve()
for num in numbers:
    print(num)