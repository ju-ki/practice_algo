"""
https://algo-method.com/tasks/490

### 問題文
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
この中から $K$ 個の整数を「最大値と最小値の差」ができるだけ小さくなるよう選んだとき、
$K$ 個の整数の「最大値と最小値の差」はいくつになりますか。
### 入力
入力は次の形式で与えられます。
```IOExample
$N K$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $10^5$ 以下の整数
- $K$ は $2$ 以上 $N$ 以下の整数
- $A_i$ は $-10^9$ 以上 $10^9$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = 100000**10

for num_i in range(N-K+1):
    diff = A[num_i+K-1] - A[num_i]
    ans = min(ans, diff)
print(ans)