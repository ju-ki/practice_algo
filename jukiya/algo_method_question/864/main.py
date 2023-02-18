"""
https://algo-method.com/tasks/864

### 問題文
$N$ 個の整数 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
この中から $2$ つの整数をランダムに選びます。
整数値が等しくなってもよいですが、同じ位置から選ばないようにします。
このとき、$2$ つの整数値が等しくなる確率を求めてください。
なお、方針によっては計算途中の数値が **32bit 整数型に収まらない可能性** があることに注意してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $2 \times 10^{5}$ 以下の整数
- $A_i$ は $0$ 以上 $10^{5}$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
絶対誤差は $10^{−6}$ まで許されます。
ただし、絶対誤差とは想定解と出力の差の絶対値のことです。
"""


N = int(input())
A = list(map(int, input().split()))
max_A = max(A)
count_list = [0] * (max_A+1)
denominator = N * (N-1) // 2
counter = 0


for a in A:
    count_list[a] += 1

for val in count_list:
    counter += val * (val-1) // 2

print(counter / denominator)
