a = list()
i = 0
k = 0


while True:
    a.append(input())
    i += 1
    if a[i - 1].find('-') != -1 : break

count1 = [0] * len(a)

for n in a:
    if n.find('-') != -1: break
    q = list(n)
    p = []
    h = 0
    first = 0
    for t in range(len(q)):
  
        
        if q[t] == '{':
            p.insert(h, q[t])
            h += 1

        elif q[t] == '}':
       
            if t == 0:
                p.insert(0, '{')
                h += 1
                first += 1
                
            elif h == 0:
                p.insert(0, '{')
                h += 1
                first += 1
                
            else:
                p.pop()
                h -= 1
                 
   

    count1[k] = (p.count('{')// 2) + first
    k += 1
    first = 0
   


for y in range(len(a) - 1):
    print(str(y + 1)+'. '+str(count1[y]))
    
            
