import sys

a = list(map(int, input()))


a.sort(reverse=True)
a= list(map(str, a))

a= int(''.join(a))

print(a)
