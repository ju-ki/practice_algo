"""
https://algo-method.com/tasks/217

### 問題
$N$ 個の **$1$ 以上 $9$ 以下の**整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数に含まれる $1, 2, \dots, 9$ の個数をそれぞれ求めるプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約をみたします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $A_i$ は **$1$ 以上 $9$ 以下の**整数 $(0 \leq i \leq N-1)$
### 出力
$i$ 行目には $i$ の個数を出力してください ( $i = 1, \cdots, 9$ )。
たとえば、 $1$ 行目には $1$ の個数を出力します。
"""


N = int(input())
A = list(map(int, input().split()))

for idx in range(1, 10):
    counter = A.count(idx)
    print(counter)