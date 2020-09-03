result = 0
time = 0
n = list()
m = list()

for _ in range(11):
    a, b = map(int, input().split())
    n.append(a)
    m.append(b)


n.sort()
m.sort()
        
for i in range(11):     
    time += n[i]
    result += (time + 20 * m[i])
    print(result)
    

print(result)
    
