n = int(input())
if n == 1:
    print(1)
    print(1)
    exit()
sum = 0
nums = []
for i in range(n):
    if (sum + i) <= n:
        sum += i
        nums.apped(i)
    else:
        break
d = n - sum
q = nums.pop()
nums.append(q + d)
print(len(nums))
print(" ".join(map(str, nums)))
