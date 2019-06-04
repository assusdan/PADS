from bisect import insort

n = int(input())
l = list()

for i in range(n):
    command, _, v = input().partition(" ")
    {
        'Insert': lambda: insort(l, int(v)),
        'ExtractMax': lambda: print(l.pop())
    }[command]()
