"""
https://algo-method.com/tasks/338

### 問題文
文字列 $S$ が与えられます。
文字列 $S$ に括弧書きが含まれるか判定するプログラムを作成してください。
ただし、括弧書きは「 `(` と `)` で挟まれた $1$ 文字以上の文字列  」のこととします。
### 入力
入力は以下の形式から与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は半角英子文字, `(`, `)` からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
$S$ が 括弧書きを含むならば `Yes` を、含まないならば `No` を出力してください。
"""

import re

S = input()
pattern = r'\(.+\)'

ans = re.search(pattern, S)

print("Yes") if ans else print("No")