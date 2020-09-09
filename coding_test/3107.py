n = list(input().split(':'))
done =0
add = 0



def zero(add):
    if add == 8:
        return
    for i in range(8-len(n)):
        n.insert(add, '0000')
        add += 1
        

        

for word in range(len(n)):
    if len(n[word]) == 4:
        pass
    elif len(n[word]) == 3:
        n[word] = '0' + n[word]
    elif len(n[word]) == 2:
        n[word] = '00' + n[word]
    elif len(n[word]) == 1:
        n[word] = '000' + n[word]
    elif n[word] == '':
        n[word] = '0000'
        add = word + 1
        


        
zero(add)      
joined_str = ':'.join(n)


    
print(joined_str[:39])
    
