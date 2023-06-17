N = int(input())
A = list(map(int, input().split()))
alice, bob = 0, 0
while len(A) > 0:
    a = max(A)
    A.remove(a)
    alice += a
    if len(A) > 0:
        b = max(A)
        A.remove(b)
        bob += b

print(alice - bob)