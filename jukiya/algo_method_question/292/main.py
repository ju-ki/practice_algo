"""
https://algo-method.com/tasks/292

### 問題文
文字列 $S$ が与えられます。
文字列 $S$ が `algo` という文字列を含むか判定するプログラムを作成してください。
### 入力
入力は以下の形式から与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は半角英数字からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
$S$ が `algo` という文字列を含むならば `Yes` を、含まないならば `No` を出力してください。
"""

import re
S = input()

pattern = r'.*algo'

ans = re.search(pattern, S)

if ans:
    print("Yes")
else:
    print("No")