N = int(input())
A = list(map(int, input().split()))

alice = 0
bob = 0

for i in range(1, N+1):
    if i % 2 != 0:
        alice += max(A)
        A.remove(max(A))
    else:
        bob += max(A)
        A.remove(max(A))
print(alice-bob)
