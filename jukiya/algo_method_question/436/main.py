"""
https://algo-method.com/tasks/436

### 問題文
空白区切りの複数単語からなる英文字列 $S$ が与えられます。
文字列 $S$ の中にある `asian` という単語のあとに $5$ 単語以上が続くならば、その `asian` を `global` に置き換えた文字列を出力してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は半角英子文字と半角空白からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
問題文の指示に従って置換したあとの文字列を出力してください。
"""

import re

S = input()
pattern = r'asian(?=(\s[a-z]+){5,})'
replaced = "global"
ans = re.sub(pattern, replaced, S)
print(ans)