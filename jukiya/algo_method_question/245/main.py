"""
https://algo-method.com/tasks/245

### 問題
$2$ つの整数 $L, R$ が与えられます。
$L$ 以上 $R$ 以下の整数の中から、
一の位が等しくなるように相異なる $2$ つの整数を選ぶ方法は何通りあるか求めるプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$L$ $R$
```
また、入力される値は次の制約を満たします。
- $L, R$ は $1$ 以上 $1000$ 以下の整数
- $L \leq R$
### 出力
答えを出力してください。
"""

L, R = map(int, input().split())
counter = 0

for num_i in range(L, R+1):
    for num_j in range(num_i, R+1):
        if num_i % 10 == num_j % 10 and num_i != num_j:
            counter += 1
print(counter)
