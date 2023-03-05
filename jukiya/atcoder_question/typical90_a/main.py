N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))



def solve(M):
    counter = 0
    prev = 0
    for i in range(N):
        if A[i] - prev >= M and L - A[i] >= M:
            counter += 1
            prev = A[i]
    if counter >= K:
        return True
    return False


left, right = -1, L+1
a = 0
while right - left > 1:
    medium = (right + left) // 2
    if solve(medium) == False:
        right = medium
    else:
        left = medium
    a += 1
print(left)