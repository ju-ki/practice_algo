"""
https://algo-method.com/tasks/1019

### 問題文
$N$ 個の整数 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
これらの整数の中から $1$ つの整数を選ぶ操作を $2$ 回行って、それらの積をとります。
そうして得られる $N^2$ 個の積の総和を求めてください。
つまり、
$\displaystyle \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} A_i \times A_j$
の値を求めてください。
なお、答えが **32bit 整数型に収まらない可能性** があることに注意してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^{5}$ 以下の整数
- $A_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))

S = sum(A)
print(S * S)