"""
https://algo-method.com/tasks/887

### 問題文
`(` と `)` のみからなる文字列を括弧列と呼ぶことにします。
長さ $N$ の括弧列 $S$ が与えられます。
この括弧列は、括弧の対応関係がとれたものとなっています (厳密な定義は下で述べます)。
たとえば括弧列 `()(())` は、次の対応関係が成り立っています。
- $0$ 文字目の `(` と $1$ 文字目の `)` が対応する
- $2$ 文字目の `(` と $5$ 文字目の `)` が対応する
- $3$ 文字目の `(` と $4$ 文字目の `)` が対応する
与えられた括弧列 $S$ において、左端の括弧に対応する括弧が何文字目に相当するかを求めてください。
なお、括弧列 $S$ の左端の文字を $0$ 番目であると数えることにします。
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
- $N$ は $2$ 以上 $10^{6}$ 以下の偶数
- $K$ は $0$ 以上 $N-1$ 以下の整数
- $S$ は `(` と `)` のみからなる長さ $N$ の文字列
- $S$ は整合した括弧列である
### 出力
答えを出力してください。
"""

N = int(input())
S = list(input())
S.pop(0)
counter = 0

for i in range(N-1):
    s = S[i]
    if s == "(":
        counter += 1
    elif s == ")" and counter == 0:
        print(i+1)
        break
    elif s == ")" and counter > 0:
        counter -= 1


# stackを使ったやり方
N = int(input())
S = list(input())

open_bracket = []

answer = -1

for i in range(N):
    s = S[i]
    if s == "(":
        open_bracket.append(i)
    elif s == ")":
        left = open_bracket.pop()
        if left == 0:
            answer = i
print(answer)