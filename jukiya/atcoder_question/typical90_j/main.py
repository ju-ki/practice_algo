N = int(input())

class1 = [0] * (N+1)
class2 = [0] * (N+1)


for i in range(1, N+1):
    c, p = map(int, input().split())
    if c == 1:
        class1[i] = p
        class1[i] += class1[i-1]
        class2[i] += class2[i-1]
    elif c == 2:
        class2[i] = p
        class1[i] += class1[i-1]
        class2[i] += class2[i-1]

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    sum1 = class1[r] - class1[l-1]
    sum2 = class2[r] - class2[l-1]
    print(sum1, sum2)