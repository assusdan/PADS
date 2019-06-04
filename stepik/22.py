def fib(n):
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n-1]

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
