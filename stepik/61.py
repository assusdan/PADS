a = {}
A = list(map(int, input().split()))
for i in range(1, len(A)):
    a[A[i]] = i
b = list(map(int, input().split()))
result = []
for i in range(1, len(b)):
    result.append(a.get(b[i], -1))
print(" ".join(map(str, result)))
