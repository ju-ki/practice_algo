N = int(input())
A = list(map(int, input().split()))

counter = 0

while True:
    flag = True
    for i in range(N):
        if A[i] % 2 != 0:
            flag = False
            break
        A[i] = A[i] // 2
    if not flag:
        break
    counter += 1
print(counter)