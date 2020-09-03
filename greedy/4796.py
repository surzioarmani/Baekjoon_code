
num = 0
total = list()

while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break;
    else:
        can = v // p
        last = v % p
        if v % p > l:
            total.append(can * l + l)
            num += 1
        else:
            total.append(can * l + last)
            num += 1

for i in range(num):
    print("Case " + str(i+1) +": "+ str(total[i]))
    
