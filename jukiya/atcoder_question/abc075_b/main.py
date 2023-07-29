H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
A = [[0 for _ in range(W)] for _ in range(H)]
DX = [0, 0, 0, 1, 1, 1, -1, -1, -1]
DY = [0, 1, -1, 0, 1, -1, 0, 1, -1]

for i in range(H):
    for j in range(W):
        if S[i][j] != '.':
            A[i][j] = "#"
            continue
        counter = 0
        for w in range(len(DX)):
            dx, dy = i + DX[w], j + DY[w]
            if dx < 0 or dx >= H or dy < 0 or dy >= W:
                continue
            if S[dx][dy] == "#":
                counter += 1
        A[i][j] = counter

for i in range(H):
    for j in range(W):
        print(A[i][j], end="")
    print()