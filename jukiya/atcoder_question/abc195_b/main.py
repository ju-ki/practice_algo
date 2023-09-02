# A, B, W = map(int, input().split())
# max_num, min_num = -1, 10000
# for i in range(A, B + 1):
#     C = (W * 1000 // i) * 10
#     for j in range(1, C + 1):
#         if i * j == W * 1000:
#             max_num = max(j, max_num)
#             min_num = min(j, min_num)
# print(min_num, max_num)

A, B, _W = map(int, input().split())
W = 1000 * _W

min_num = float("INF")
max_num = -1

for n in range(1, 10**6 + 100):
    l = A * n
    r = B * n
    if l <= W <= r:
        max_num = max(max_num, n)
        min_num = min(min_num, n)

if max_num == -1:
    print("UNSATISFIABLE")
else:
    print(min_num, max_num)