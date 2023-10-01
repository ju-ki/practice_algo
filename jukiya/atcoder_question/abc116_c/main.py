N = int(input())
H = list(map(int, input().split()))

maxH = max(H)
counter = 0

for i in range(N):
    counter += maxH - H[i]
print(counter)