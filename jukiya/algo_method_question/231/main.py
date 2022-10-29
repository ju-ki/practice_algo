"""
https://algo-method.com/tasks/231

### 問題
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ と $M$ 個の整数 $B_0, B_1, \dots, B_{M-1}$ が与えられます。
次の条件を満たす組 $(i, j)$ の個数を答えるプログラムを作成してください。
- $i$ は $0$ 以上 $N-1$ 以下の整数
- $j$ は $0$ 以上 $M-1$ 以下の整数
- $A_i \gt B_j$
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $M$
$A_0 A_1 \dots A_{N-1}$
$B_0 B_1 \dots B_{M-1}$
```
また、入力される値は次の制約を満たします。
- $N, M$ は $1$ 以上 $100$ 以下の整数
- $A_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
- $B_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq M-1)$
### 出力
答えを出力してください。
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

counter = 0

for num_a in A:
    for num_b in B:
        if num_a > num_b:
            counter += 1
print(counter)
