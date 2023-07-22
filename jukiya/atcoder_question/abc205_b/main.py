#ソートを使って比較
N = int(input())
A = list(map(int, input().split()))

target = [i for i in range(1, N + 1)]

A.sort()

print("Yes") if A == target else print("No")