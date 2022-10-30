"""
https://algo-method.com/tasks/1023

### 問題文
$N$ 個の整数 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
これらの整数から $1$ 個選んで除外します。
残りの $N - 1$ 個の整数の総和として考えられる最大値を求めてください。
なお、**答えが 32bit 整数型に収まらない可能性がある**ことに注意してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $2 \times 10^{5}$ 以下の整数
- $A_i$ は $1$ 以上 $10^{9}$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)
max_value = 0

for num_i in range(N):
    max_value = max(max_value, sum_A - A[num_i])
print(max_value)
