import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
counter = 0
for i in range(N):
    for j in range(i + 1, N):
        total = 0.0
        for m in range(len(X[i])):
            total += (X[i][m] - X[j][m])**2
        if math.sqrt(total).is_integer():
            counter += 1
print(counter)