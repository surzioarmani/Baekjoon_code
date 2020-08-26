m = input()

a = [ 'c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in a:
    m = m.replace(i,'a')

print(len(m))
print(m)
