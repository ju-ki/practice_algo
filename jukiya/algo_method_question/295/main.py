"""
https://algo-method.com/tasks/295

### 問題文
文字列 $S$ が与えられます。
文字列 $S$ が以下の形式を満たすか判定するプログラムを作成してください。
```Statement
(数字が $3$ つ) $\text{-}$ (数字が $4$ つ)
```
### 入力
入力は以下の形式から与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は`0`, `1`, $\cdots$, `9`, `-` から構成される、長さ $8$ の文字列
### 出力
$S$ が与えられた形式を満たすならば `Yes` を、満たさないならば `No` を出力してください。
"""

import re
S = input()

pattern = r'^\d{3}\-\d{4}$'

ans = re.search(pattern, S)

print("Yes") if ans else print("No")