"""
https://algo-method.com/tasks/881

### 問題文
$N$ 個の整数からなる数列 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
これらの整数のうち、いくつかの整数を削除することで「どの整数も互いに相異なるような数列」にしたいとします。
削除するべき整数の個数の最小値を答えてください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $A_i$ は $1$ 以上 $10^{9}$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))

original_length = len(A)
distinct_length = len(list(set(A)))

print(original_length - distinct_length)