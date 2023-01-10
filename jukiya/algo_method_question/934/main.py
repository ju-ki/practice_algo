"""
https://algo-method.com/tasks/934

### 問題文
サイズ $H \times W$ の盤面が $2$ つ与えられます。
これらの盤面の各マスには、文字 `o` か `x` が描かれています。
各盤面に対して、上から $x$ 行目 (最上行を $0$ 行目とする)、左から $y$ 列目 (最左列を $0$ 列目とする) のマスを
$(x, y)$ と表すことにします。
このとき $2$ つの盤面の**違い度**を、
$2$ つの盤面で描かれた文字が異なるようなマス $(x, y)$ の個数として定義します。
与えられた $2$ つの盤面の違い度を求めてください。
たとえば、下図の $2$ つの盤面の違い度は $2$ です。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F160bbe15-b63d-471a-a524-6f8db9831a72%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-05-24+20.27.44.png)
### 入力
入力は次の形式で与えられます。
文字列 $S_0, S_1, \dots, S_{H-1}$ は $1$ 個目の盤面を表し、
文字列 $T_0, T_1, \dots, T_{H-1}$ は $2$ 個目の盤面を表します。
```IOExample
$H$ $W$
$S_0$
$S_1$
$\vdots$
$S_{H-1}$
$T_0$
$T_1$
$\vdots$
$T_{H-1}$
```
また、入力される値は次の制約を満たします。
- $H, W$ は $1$ 以上 $100$ 以下の整数
- $S_i, T_i$ は文字 `o`, `x` からなる長さ $W$ の文字列 $(0 \leq i \leq H-1)$
### 出力
答えを出力してください。
"""

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]
counter = 0

for h in range(H):
    for w in range(W):
        if S[h][w] != T[h][w]:
            counter += 1
print(counter)