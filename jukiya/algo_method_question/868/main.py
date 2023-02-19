"""
https://algo-method.com/tasks/868

### 問題文
$N$ 個の文字列 $S_0, S_1, \ldots, S_{N-1}$ が与えられます。
このデータ構造に対して、$Q$ 回のクエリが与えられます。それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **Insert($T$)**：列の末尾に文字列 $T$ を挿入してください
- **Delete($T$)**：列に含まれる文字列 $T$ をすべて削除してください
- **Count($T$)**：列に含まれる文字列 $T$ の個数を出力してください
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
$0$ $T$
```
```IOExample
$1$ $T$
```
```IOExample
$2$ $T$
```
- 先頭が $0$ の入力データは、クエリ **Insert($T$)** を表します
- 先頭が $1$ の入力データは、クエリ **Delete($T$)** を表します
- 先頭が $2$ の入力データは、クエリ **Count($T$)** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^{5}$ 以下の整数
- $A_i$ は英小文字のみからなる長さ $10$ 以下の文字列 $(0 \leq i \leq N-1)$
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- 各クエリにおいて $T$ は英小文字のみからなる長さ $10$ 以下の文字列
### 出力
答えを出力してください。
"""

N = int(input())
A = list(input().split())
Q = int(input())
count_dict = {}

for a in A:
    count_dict[a] = count_dict.get(a, 0) + 1

for _ in range(Q):
    query_type, word = map(str, input().split())
    if query_type == "0":
        count_dict[word] = count_dict.get(word, 0) + 1
    elif query_type == "1":
        count_dict[word] = 0
    elif query_type == "2":
        print(count_dict.get(word, 0))
