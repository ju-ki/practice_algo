N, K = map(int, input().split())
H = [int(input()) for i in range(N)]

H.sort()

answer = 10**9

for i in range(N - K + 1):
    # 先頭
    R = i + K - 1
    answer = min(answer, H[R] - H[i])
print(answer)
