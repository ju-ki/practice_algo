"""
https://algo-method.com/tasks/842

### 問題文
縦のサイズが $H$、横のサイズが $W$ のマス目に区切られた盤面があります。
各マス目は白色か黒色のいずれかに塗られています。
その入力データは、文字を $H \times W$ の長方形形状に並べたものとして与えられます。
文字 `.` は対応するマスが白色であることを表し、
文字 `#` は対応するマスが黒色であることを表します
この盤面において、$Q$ 回のクエリが与えられました。
各クエリでは、マス $(p, q)$ が与えられますので、そのマスの上下左右全体に何個の黒色マスがあるかを答えてください。
なお、上から $p$ 行目 ($0$ 始まり)、左から $q$ 列目 ($0$ 始まり) のマスを $(p, q)$ と表すことにします。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F8ec16b60-b38c-4aed-a51e-18f94d2eb28e%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-03-21+10.15.01.png)
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
各 $query$ は、次の形式で与えられます。
```IOExample
$p$ $q$
```
また、入力される値は次の制約を満たします。
- $H, W$ は $1$ 以上 $2 \times {10}^5$ 以下の整数
- $H \times W$ は $1$ 以上 $2 \times {10}^5$ 以下の整数
- $S_i$ は `.` と `#` のみからなる長さ $W$ の文字列 $(0 \leq i \leq H - 1)$
- $Q$ は $1$ 以上 $2 \times {10}^5$ 以下の整数
- $p$ は $0$ 以上 $H-1$ 以下の整数
- $q$ は $0$ 以上 $W-1$ 以下の整数
### 出力
答えを出力してください。
"""

H, W = map(int, input().split())
S = [input() for _ in range(H)]
Q = int(input())

# クエリが呼び出されるたびに全ての配列を呼び出しているからTLE
# for _ in range(Q):
#     counter = 0
#     p, q = map(int, input().split())
#     for sp in S[p]:
#         if sp == "#":
#             counter += 1
#     for s in S:
#         if s[q] == "#":
#             counter += 1
#     if S[p][q] == "#":
#         counter -= 1
#     print(counter)


# あらかじめ#が何個あるか行、列共に求めておく
sum_row = [0 for _ in range(H)]
sum_columns = [0 for _ in range(W)]


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            sum_row[i] += 1

for j in range(W):
    for i in range(H):
        if S[i][j] == "#":
            sum_columns[j] += 1

for _ in range(Q):
    counter = 0
    p, q = map(int, input().split())
    if S[p][q] == "#":
        counter = sum_row[p] + sum_columns[q] - 1
    else:
        counter = sum_row[p] + sum_columns[q]
    print(counter)