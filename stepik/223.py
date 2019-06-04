def fib_mod(n, m):
    fibs = [0, 1, 1]
    while len(fibs) < n + 1 and not(fibs[-2] == 0 and fibs[-1] == 1): 
        fibs.append((fibs[-2] + fibs[-1]) % m)
    if len(fibs) < n + 1:
        fibs.pop()
        fibs.pop()
    return fibs[n%len(fibs)]
        


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
