"""
https://algo-method.com/tasks/832

### 問題文
$N$ 個の整数からなる整数列 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
このデータ構造に対して、$Q$ 回のクエリが与えられます。それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **PushFront($v$)**：整数値 $v$ が与えられるので、数列の**先頭**に整数 $v$ を挿入してください
- **PopFront()**：数列の**先頭**の整数値を出力し、さらに数列の**先頭**の値を削除してください。ただし数列が空の状態でこのクエリが呼ばれたときは `Error` と出力してください。このとき数列には何もしません
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
$1$
```
- 先頭が $0$ の入力データは、クエリ **PushFront($v$)** を表します
- 先頭が $1$ の入力データは、クエリ **PopFront()** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $A_i$ は $0$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
- $Q$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $v$ は $0$ 以上 $100$ 以下の整数
- **Pop** のクエリが少なくとも $1$ つ存在する
### 出力
各クエリに対して一行ずつ答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
A.reverse()
Q = int(input())


for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        A.append(query[1])
    else:
        if len(A) == 0:
            print("Error")
        else:
            print(A.pop())
