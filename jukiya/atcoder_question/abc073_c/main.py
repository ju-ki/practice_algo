from collections import defaultdict

N = int(input())
numDict = defaultdict(int)
for _ in range(N):
    a = int(input())
    numDict[a] += 1

counter = 0
for idx, num in numDict.items():
    if num % 2 != 0:
        counter += 1
print(counter)