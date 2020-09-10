n = []

for i in range(int(input())):
    n.append(input())

# 중복 제거
set_list = list(set(n))

sort_list = []

for j in set_list:
    sort_list.append((len(j), j))



sort_list.sort()

for len_list, word in sort_list:
    print(word)
