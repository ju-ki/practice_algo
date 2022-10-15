"""
https://algo-method.com/tasks/213

### 問題
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数の最大値を求めるプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $A_i$ は $-100$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
$N$ 個の整数の最大値を出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
ans = -99999

for num in A:
    if num > ans:
        ans = num
print(ans)
