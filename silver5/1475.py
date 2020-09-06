room = list(map(int, str(input())))
num = [0] * 10
 
for i in room:
    if i == 9:
        num[6] += 0.5         
    elif i == 6:
        num[6] += 0.5         
    else:
        num[i] += 1           
print(round(max(num)))          
