#ソートしてメジアンを取る

N = int(input())
D = list(map(int, input().split()))

D.sort()

Ni = max(D)

target1, target2 = D[N // 2 - 1], D[N // 2]

print(target2 - target1)