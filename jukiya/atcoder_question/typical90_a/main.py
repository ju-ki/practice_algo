N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

answer = A[-1]
left, right = 0, N
while right >= left:
    medium = (right + left) // 2
    answer = min(A[medium], answer)