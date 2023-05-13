N = int(input())
A = list(map(int, input().split()))
remain_list = [True] * N

for i in range(N):
    if not remain_list[i]:
        continue
    if remain_list[A[i] - 1]:
        remain_list[A[i] - 1] = False

print(sum([i for i in remain_list]))

print(*[i + 1 for i in range(N) if remain_list[i]])
