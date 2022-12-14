"""
https://algo-method.com/tasks/826

### 問題文
$N$ 個の整数からなる整数列 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
左から $k$ 番目の整数値と、右から $k$ 番目の整数値を一行ずつ答えてください。
ただし、**最も左の整数は左から $0$ 番目、最も右の整数は右から $0$ 番目**と数えることにします。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $k$
$A_0 A_1 \ldots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $k$ は $0$ 以上 $N - 1$ 以下の整数
- $A_i$ は $0$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを一行ずつ出力してください。
"""

N, k = map(int, input().split())
A = list(map(int, input().split()))

print(A[k])
print(A[N-k-1])