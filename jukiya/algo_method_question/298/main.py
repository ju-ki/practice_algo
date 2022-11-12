"""
https://algo-method.com/tasks/298

### 問題文
文字列 $S$ が与えられます。
文字列 $S$ が以下の形式を満たすか判定するプログラムを作成してください。
- $meth\underbrace{o \cdots o}_{1\text{つ以上}}d$
### 入力
入力は以下の形式から与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は半角英数字からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
$S$ が与えられた形式を満たすならば `Yes` を、満たさないならば `No` を出力してください。
"""

import re

S = input()
pattern = r'^metho+d$'

ans = re.search(pattern, S)

print("Yes") if ans else print("No")