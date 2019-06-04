n = int(input())
x = [int(i) for i in input().split(' ')][::-1]
p = [0] * n
d = [0] * (n + 1)
longest_subs = 0

for i in range(n):
    lo = 1
    hi = longest_subs
    
    # binary search for longest subs able to hold curr elem
    while lo <= hi:
        mid = (lo + hi) // 2
        if x[d[mid]] <= x[i]:
            lo = mid + 1
        else:
            hi = mid - 1

    longest_with_curr = lo
    p[i] = d[longest_with_curr - 1]
    d[longest_with_curr] = i

    if longest_with_curr > longest_subs:
        longest_subs = longest_with_curr

result = [0] * longest_subs
k = d[longest_subs]
for i in range(longest_subs - 1, -1, -1):
    result[i] = n - k
    k = p[k]

print(len(result))
print(*result[::-1])
