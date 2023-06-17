N, K = map(int, input().split())
L = list(map(int, input().split()))
counter = 1
D = 0
for n in range(N):
    D += L[n]
    if D > K:
        break
    counter += 1
print(counter)
