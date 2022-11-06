"""
https://algo-method.com/tasks/1026

### 問題文
$N$ 個の整数 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
この数列に対して、以下の $Q$ 回の質問に答えてください。
```Statement
整数値 $l, r$ ($l \lt r$) が与えられます。
$A_l + A_{l+1} + \dots + A_{r-1}$
の値を求めてください。
```
<details><summary>ヒント</summary><div>
数列 $A$ の累積和を $S$ とすると、
- $S_l = A_0 + A_1 + \dots + A_{l-1}$
- $S_r = A_0 + A_1 + \dots + A_{l-1} + A_l + \dots + A_{r-1}$
と表せます。これより、
$S_r - S_l = A_l + A_{l+1} + \dots + A_{r-1}$
となることが分かります。
</div></details>
### 入力
入力は次の形式で与えられます。ただし、$l_i, r_i$ は $i$ 番目のクエリを表しています。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
$Q$
$l_0$ $r_0$
$l_1$ $r_1$
$\vdots$
$l_{Q-1}$ $r_{Q-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^{5}$ 以下の整数
- $A_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- $l_i, r_i$ は $0$ 以上 $N$ 以下の整数 $(0 \leq i \leq Q-1)$
- $l_i \lt r_i$ $(0 \leq i \leq Q-1)$
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
    l, r = map(int, input().split())
    Sl = acc_list[l]
    Sr = acc_list[r]
    print(Sr - Sl)