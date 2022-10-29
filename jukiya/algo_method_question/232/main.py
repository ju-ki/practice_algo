"""
https://algo-method.com/tasks/232

### 問題
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ と $M$ 個の整数 $B_0, B_1, \dots, B_{M-1}$ と整数 $K$ が与えられます。
次の条件を満たす組 $(i, j)$ の個数を答えるプログラムを作成してください。
- $i$ は $0$ 以上 $N-1$ 以下の整数
- $j$ は $0$ 以上 $M-1$ 以下の整数
- $A_i + B_j = K$
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $M$ $K$
$A_0 A_1 \dots A_{N-1}$
$B_0 B_1 \dots B_{M-1}$
```
また、入力される値は次の制約を満たします。
- $N, M$ は $1$ 以上 $100$ 以下の整数
- $K$ は $1$ 以上 $200$ 以下の整数
- $A_0, A_1, \dots, A_{N-1}$ は $1$ 以上 $100$ 以下の整数
- $B_0, B_1, \dots, B_{M-1}$ は $1$ 以上 $100$ 以下の整数
### 出力
答えを出力してください。
"""

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
counter = 0

for num_a in A:
    for num_b in B:
        equation = num_a + num_b
        if equation == K:
            counter += 1
print(counter)
