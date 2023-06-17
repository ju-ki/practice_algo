H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
# print(A)
ans = 0

# 右-> 1 下->0
# bit全探索
# H, Wが20以下

for order in range(2**(H + W - 2)):
    h, w = 0, 0
    # マスの種類を管理
    seen = set()
    seen.add(A[0][0])
    # i 番目のマス ( order(2) の i 桁目 )
    for i in range(H + W - 2):
        print(order >> i & 1)
        # 右にいく
        if order >> i & 1:
            h += 1
            # 盤外
            if h == H:
                break
            # 嬉しくない
            if A[h][w] in seen:
                break
        # 下に行く
        else:
            w += 1
            # 盤外
            if w == W:
                break
            # 嬉しくない
            if A[h][w] in seen:
                break
        # マスを記録
        seen.add(A[h][w])

    # 条件を満たす経路なら計上
    else:
        ans += 1

print(ans)
