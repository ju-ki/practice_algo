N, X = map(int, input().split())
A = list(map(int, input().split()))


def binary_search(x, lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == x:
            return True
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


A.sort()
# for文が抜けていた
for i in range(N):
    if binary_search(A[i] + X, A):
        print("Yes")
        break
else:
    print("No")
