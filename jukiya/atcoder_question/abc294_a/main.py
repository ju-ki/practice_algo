N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    ai = A[i]
    if ai % 2 == 0:
        print(ai, end=" ")
