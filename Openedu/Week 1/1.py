from functools import reduce
f = open("input.txt", "r");
o = open("output.txt", "w")

o.write(str(reduce(lambda x, y: x+y, map(int, f.readline().split(' ')))))