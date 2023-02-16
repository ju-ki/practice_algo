"""
https://algo-method.com/tasks/858

### 問題文
$N$ 個の整数列 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
このデータ構造に対して、$Q$ 回のクエリが与えられます。それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **Insert($v$)**：数列の末尾に整数 $v$ を挿入してください
- **Delete($v$)**：数列に含まれる整数 $v$ をすべて削除してください
- **Count($v$)**：数列に含まれる整数 $v$ の個数を出力してください
これらのクエリの実行例については、入力例 1・出力例 1 を参考にしてください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
$Q$
$query_0$
$query_1$
$\vdots$
$query_{Q-1}$
```
各 $query$ は、次のいずれかの形式で与えられます。
```IOExample
$0$ $v$
```
```IOExample
$1$ $v$
```
```IOExample
$2$ $v$
```
- 先頭が $0$ の入力データは、クエリ **Insert($v$)** を表します
- 先頭が $1$ の入力データは、クエリ **Delete($v$)** を表します
- 先頭が $2$ の入力データは、クエリ **Count($v$)** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^{5}$ 以下の整数
- $A_i$ は $1$ 以上 $10^5$ 以下の整数 $(0 \leq i \leq N-1)$
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- 各クエリにおいて $v$ は $1$ 以上 $10^5$ 以下の整数
- **Count** クエリが少なくとも $1$ つ存在する
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
max_A = max(A)
count_list = [0] * (10 ** 5 + 1)

for a in A:
    count_list[a] += 1


for _ in range(Q):
    query_type, v = map(int, input().split())
    if query_type == 0:
        count_list[v] += 1
    elif query_type == 1:
        count_list[v] = 0
    elif query_type == 2:
        print(count_list[v])