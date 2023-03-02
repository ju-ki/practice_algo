N, Y = map(int, input().split())
bill_list = [10000, 5000, 1000]
flag = False
count_list = []

for a in range(N+1):
    for b in range(N+1-a):
        total = bill_list[0] * a + bill_list[1] * b + bill_list[2] * (N-a-b)
        if total == Y:
            flag = True
            count_list.append([a, b, N-a-b])
            break
    if flag:
        break

if flag:
    print(*count_list[0])
else:
    print("-1 -1 -1")
