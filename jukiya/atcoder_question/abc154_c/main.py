N = int(input())
A = list(map(int, input().split()))
if len(A) == len(list(set(A))):
    print("YES")
else:
    print("NO")