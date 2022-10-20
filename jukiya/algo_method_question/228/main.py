"""
https://algo-method.com/tasks/228

### 問題文
英小文字からなる文字列 $S$ が与えられます。
文字列 $S$ 中に「連続する $2$ 文字が同じ文字である箇所」が何個あるかを答えるプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は英小文字からなる長さ $100$ 以下の文字列
### 出力
答えを出力してください。
"""

S = input()
length = len(S)
counter = 0

for i in range(length-1):
    if S[i] == S[i+1]:
        counter += 1
print(counter)