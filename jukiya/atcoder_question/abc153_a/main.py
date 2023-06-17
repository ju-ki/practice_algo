H, A = map(int, input().split())
# counter = 0

# while H > 0:
#     H -= A
#     counter += 1

# print(counter)

# あまりで解いた方が良くない

if H % A == 0:
    print(H // A)
else:
    print(H // A + 1)