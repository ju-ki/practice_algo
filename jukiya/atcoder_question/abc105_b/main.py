N = int(input())
flag = False

for i in range(101):
    for j in range(101):
        if 4 * i + 7 * j == N:
            flag = True
            break
    if flag:
        break
print('Yes') if flag else print('No')