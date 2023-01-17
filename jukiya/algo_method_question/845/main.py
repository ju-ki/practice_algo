"""
https://algo-method.com/tasks/845

### 問題文
今回は連結リストを用いて、[スタック](https://algo-method.com/descriptions/157)を実装します。
連結リストとは、下図のように、各要素をポインタとよばれる「矢印」によって 1 列に繋いだものです。
なお、何もないことを表すダミーノード `nil` を用意しています。
連結リストが空であるとは、ダミーノード `nil` しかない状態を言います。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F2488c1f1-bd48-4165-b4e2-50641f850b87%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-03-27+23.14.58.png)
今、空の連結リスト (`nil` のみがある状態) から開始して、$Q$ 回のクエリが与えられます。
それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **PushHead($S$)**：文字列 $S$ 表すノードを先頭 (`nil` の直後) に挿入してください
- **PopHead()**：先頭 (`nil` の直後) のノードの文字列を出力して、そのノードを削除してください。ただし連結リストが空である場合は `Error` と出力してください
### 入力
入力は次の形式で与えられます。
```IOExample
$Q$
$query_0$
$query_1$
$\vdots$
$query_{Q-1}$
```
各 $query$ は、次のいずれかの形式で与えられます。
```IOExample
$0$ $S$
```
```IOExample
$1$
```
- 先頭が $0$ の入力データは、クエリ **PushHead($S$)** を表します
- 先頭が $1$ の入力データは、クエリ **PopHead()** を表します
また、入力される値は次の制約を満たします。
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- $S$ は英小文字のみからなる $1$ 文字以上 $10$ 文字以下の文字列
- **PopHead** クエリが少なくとも $1$ つ存在する
### 出力
各クエリに答えてください。
"""
from typing import Any
Q = int(input())


class Node:
    def __init__(self, value: Any = "") -> None:
        self.nex = None
        self.value = value


nil = Node()
nil.nex = nil


def insert(v: Node = None):
    v.nex = nil.nex
    nil.nex = v


def remove():
    front = nil.nex
    nil.nex = front.nex
    del front


for _ in range(Q):
    query = list(map(str, input().split()))
    if query[0] == "0":
        v = Node(query[1])
        insert(v)
    else:
        if nil.nex.value != "":
            print(nil.nex.value)
        else:
            print("Error")
        remove()