"""
https://algo-method.com/tasks/221

### 問題文
$N$ の約数の個数を数えるプログラムを作成してください。
ただし $N$ の約数とは「 $N$ を割り切ることのできる $1$ 以上の整数」のことです。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
### 出力
答えを出力してください。
"""

N = int(input())
counter = 0

for num in range(1, N+1):
    if N % num == 0:
        counter += 1
print(counter)
