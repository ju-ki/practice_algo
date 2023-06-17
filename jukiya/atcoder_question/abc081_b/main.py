N = int(input())
A = list(map(int, input().split()))

counter = 0
flag = True
while flag:
    for a in A:
        if a % 2 != 0:
            flag = False
            break
    if flag:
        counter += 1
        for i in range(len(A)):
            A[i] = A[i] // 2
print(counter)