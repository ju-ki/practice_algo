from collections import defaultdict

N = int(input())
num = defaultdict(int)
for _ in range(N):
    s = input()
    s = "".join(sorted(s))
    num[s] += 1

counter = 0
for s in num:
    n = num[s]
    counter += (n * (n - 1)) // 2
print(counter)