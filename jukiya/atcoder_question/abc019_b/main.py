S = list(input())
N = len(S)

l = 0
ans = []
while l < N:
    r = l + 1
    while r < N and S[l] == S[r]:
        r += 1
    print(S[l], end="")
    print(r - l, end="")
    l = r
print()