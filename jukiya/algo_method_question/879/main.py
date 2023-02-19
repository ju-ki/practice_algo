"""
https://algo-method.com/tasks/879

### 問題文
$N$ 個の文字列 $S_0, S_1, \dots, S_{N-1}$ が与えられます。
これらの文字列に含まれる文字列の種類数を答えてください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S_0 S_1 \ldots S_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $5 \times 10^{5}$ 以下の整数
- $S_i$ は英小文字のみからなる長さ $5$ 以下の文字列 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = int(input())
S = list(input().split())

print(len(list(set(S))))