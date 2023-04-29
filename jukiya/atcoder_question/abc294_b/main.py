H, W = map(int, input().split())
A = [list(input().split()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        S = A[h][w]
        if S == "0":
            print(".", end="")
        else:
            print(chr(int(S) + 64), end="")
    print()