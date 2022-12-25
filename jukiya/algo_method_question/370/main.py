"""
https://algo-method.com/tasks/370

### 問題文
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ と、$M$ 個の整数 $B_0, B_1, \dots, B_{M-1}$ が与えられます。
$A_0, A_1, \dots, A_{N-1}$ はすべて異なり、小さい順に並んでいます。
つまり、 $A_0 \lt A_1 \lt \dots \lt A_{N-1}$ が成り立ちます。
$k = 0, 1, \dots, M-1$ について次の問いに答えてください。
```Statement
$A_x \geq B_k$ を満たす $x$ の最小値を求めよ。
```
### 入力
入力は次の形式から与えられます。
```IOExample
$N$ $M$
$A_0 A_1 \dots A_{N-1}$
$B_0 B_1 \dots B_{M-1}$
```
また、入力される値は次の制約を満たします。
- $N, M$ は $1$ 以上 $10^5$ 以下の整数
- $A_i$ は $1$ 以上 $10^9$ 以下の整数 $(0 \leq i \leq N-1)$
- $A_0 \lt A_1 \lt \dots \lt A_{N-1}$
- $B_i$ は $1$ 以上 $A_{N-1}$ 以下の整数 $(0 \leq i \leq M-1)$
### 出力
$M$ 行で答えを出力してください。(最初の行を $0$ 行目とします。)
ただし、$i$ 行目には $k=i$ の場合の答えを出力してください。
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


# whileの条件式が違う, compare関数を自作したせいでごっちゃになった
for num_b in range(len(B)):
    left, right = 0, N-1
    while (left != right):
        mid = (left + right) // 2
        if (A[mid] >= B[num_b]):
            right = mid
        else:
            left = mid + 1
    answer = left
    print(answer)