"""
https://algo-method.com/tasks/837

### 問題文
$N$ 人の生徒それぞれの好きな色をリストアップしたものが与えられます。
色を表す文字列 $T$ が与えられるので、色 $T$ が好きな生徒の人数を答えてください。
### 入力
入力は次の形式で与えられます。
まず最初の行には、生徒の人数を表す整数値 $N$ と、色を表す文字列 $T$ が記述されます。
なお $i$ 人目の生徒を、生徒 $i$ と呼ぶことにします。
つづく $N$ 行は各生徒の好きな色の情報を表します。
$M_i$ は生徒 $i$ の好きな色の個数を表し、$S_{i, 0}$, $S_{i, 1}$, $\dots$, $S_{i, M_{i}-1}$
は生徒 $i$ の好きな色を示す $M_i$ 個の文字列を表します。
```IOExample
$N$ $T$
$M_0$ $S_{0, 0}$ $S_{0, 1}$ $\dots$ $S_{0, M_{0}-1}$
$M_1$ $S_{1, 0}$ $S_{1, 1}$ $\dots$ $S_{1, M_{1}-1}$
$\vdots$
$M_{N-1}$ $S_{N-1, 0}$ $S_{N-1, 1}$ $\dots$ $S_{N-1, M_{N-1}-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $M_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
- $S_{i, j}, T$ は英小文字のみからなる、長さ $1$ 以上 $10$ 以下の文字列 $(0 \leq i \leq N-1, 0 \leq j \leq M_i-1)$
- $j \neq k$ のとき、$S_{i, j}$ と $S_{i, k}$ は異なる
### 出力
答えを出力してください。
"""

N, T = map(str, input().split())
counter = 0

for _ in range(int(N)):
    color_list = list(map(str, input().split()))
    for color in color_list[1:]:
        if color == T:
            counter += 1
print(counter)