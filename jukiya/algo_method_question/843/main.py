"""
https://algo-method.com/tasks/843

### 問題文
縦のサイズが $H$、横のサイズが $W$ のマス目に区切られた盤面があります。
各マス目は白色か黒色のいずれかに塗られています。
その入力データは、文字を $H \times W$ の長方形形状に並べたものとして与えられます。
文字 `.` は対応するマスが白色であることを表し、
文字 `#` は対応するマスが黒色であることを表します
この盤面において、$Q$ 回のクエリが与えられました。
それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **Push($p, q$)**：マス $(p, q)$ および、その上下左右に隣接するマス (盤外を除く) の白色と黒色を反転させます
- **GetNum()**：盤面全体の黒色の個数を答えてください
なお、上から $p$ 行目 ($0$ 始まり)、左から $q$ 列目 ($0$ 始まり) のマスを $(p, q)$ と表すことにします。
たとえば下図左の盤面に対して、**Push($1, 2$)** を適用すると下図のようになります。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F5d9bdf55-e36b-4baf-9399-3ec6279ded6a%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-03-21+14.02.53.png)
さらに続けて **Push($4, 4$)** を適用すると下図のようになります。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F05f5fc91-5423-470f-8d02-c100df9e17f7%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-03-21+14.05.27.png)
この状態で **GetNum()** を呼び出すと、$9$ を返します。
### 入力
入力は次の形式で与えられます。
```IOExample
$H$ $W$
$S_0$
$S_1$
$\vdots$
$S_{H-1}$
$Q$
$query_0$
$query_1$
$\vdots$
$query_{Q-1}$
```
各 $query$ は、次のいずれかの形式で与えられます。
```IOExample
$0$ $p$ $q$
```
```IOExample
$1$
```
- 先頭が $0$ の入力データは、クエリ **Push($p, q$)** を表します
- 先頭が $1$ の入力データは、クエリ **GetNum()** を表します
また、入力される値は次の制約を満たします。
- $H, W$ は $1$ 以上 $1000$ 以下の整数
- $S_i$ は `.` と `#` のみからなる長さ $W$ の文字列
- $Q$ は $1$ 以上 ${10}^5$ 以下の整数
- $p$ は $0$ 以上 $H-1$ 以下の整数
- $q$ は $0$ 以上 $W-1$ 以下の整数
### 出力
答えを出力してください。
"""

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
Q = int(input())
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

sum_black = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            sum_black += 1

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        for (x, y) in zip(dx, dy):
            diff_x = query[1] + x
            diff_y = query[2] + y
            if 0 <= diff_x < H and 0 <= diff_y < W:
                if grid[diff_x][diff_y] == "#":
                    grid[diff_x][diff_y] = "."
                    sum_black -= 1
                else:
                    grid[diff_x][diff_y] = "#"
                    sum_black += 1
    else:
        print(sum_black)