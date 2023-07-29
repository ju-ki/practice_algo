a, b = map(int, input().split())
A, B = "", ""

for _a in range(a):
    A += str(b)

for _b in range(b):
    B += str(a)

print(A) if A < B else print(B)