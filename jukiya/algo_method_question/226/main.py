"""
https://algo-method.com/tasks/226

### 問題
英小文字からなる文字列 $S$ と、英小文字 $c$ が与えられます。
文字列 $S$ の中に $c$ が含まれるかどうかを答えるプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$S$
$c$
```
また、入力される値は次の制約を満たします。
- $S$ は英小文字からなる長さ $100$ 以下の文字列
- $c$ は英小文字
### 出力
文字列 $S$ の中に $c$ が含まれるならば`Yes`を出力し、含まれないならば`No`を出力してください。
"""

S = input()
c = input()

contain_flag = False

for s in S:
    if s == c:
        contain_flag = True
        break
print("Yes") if contain_flag else print("No")