"""
https://algo-method.com/tasks/1066

### 問題文
ライフゲームは、$2$ 次元のグリッド上で行う生命の誕生と死のシミュレーションです。
グリッドの各マスは色が塗られているか塗られていないかのどちらかであり、色が塗られているマスは「生きているマス」、塗られていないマスは「死んでいるマス」と呼びます。
ライフゲームにおいて、各グリッドの状態はステップが進むごとに変化します。
次の図は実際にグリッドの状態が変化する様子です。この例の場合、 $3$ ステップ後にはすべてのマスが死滅してしまいます。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F3f3e3f59-487a-4492-b3a8-0b2eb090368d%2Flifegame.png)
具体的には、すべてのマスは次のルールにしたがって一斉に変化します。
----
自身に $8$ 方向に隣接しているマスのうち生きているマスの個数を $x$ とする。
次の世代における自身の状態は次のルールにしたがって決定する。
- 自身が死んでいるかつ $x=3$ ならば生きたマスとなる。
- 自身が生きているかつ $x=2 \text{ or } 3$ ならば生き続ける。
- 自身が生きているかつ $x \leq 1$ ならば過疎により死滅する。
- 自身が生きているかつ $x \geq 4$ ならば過密により死滅する。
----
縦横 $N$ マスのグリッドの初期状態の情報が $N$ 個の長さ $N$ の文字列 $S_0, S_1, \ldots, S_{N-1}$ から与えられます。
$S_{i,j}$ 文字目はグリッドの上から $i$ 行目、左から $j$ 行目の状態を表しており、
$S_{i,j}$ が `.` のときマスは白く、 `#` のときマスは黒く塗られています。
なお、与えられた縦横 $N$ マスのグリッドの外部にはマスがないものと考えることにします。
$X$ ステップ後のグリッドはどのような状態になるか答えてください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N X$
$S_0$
$S_1$
$\vdots$
$S_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $X$ は $1$ 以上 $100$ 以下の整数
- $S$ は `.` または `#` からなる長さ $N$ の文字列 $(0 \leq i \leq N-1)$
### 出力
答えを $N$ 行で出力してください。
ただし、$i$ 行目にはグリッドの上から $i$ 行目の情報を表す長さ $N$ の文字列を出力してください。
"""

N, X = map(int, input().split())
S = [list(input()) for _ in range(N)]

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def next_state(grid, counter, num_i, num_j):
    if grid[num_i][num_j] == "#" and counter >= 4:
        return "."
    elif grid[num_i][num_j] == "#" and counter <= 1:
        return "."
    elif grid[num_i][num_j] == "." and counter == 3:
        return "#"
    elif grid[num_i][num_j] == "#":
        if counter == 2 or counter == 3:
            return "#"
    else:
        return grid[num_i][num_j]


for _ in range(X):
    next_grid = [["." for _ in range(N)] for _ in range(N)]
    for num_i in range(N):
        for num_j in range(N):
            counter = 0
            for num_d in range(8):
                diff_num_i = num_i + dx[num_d]
                diff_num_j = num_j + dy[num_d]
                if 0 <= diff_num_i < N and 0 <= diff_num_j < N:
                    if S[diff_num_i][diff_num_j] == "#":
                        counter += 1
            next_grid[num_i][num_j] = next_state(S, counter, num_i, num_j)
    S = next_grid

for i in range(N):
    for j in range(N):
        print(S[i][j], end="")
    print()
