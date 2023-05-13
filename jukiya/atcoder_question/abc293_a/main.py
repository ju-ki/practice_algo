S = list(input())

N = len(S) // 2

for i in range(N):
    S[2 * i], S[2 * i + 1] = S[2 * i + 1], S[2 * i]
print("".join(S))