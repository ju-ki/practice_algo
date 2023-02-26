N, A, B = map(int, input().split())
sums_list = []

for num_i in range(1, N+1):
    total = 0
    for num_j in str(num_i):
        total += int(num_j)
    if A <= total <= B:
        sums_list.append(num_i)
print(sum(sums_list))
