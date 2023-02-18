"""
https://algo-method.com/tasks/888

### 問題文
`(` と `)` のみからなる文字列を括弧列と呼ぶことにします。
長さ $N$ の括弧列 $S$ が与えられますので、
$S$ が整合した括弧列であるかどうかを判定してください。
たとえば `(())()` や `()` は整合している括弧列ですが、以下は整合した括弧列ではありません。
- 括弧が開いていないのに閉じる括弧が現れる例：`)(`
- 括弧が閉じきっていない例：`(()`
<details><summary>括弧列が整合しているとは</summary><div>
括弧列 $S$ に対して、連続する $2$ 文字が `()` である箇所を除去する操作を $0$ 回以上繰り返すことで空文字にできるとき、
括弧列 $S$ は整合しているといいます
</div></details>
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^{6}$ 以下の整数
- $S$ は `(` と `)` のみからなる長さ $N$ の文字列
### 出力
括弧列 $S$ が整合しているときは `Yes`、整合していないときは `No` を出力してください。
"""

N = int(input())
S = list(input())

open_bracket = []
flag = True

for i in range(N):
    s = S[i]
    if s == "(":
        open_bracket.append(i)
    elif s == ")":
        if len(open_bracket) == 0:
            flag = False
            break
        else:
            open_bracket.pop()

if len(open_bracket) > 0:
    flag = False

print("Yes") if flag else print("No")
