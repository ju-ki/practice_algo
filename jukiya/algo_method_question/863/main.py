"""
https://algo-method.com/tasks/863

### 問題文
$N$ 個の整数からなる整数列 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
この整数列に対して、$Q$ 回のクエリが与えられます。それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **Insert($v$)**：数列の末尾に整数 $v$ を挿入してください
- **Change($x, y$)**：数列に含まれる整数 $x$ をすべて整数 $y$ に書き換えてください
- **Sum()**：数列中の整数の総和を答えてください
これらのクエリの実行例については、入力例 1・出力例 1 を参考にしてください。
なお、計算途中の数値が **32bit 整数型に収まらない可能性** があることに注意してください。
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
$1$ $x$ $y$
```
```IOExample
$2$
```
- 先頭が $0$ の入力データは、クエリ **Insert($v$)** を表します
- 先頭が $1$ の入力データは、クエリ **Change($x, y$)** を表します
- 先頭が $2$ の入力データは、クエリ **Sum()** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $A_i$ は $1$ 以上 $10^5$ 以下の整数 $(0 \leq i \leq N-1)$
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- 各クエリにおいて $v, x, y$ は $1$ 以上 $10^5$ 以下の整数
- **Change** クエリにおいて $x \neq y$
- **Sum** クエリが少なくとも $1$ つ含まれる
### 出力
答えを出力してください。
"""


N = int(input())
A = list(map(int, input().split()))
max_A = max(A)
Q = int(input())
count_list = [0] * (10 ** 5 + 1)
total = 0

for a in A:
    count_list[a] += 1
    total += a

for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]
    if query_type == 0:
        count_list[query[1]] += 1
        total += query[1]
    elif query_type == 1:
        x, y = query[1], query[2]
        total += y * count_list[x]
        count_list[y] += count_list[x]
        total -= x * count_list[x]
        count_list[x] = 0
    elif query_type == 2:
        print(total)