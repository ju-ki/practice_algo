"""
https://algo-method.com/tasks/235

### 問題
$1$ 以上の整数 $N$, $K$ が与えられます。
$1$ 以上 $N$ 以下の整数の中で約数をちょうど $K$ 個持つ数の個数を調べるプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $K$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $K$ は $1$ 以上 $30$ 以下の整数
### 出力
答えを出力してください。
"""

N, K = map(int, input().split())
counter = 0

for num_i in range(1, N+1):
    divisor_counter = 0
    for num_j in range(1, num_i+1):
        if num_i % num_j == 0:
            divisor_counter += 1
    if divisor_counter == K:
        counter += 1
print(counter)