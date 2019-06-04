def gcd(a, b):
    while b > 0:
        a = a % b
        a, b = b, a
    return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
