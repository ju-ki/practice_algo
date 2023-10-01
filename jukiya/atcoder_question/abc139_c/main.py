# O(N^2)になりTLEになる
# N = int(input())
# H = list(map(int, input().split()))

# def rle(h):
#     l = 0
#     ans = []
#     while l < N:
#         r = l + 1
#         counter = 0
#         tmp_l = l
#         tmp_r = r
#         while tmp_r < N and h[tmp_l] >= h[tmp_r]:
#             r += 1
#             tmp_l += 1
#             tmp_r += 1
#             counter += 1
#         ans.append(counter)
#         if counter == 0:  # もしカウンターが0の場合、次の要素に移動
#             l += 1
#         else:  # それ以外の場合、r の位置にジャンプ
#             l = r
#     return ans

# print(max(rle(H)))

N = int(input())
H = list(map(int, input().split()))

max_moves = 0
current_moves = 0

for i in range(N - 1):  # N-1 回の比較のみが必要です
    if H[i] >= H[i + 1]:  # 現在の位置の高さが次の位置よりも高い場合
        current_moves += 1  # カウンターを増やします
        max_moves = max(max_moves, current_moves)  # カウンターの最大値を更新します
    else:
        current_moves = 0  # カウンターをリセットします

print(max_moves)
