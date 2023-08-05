N = int(input())
L = list(map(int, input().split()))

counter = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if L[i] == L[j] or L[j] == L[k] or L[i] == L[k]:
                continue
            if abs(L[k] - L[j]) < L[i] and L[i] < L[k] + L[j]:
                counter += 1
print(counter)