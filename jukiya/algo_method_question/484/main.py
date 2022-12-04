"""
https://algo-method.com/tasks/484

### 問題文
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
この中から $K$ 個の整数を、できるだけ総和が大きくなるよう選んだとき、
$K$ 個の整数の総和はいくつになりますか。
### 入力
入力は次の形式で与えられます。
```IOExample
$N K$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^5$ 以下の整数
- $K$ は $1$ 以上 $N$ 以下の整数
- $A_i$ は $-10000$ 以上 $10000$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = sum(A[N-K:])
print(ans)