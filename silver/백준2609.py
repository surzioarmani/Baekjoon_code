a = int(input())


b = list()
for _ in range(a):
    A = list(map(int, input().split()))
    A.sort(reverse = True)
    b.append(A[2])

for i in range(a):
    print(b[i])
    

