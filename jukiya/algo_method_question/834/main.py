"""
https://algo-method.com/tasks/834

### 問題文
$N$ 個の整数からなる整数列 $A_0, A_1, \ldots, A_{N-1}$ が与えられます。
このデータ構造に対して、$Q$ 回のクエリが与えられます。それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **PushFront($v$)**：整数値 $v$ が与えられるので、数列の**先頭**に整数 $v$ を挿入してください
- **PushBack($v$)**：整数値 $v$ が与えられるので、数列の**末尾**に整数 $v$ を挿入してください
- **Get($k$)**：整数値 $k$ が与えられるので、数列の左から $k$ 番目の値を答えてください。ただし $k$ 番目の要素が数列外を参照する場合は `Error` と出力してください
**最も左の数字は左から $0$ 番目**と数えることにします。
また、これらのクエリの実行例については、入力例 1・出力例 1 を参考にしてください。
#### ヒント
可変長配列を使う場合、先頭への挿入と末尾への挿入の両方を高速に処理することは難しいです。
そこで、配列を $2$ 本用意して別々に処理してみましょう。
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
$2$ $k$
```
- 先頭が $0$ の入力データは、クエリ **PushFront($v$)** を表します
- 先頭が $1$ の入力データは、クエリ **PushBack($v$)** を表します
- 先頭が $2$ の入力データは、クエリ **Get($k$)** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $A_i$ は $0$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
- $Q$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $v$ は $0$ 以上 $100$ 以下の整数
- $k$ は $0$ 以上 $2 \times 10^{5}$ 以下の整数
- **Get** のクエリが少なくとも $1$ つ存在する
### 出力
各クエリに対して一行ずつ答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A_front = []

for _ in range(Q):
    num1, num2 = map(int, input().split())
    if num1 == 0:
        A_front.append(num2)
    elif num1 == 1:
        A.append(num2)
    else:
        try:
            if num2 < len(A_front):
                print(A_front[-(num2+1)])
            else:
                print(A[num2 - len(A_front)])
        # try:
        #     A[num2]
        except IndexError:
            print("Error")