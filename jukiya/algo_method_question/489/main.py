"""
https://algo-method.com/tasks/489

### 問題文
$N$ 個の異なる整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$k = 0, 1, \dots, M-1$ について、次の質問に答えてください。
```Statement
$N$ 個の整数のうち、$X_k$ 番目に小さい数はいくつですか。
```
ただし、一番小さい数を 「 $0$ 番目に小さい数 」 とします。
### 入力
入力は次の形式で与えられます。
```IOExample
$N M$
$A_0 A_1 \dots A_{N-1}$
$X_0 X_1 \dots X_{M-1}$
```
また、入力される値は次の制約を満たします。
- $N, M$ は $1$ 以上 $10^5$ 以下の整数
- $A_i$ は $-10^9$ 以上 $10^9$ 以下の整数 $(0 \leq i \leq N-1)$
- $i \neq j$ のとき、 $A_i \neq A_j$
- $X_i$ は $0$ 以上 $N-1$ 以下の整数 $(0 \leq i \leq M-1)$
### 出力
$k = 0, 1, \dots, M-1$ について答えを出力してください。
$i$ 行目には $k = i$ のときの質問の答えを出力してください。
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))


A.sort()

for num_m in range(M):
    idx = X[num_m]
    print(A[idx])