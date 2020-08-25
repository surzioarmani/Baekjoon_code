T = int(input())

zero = [1, 0, 1]
one= [0, 1, 1]
b=list()
c=list()

def fib(n):
    
    if len(zero) <= n:
        for i in range(1, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])





for i in range(T):
    m = int(input())
    fib(m)
    b.append(zero[m])
    c.append(one[m])

for i in range(T):
    print(b[i], c[i])

