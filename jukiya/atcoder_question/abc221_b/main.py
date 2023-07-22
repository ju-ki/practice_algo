S = list(input())
T = list(input())

N = len(S)

flag = False

if S == T:
    flag = True
for i in range(N - 1):
    S[i], S[i + 1] = S[i + 1], S[i]
    if S == T:
        flag = True
        break
    S[i], S[i + 1] = S[i + 1], S[i]

print('Yes') if flag else print('No')