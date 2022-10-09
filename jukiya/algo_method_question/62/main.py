"""
https://algo-method.com/tasks/62

### 問題文
$N$ 個の文字列 $S_0, S_1, \dots, S_{N-1}$ が与えられます。
$N$ 個の文字列はすべて `left` または `right` のどちらかです。
$N$ 個の文字列のうち、
- `left` の個数が多い場合は `left` を、
- `right` の個数が多い場合は `right` を、
- `left` と `right` の個数が等しい場合は `same` を出力してください。
### 入力
入力は次の形式で与えられます。$N$ は与えられる入力値の個数を指定しています。
```IOExample
$N$
$S_0$
$S_1$
$\vdots$
$S_{N-1}$
```
 また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $S_i$ は `left` は `right` のどちらかである $(0\leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = int(input())
left_count = 0
right_count = 0

for _ in range(N):
    text = input()
    if text == "left":
        left_count += 1
    else:
        right_count += 1

if left_count > right_count:
    print("left")
elif left_count < right_count:
    print("right")
else:
    print("same")
