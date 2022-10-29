"""
https://algo-method.com/tasks/234

### 問題
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数の中に素数がいくつあるか調べるプログラムを作成してください。
### 入力と出力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $A_0, A_1, \dots, A_{N-1}$ は $1$ 以上 $100$ 以下の整数
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
counter = 0

for num_i in A:
    if num_i == 1:
        continue
    prime_flag = True
    for num_j in range(2, num_i):
        if num_i % num_j == 0:
            prime_flag = False
    if prime_flag:
        counter += 1
print(counter)
