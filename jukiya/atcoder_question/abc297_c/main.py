case = 1
if case == 0:
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    for h in range(H):
        S[h] = S[h].replace("TT", "PC")
        for w in range(W - 1):
            if S[h][w] == "T" and S[h][w + 1] == "T":
                S[h][w] = "P"
                S[h][w + 1] = "C"

    for h in range(H):
        for w in range(W):
            print(S[h][w], end="")
        print()
elif case == 1:
    H, W = map(int, input().split())
    for _ in range(H):
        print(input().replace("TT", "PC"))