"""
https://algo-method.com/tasks/1022

### 問題文
$N$ 個の整数 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
これらの整数から $2$ 個選びます (重複してもよいです)。
選んだ $2$ 個の整数の**差の最大値**を求めてください。
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


max_value = max(A)
min_value = min(A)
diff = max_value - min_value
print(diff)