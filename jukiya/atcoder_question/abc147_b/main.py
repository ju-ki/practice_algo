S = list(input())
Sl = len(S) // 2

counter = 0

for i in range(Sl):
    if S[i] == S[-i - 1]:
        continue
    counter += 1
print(counter)