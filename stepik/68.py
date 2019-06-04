input()
store = [0,0,0,0,0,0,0,0,0,0,0]
for i in map(int, input().split()):
    store[i] += 1
result = []
for i in range(len(store)):
    result.extend([str(i)]*store[i])
print(" ".join(result))
