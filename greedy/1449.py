N, L =map(int, input().split())

loc = list(map(int, input().split()))
loc.sort()

start = 0
tape = 0

for i in loc:
    if start<i:
        start = i + L - 1
        tape += 1

print(tape)
