"""
https://algo-method.com/tasks/501

### 問題文
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。これらの中央値 $\tilde{A}$ を求めてください。
ただし、中央値 $\tilde{A}$ は次のように定められる値です。
```Statement
$N$ 個の整数を小さい順に $A[0], A[1], \dots, A[N-1]$ とおくと、
$\tilde{A} = \left\{
\begin{array}{ll}
A[\frac{N-1}{2}] & (N=\text{奇数}) \\
 & \\
(A[\frac{N}{2}-1] + A[\frac{N}{2}]) \div 2 & (N=\text{偶数})
\end{array}
\right.$
```
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^5$ 以下の整数
- $A_i$ は $-10^9$ 以上 $10^9$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
出力値の誤差は $10^{-6}$ まで許容されます。
"""

N = int(input())
A = list(map(int, input().split()))


A.sort()

if len(A) % 2 == 0:
    medium = (A[N // 2 - 1] + A[N // 2]) / 2
else:
    medium = A[(N-1) // 2]
print(medium)