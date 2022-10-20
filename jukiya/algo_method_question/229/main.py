"""
https://algo-method.com/tasks/229

### 問題文
英小文字からなる文字列 $S$ (長い) と $T$ (短い) が与えられます。
文字列 $S$ の中に、文字列 $T$ が含まれるかどうかを判定してください。
たとえば、次の通りです。
- `algomethod` は `go` を含みます
- `algomethod` は `met` を含みます
- `algomethod` は `ago` を含みません (`l` が挟まっています)
### 入力
入力は次の形式で与えられます。
```IOExample
$S$
$T$
```
また、入力される値は次の制約を満たします。
- $S$ は英小文字からなる長さ $100$ 以下の文字列
- $T$ は英小文字からなる長さ $100$ 以下の文字列
- $S$ の長さは $T$ の長さ以上である
### 出力
一致させることができるならば `Yes` を出力し、できないならば `No` を出力してください。
"""

S = input()
T = input()
s_length = len(S)
t_length = len(T)
contain_flag = False

for i in range(s_length - t_length+1):
    if S[i:i+t_length] == T:
        contain_flag = True
        break
print("Yes") if contain_flag else print("No")