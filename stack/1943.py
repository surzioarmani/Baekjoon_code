from math import gcd

n = int(input())

num = list()


    

def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)


for i in range(n):
    num1, num2 = map(int, input().split())
    num.append((lcm(num1, num2)


            
