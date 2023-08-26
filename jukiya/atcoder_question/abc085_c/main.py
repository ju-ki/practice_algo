N, Y = map(int, input().split())

bill_list = [10000, 5000, 1000]
flag = False
#1重ループでもできるらしい
for x in range(N + 1):
    for y in range(N - x + 1):
        z = (N - (x + y))
        total = bill_list[0] * x + bill_list[1] * y + bill_list[2] * z
        if total == Y:
            print(x, y, z)
            flag = True
            break
    if flag:
        break

if not flag:
    print(-1, -1, -1)