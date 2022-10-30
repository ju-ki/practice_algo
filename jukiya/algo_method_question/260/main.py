"""
https://algo-method.com/tasks/260

### 問題文
$N$ 個の文字列 $S_0, S_1, \dots, S_{N-1}$ が与えられます。
これらの $N$ 個の文字列の中に同じ $2$ つの文字列があるかどうかを判定するプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$S_0$
$S_1$
$\vdots$
$S_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $S_i$ は英小文字からなる長さ $1$ 以上 $100$ の文字列 $(0 \leq i \leq N-1)$
### 出力
同じ文字列が含まれていれば `Yes` を出力し、含まれていなければ `No` を出力してください。
"""

N = int(input())
text_list = []
contain_flag = False

for _ in range(N):
    text = input()
    if text in text_list:
        contain_flag = True
        break
    else:
        text_list.append(text)


print("Yes") if contain_flag else print("No")
