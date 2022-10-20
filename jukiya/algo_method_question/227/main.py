"""
https://algo-method.com/tasks/227

### 問題文
英小文字からなる文字列 $S$ が与えられます。
文字列 $S$ が回文かどうかを判定するプログラムを作成してください。
なお文字列 $S$ が回文であるとは、$S$ を逆から読んでも $S$ になることを言います。
### 入力
入力は次の形式で与えられます。
```IOExample
$S$
```
また、入力される値は次の条件を満たします。
- $S$ は英小文字からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
文字列 $S$ が回文ならば `Yes`を出力し、そうでないならば `No` を出力してください。
"""

S = input()
reversed_S = reversed(S)

kaibun_flag = True
for s, r in zip(S, reversed_S):
    if s != r:
        kaibun_flag = False
        break
    
print("Yes") if kaibun_flag else print("No")