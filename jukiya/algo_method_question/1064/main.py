"""
https://algo-method.com/tasks/1064

### 問題文
サイズ $H \times W$ の盤面が与えられます。
これらの盤面の各マスには、文字 `o` か `x` が描かれています。
この盤面内の `o` の描かれたマスの個数を求めてください。
たとえば下図の盤面については、`o` の個数は $5$ 個です。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F74ff2666-835c-403c-bcda-040aa477c6c8%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-07-08+14.47.11.png)
### 入力
入力は次の形式で与えられます。
文字列 $S_0, S_1, \dots, S_{H-1}$ は盤面の各行の様子を表します。
```IOExample
$H$ $W$
$S_0$
$S_1$
$\vdots$
$S_{H-1}$
```
また、入力される値は次の制約を満たします。
- $H, W$ は $1$ 以上 $100$ 以下の整数
- $S_i$ は文字 `o`, `x` からなる長さ $W$ の文字列 $(0 \leq i \leq H-1)$
### 出力
答えを出力してください。
"""

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
counter = 0

for h in range(H):
    for w in range(W):
        if S[h][w] == "o":
            counter += 1

print(counter)