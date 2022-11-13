"""
https://algo-method.com/tasks/435

### 問題文
英小文字のみからなる文字列 $S$ が与えられます。
文字列 $S$ のなかに、`algo` のあとに来るのが `rithm` でも `method` でもないような、`algo` + $5$ 文字以上の文字からなる部分文字列が含まれているかを答えてください。
### 入力
入力は次の形式で与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は半角英小文字からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
$S$ が問題文の条件を満たす場合 `Yes` を、そうでない場合 `No` を出力してください。
"""

import re

S = input()
pattern = r'algo(?!rithm)(?!method)[a-z]{5,}'
ans = re.search(pattern, S)

print("Yes") if ans else print("No")