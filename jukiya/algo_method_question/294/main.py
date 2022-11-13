"""
https://algo-method.com/tasks/294

### 問題文
文字列 $S$ が与えられます。
文字列 $S$ が**位置が連続する $3$ 文字以上の数字**を含むか判定するプログラムを作成してください。
### 入力
入力は以下の形式から与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は半角英数字からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
$S$ が位置が連続する $3$ 文字以上の数字を含むならば `Yes` を、含まないならば `No` を出力してください。
"""

import re

S = input()

pattern = r'\d{3,}'

ans = re.search(pattern, S)

print("Yes") if ans else print("No")