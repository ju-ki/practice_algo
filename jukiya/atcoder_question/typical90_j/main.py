N = int(input())

class1 = [0] * (N+1)
class2 = [0] * (N+1)


for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        class1[i] = p
    elif c == 2:
        class1[i] = p

Q = int(input())

# for _ in range(Q):
#     l, r = 