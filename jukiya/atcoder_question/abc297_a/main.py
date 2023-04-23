N, D = map(int, input().split())
T = list(map(int, input().split()))
double_flag = False

for i in range(N - 1):
    if T[i + 1] - T[i] <= D:
        print(T[i + 1])
        double_flag = True
        break
if not double_flag:
    print(-1)