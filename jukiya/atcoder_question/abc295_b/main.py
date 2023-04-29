R, C = map(int, input().split())
B = [input() for _ in range(R)]

for r in range(R):
    for c in range(C):
        if B[r][c] != "#" and B[r][c] != ".":
            power = int(B[r][c])
