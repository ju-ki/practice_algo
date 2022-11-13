"""
https://algo-method.com/tasks/397

### 問題文
英小文字のみからなる文字列 $S$ が与えられます。
文字列 $S$ のうち、`r` に挟まれた(両隣の文字が `r` である) `u` を `a` に置換するプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は半角英小文字からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
$S$ から、`r` に挟まれた `u` を `a` に置換したあとの文字列を出力してください。
"""

import re

S = input()
pattern = r'ru(?=r)'
replaced = "ra"

ans = re.sub(pattern, replaced, S)
print(ans)