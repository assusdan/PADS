def calculator(n):
    min_opers = [0, 0]

    for i in range(2, n + 1):
        a = min_opers[i // 3] if i % 3 == 0 else float('inf')
        b = min_opers[i // 2] if i % 2 == 0 else float('inf')
        min_opers.append(min(a, b, min_opers[i - 1]) + 1)
    sequence = []
    i = n
    while i:
        sequence.append(i)
        k = min_opers[i]
        if i % 3 == 0 and min_opers[i // 3] == (k - 1):
            i //= 3
        elif i % 2 == 0 and min_opers[i // 2] == (k - 1):
            i //= 2
        else:
            i -= 1

    return min_opers[n], reversed(sequence)


def main():
    n = int(input())
    k, sequence = calculator(n)

    print(k)
    print(*sequence)


if __name__ == '__main__':
    main()
