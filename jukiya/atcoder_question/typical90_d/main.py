H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


row = [0] * H
column = [0] * W
answer = [[0]  * W for _ in range(H)]

# O(H)
for i in range(H):
    row[i] = sum(A[i])

# O(W)
for i in range(H):
    for j in range(W):
        column[j] += A[i][j]

# O(HW)
for i in range(H):
    for j in range(W):
        answer[i][j] = row[i] + column[j] - A[i][j]
# O(HW)
for i in range(H):
    for j in range(W):
        if j < W-1:
            print(answer[i][j], end=" ")
        else:
            print(answer[i][j], end="")
    print()



