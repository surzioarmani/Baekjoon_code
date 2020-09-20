num = int(input())
price = []

for _ in range(num):
    price.append(list(map(int,input().split())))

    total = [price[0]]


for i in range(1,num):
    color = []

    red = min(total[i-1][1], total[i-1][2])
    color.append(red + price[i][0])

    green =min(total[i-1][0], total[i-1][2])
    color.append( green + price[i][1])

    blue = min(total[i-1][0], total[i-1][1])
    color.append(blue + price[i][2])

    total.append(color)

print(min(total[num-1]))
