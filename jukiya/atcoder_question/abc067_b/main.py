#ソートしてK個の合計値を求める
N, K = map(int, input().split())
L = list(map(int, input().split()))

L.sort(reverse=True)

print(sum(L[:K]))