import math

N, D = map(int, input().split())

counter = 0
for _ in range(N):
    X, Y = map(int, input().split())
    d = math.sqrt(X**2 + Y**2)
    if d <= D:
        counter += 1
print(counter)