"""
https://algo-method.com/tasks/1025

### 問題文
$N$ 個の整数からなる数列 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
この数列に対して、以下の $Q$ 回の質問に答えてください。
----
各質問では整数値 $k$ ($0 \le k \le N$) が与えられます。
$A_0 + A_{1} + \dots + A_{k-1}$
の値を求めてください。
つまり、数列の左端から $k$ 個分の値の総和を求めてください。
----
### 入力
入力は次の形式で与えられます。ただし、$k_i$ は $i$ 番目のクエリを表しています。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
$Q$
$k_0$
$k_1$
$\vdots$
$k_{Q-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^{5}$ 以下の整数
- $A_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- $k_i$ は $0$ 以上 $N$ 以下の整数 $(0 \leq i \leq Q-1)$
### 出力
質問の答えを $1$ 行ずつ出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
acc_list = [0] * (N+1)

for idx, val in enumerate(A):
    acc_list[idx+1] = acc_list[idx] + val


for _ in range(Q):
    k = int(input())
    print(acc_list[k])