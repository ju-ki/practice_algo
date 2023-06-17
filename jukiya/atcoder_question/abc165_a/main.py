K = int(input())
A, B = map(int, input().split())
flag = False

for t in range(A, B + 1):
    if t % K == 0:
        flag = True
        break

print("OK") if flag else print("NG")