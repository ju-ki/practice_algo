"""
https://algo-method.com/tasks/365

### 問題文
「巡回セールスマン問題」と呼ばれる有名な問題があります。
```Statement
二次元座標上に $N$ 個の頂点 $0, 1, \dots, N-1$ があり、頂点 $i$ の座標は $(X_i, Y_i)$ です。
頂点 $0$ からスタートしてすべての頂点を経由して頂点 $0$ に戻ります。総移動距離をできるだけ短くしてください。
ただし、ここでの距離はユークリッド距離 (日常生活で使われている距離) を指します。
```
これに対し、アルルは次のアルゴリズムを考えました。
```Statement
まだ訪れていない頂点がある場合は、今いる頂点からまだ訪れていない頂点のうち最も近い頂点に移動する。
ただし、距離が等しい頂点がある場合は最も番号が小さい頂点に移動する。全ての頂点を訪れた後は、頂点 $0$ に戻る。
```
アルルの考えたアルゴリズムを実現するプログラムを作成してください。
### 入力
入力は以下の形式から与えられます。
```IOExample
$N$
$X_0 Y_0$
$X_1 Y_1$
$\vdots$
$X_{N-1} Y_{N-1}$
```
また、入力される値は以下の制約を満たします。
- $N$ は $2$ 以上 $1000$ 以下の整数
- $X_i$ は $-1000$ 以上 $1000$ 以下の整数 $(0 \leq i \leq N-1)$
- $Y_i$ は $-1000$ 以上 $1000$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。絶対誤差は $10^{-4}$ まで許されます。
ただし、絶対誤差とは想定解と出力の差の絶対値のことです。
"""

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
current_point = 0
point_list = [x for x in reversed(range(N))]


def calculate_distance(i, j, XY=XY):
    return ((XY[j][0]-XY[i][0])**2 + (XY[j][1]-XY[i][1])**2) ** 0.5


# 答えが小数点になってしまうので不正解になるがアルゴ式では近似値なので問題なし
total_distance = 0
nearest_point = 9999

while len(point_list) > 0:
    nearest_distance = 100000
    for point in point_list:
        distance = calculate_distance(current_point, point)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_point = point
        elif distance == nearest_distance:
            nearest_distance = distance
            nearest_point = min(nearest_point, point)
    current_point = nearest_point
    point_list.remove(nearest_point)
    total_distance += nearest_distance
total_distance += calculate_distance(current_point, 0)
print(total_distance)
