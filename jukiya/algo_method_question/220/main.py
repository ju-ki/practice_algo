"""
https://algo-method.com/tasks/220

### 問題文
$1$ 以上 $N$ 以下の整数のうち、
$2$ でも $3$ でも $5$ でも割り切れない数の個数を数えるプログラムを作成してください。
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
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
        counter += 1
print(counter)
