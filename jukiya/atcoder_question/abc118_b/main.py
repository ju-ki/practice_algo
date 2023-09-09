N, M = map(int, input().split())
likes = [0] * M

for i in range(N):
    data = list(map(int, input().split()))
    for j in data[1:]:
        likes[j - 1] += 1
counter = 0
for i in likes:
    if i == N:
        counter += 1
print(counter)