class Item:
    def __init__(self, c_w):
        self.c = c_w[0]
        self.weigth = c_w[1]
        self.value = self.c / self.weigth

n, capacity = map(int, input().split())
raw_items = []
for i in range(n):
    raw_items.append(Item(list(map(int, input().split()))))
items = sorted(raw_items, key=lambda i: i.value)

max_value = 0
while capacity > 0 and len(items) > 0:
    i = items.pop()
    available_capacity = min(capacity, i.weigth)
    max_value += available_capacity * i.value
    capacity -= available_capacity

print(max_value)
