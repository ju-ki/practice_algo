"""
https://algo-method.com/tasks/52

### 問題文
$N$ 個の正の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。$N$ 個の整数の一の位を改行区切りで順に出力してください。
### 入力
入力は次の形式で与えられます。$N$ は与えられる入力値の個数を指定しています。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の条件を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $A_i$ は $1$ 以上 $1000$ 以下の整数 $(0\leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = input()
A = list(map(int, input().split()))
for item in A:
  print(item%10)