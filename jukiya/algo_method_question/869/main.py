"""
https://algo-method.com/tasks/869

### 問題文
$N$ 個の文字列 $S_0, S_1, \ldots, S_{N-1}$ が与えられます。
この中から相異なる $2$ つの文字列を選びます。
このとき、$2$ つの文字列が互いにアナグラムになっている確率を求めてください。
なお $2$ つの文字列が互いにアナグラムになっているとは、一方の文字列の文字を並び替えると他方に一致することを言います。
たとえば `algo` を並び替えると `goal` になりますので、`algo` と `goal` は互いにアナグラムです。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S_0 S_1 \ldots S_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $5 \times 10^{5}$ 以下の整数
- $S_i$ は英小文字のみからなる長さ $10$ 以下の文字列 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
絶対誤差は $10^{−9}$ まで許されます。
ただし、絶対誤差とは想定解と出力の差の絶対値のことです。
"""

from collections import defaultdict

N = int(input())
S = list(input().split())

counter = defaultdict(int)

for s in S:
    sorted_s = ''.join(sorted(s))
    counter[tuple(sorted_s)] += 1

all_pattern = N * (N-1) // 2
same_pattern = 0

for val in counter.values():
    same_pattern += val * (val-1) // 2

answer = same_pattern / all_pattern
print(answer)
