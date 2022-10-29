"""
https://algo-method.com/tasks/244

### 問題
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ と整数 $K$ が与えられます。
これらの $N$ 個の整数から、和が $K$ 以下となるように $2$ つの数を選ぶ方法は何通りあるか求めるプログラムを作成してください。
ただし選んだ $2$ つの整数の添字 ($A_i$ の $i$) が等しくなってはいけないものとします。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $K$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $100$ 以下の整数
- $K$ は $2$ 以上 $200$ 以下の整数
- $A_0, A_1, \dots, A_{N-1}$ は $1$ 以上 $100$ 以下の整数
### 出力
答えを出力してください。
"""
import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))
counter = 0

for comb_tuple in itertools.combinations(A, 2):
    equation = comb_tuple[0] + comb_tuple[1]
    if equation <= K:
        counter += 1

print(counter)
