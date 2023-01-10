"""
https://algo-method.com/tasks/1065

### 問題文
縦 $H$ マス、横 $W$ マスからなるマス目上の地図があります。
各マスには英小文字のいずれかが描かれています。
この地図の、上から $x$ マス目、左から $y$ マス目を中心とした
縦横 $3$ マスを表示するプログラムを作成してください。
ただし、左上のマスを上から $0$ マス目、左から $0$ マス目であるとします。
たとえば下図のマス目において、上から $3$ マス目、左から $2$ マス目を指定すると、
塗りつぶした部分を表示するようにします。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F1a1f71f9-98bd-4159-b662-d0d70416cef0%2Fzoom_1.png)
### 入力
入力は次の形式で与えられます。
```IOExample
$H W x y$
$S_0$
$S_1$
$\vdots$
$S_{H-1}$
```
また、入力される値は次の制約を満たします。
- $H, W$ は $3$ 以上 $100$ 以下の整数
- $x$ は $1$ 以上 $H-2$ 以下の整数
- $y$ は $1$ 以上 $W-2$ 以下の整数
- $S_i$ は 英小文字からなる長さ $W$ の文字列 $(0 \leq i \leq H-1)$
### 出力
答えを出力してください。
"""

H, W, x, y = map(int, input().split())
S = [list(input()) for _ in range(H)]

for num_x in range(x-1, x+2):
    for num_y in range(y-1, y+2):
        print(S[num_x][num_y], end="")
    print()