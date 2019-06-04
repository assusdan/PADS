n = int(input())
lines = []
for i in range(n):
    lines.append(list(map(int, input().split())))
lines = sorted(lines, key=lambda l: l[1])
points = []
while len(lines) > 0:
    point = lines[0][1]
    points.append(point)
    while len(lines) > 0:
        if lines[0][0] <= point:
            lines = lines[1:]
        else:
            break
print(len(points))
print(" ".join(map(str, points)))
