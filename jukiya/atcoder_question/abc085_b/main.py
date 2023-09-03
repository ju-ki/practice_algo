N = int(input())
dictD = []

for i in range(N):
    d = int(input())
    dictD.append(d)

dictD = list(set(dictD))
counter = 0
dictD.sort(reverse=True)

num = float("INF")
for d in dictD:
    if d < num:
        counter += 1
        num = d
print(counter)