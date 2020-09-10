a, n = map(int, input().split())

circle = list(range(1, a + 1))
result = []

i = n - 1
while True:
    result.append(circle.pop(i))
    if not circle:
        break
    i = (i + n - 1) % len(circle)

print('<'+', '.join(map(str, result)) + '>')

