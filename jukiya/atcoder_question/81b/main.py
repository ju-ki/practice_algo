N = int(input())
A = list(map(int, input().split()))
counter = 0
even_flag = True
while even_flag:
    for a in A:
        if a % 2 != 0:
            even_flag = False
    if even_flag:
        for i in range(N):
            A[i] /= 2
        counter += 1
print(counter)
