N = int(input())
S = [list(map(str, input().split())) for _ in range(N)]

S.sort(key=lambda s: int(s[1]), reverse=True)

print(S[1][0])