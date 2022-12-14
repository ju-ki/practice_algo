"""
https://algo-method.com/tasks/340

### 問題文
文字列 $S$ が与えられます。
文字列 $S$ が 英文として成立しているか判定するプログラムを作成してください。
ただし、以下の条件をみたすとき「英文として成立している」とします。
```Statement
「$S_0$-$S_1$-$\cdots$-$S_N$」という形式で表される。
ただし、$S_i$ は $1$ 文字以上の英小文字列とする。$(0 \leq i \leq N)$
```
### 入力
入力は以下の形式から与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は半角英小文字, `-` からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
$S$ が条件を満たすならば `Yes` を、満たさないならば `No` を出力してください。
"""

import re

S = input()

pattern = r'^([a-z]+\-)*[a-z]+$'

ans = re.search(pattern, S)

print("Yes") if ans else print("No")