n = int(input())
b = list()
for _ in range(n):
    b.append(input())

b.sort()

for i in range(n):
    print(b[i])
