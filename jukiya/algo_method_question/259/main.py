"""
https://algo-method.com/tasks/259

### 問題文
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
以下の条件をみたす整数の組 $(i, j, k)$ の個数を求めるプログラムを作成してください。
- $A_i, A_j, A_k$ の最大値は $A_j$ である。
- $0 \leq i \lt j \lt k \leq N-1$
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $3$ 以上 $100$ 以下の整数
- $A_i$ は $1$ 以上 $1000$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))

counter = 0


for num_i in range(N):
    for num_j in range(num_i+1, N):
        for num_k in range(num_j+1, N):
            if A[num_j] == max(A[num_i], A[num_j], A[num_k]):
                counter += 1
print(counter)