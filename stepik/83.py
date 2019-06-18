def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    m, n = len(s1), len(s2)
    previous = list(range(n + 1))

    for i, ch1 in enumerate(s1, 1):
        current = [i]

        for j, ch2 in enumerate(s2, 1):
            current.append(min(current[j - 1] + 1, previous[j] + 1, previous[j - 1] + int(ch1 != ch2)))
        previous = current[:]

    return previous[-1]


def main():
    s1, s2 = input(), input()
    print(levenshtein_distance(s1, s2))


if __name__ == '__main__':
    main()
