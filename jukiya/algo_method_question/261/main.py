"""
https://algo-method.com/tasks/261

### 問題文
長さ $N$ の文字列 $S$ が与えられます。
以下の条件をみたす整数の組 $(x,y)$ の個数を数えるプログラムを作成してください。
- $S$ の $x$ 文字目と $y$ 文字目は等しい
- $0 \leq x \lt y \leq N-1$
ただし、$S$ の先頭の文字が $0$ 文字目であるとします。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $S$ は英小文字からなる長さ $N$ の文字列
### 出力
答えを出力してください。
"""

N = int(input())
S = list(input())
counter = 0

for num_i in range(N):
    for num_j in range(num_i+1, N):
        if S[num_i] == S[num_j]:
            counter += 1


print(counter)
