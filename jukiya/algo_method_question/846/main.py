"""
https://algo-method.com/tasks/846

### 問題文
今回は**双方向連結リスト**を用いて、[キュー](https://algo-method.com/descriptions/157)を実装します。
双方向連結リストとは、下図のように、各要素をポインタとよばれる「矢印」によって 1 列に繋いだものです。
双方向連結リストでは、その名の通り、矢印を双方向に繋ぎます。
なお、何もないことを表すダミーノード `nil` を用意しています。
連結リストが空であるとは、ダミーノード `nil` しかない状態を言います。
また、`nil` の直後のノードは**先頭** (下図中の `head`) であるといい、
`nil` の直前のノードは**末尾** (下図の `tail`) であると言います。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F08bc8388-8241-4c41-a60d-bbe0215c8316%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-03-27+23.40.27.png)
今、空の連結リスト (`nil` のみがある状態) から開始して、$Q$ 回のクエリが与えられます。
それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **PushHead($S$)**：文字列 $S$ 表すノードを**先頭**に挿入してください
- **PopTail()**：**末尾**のノードの文字列を出力して、そのノードを削除してください。ただし連結リストが空である場合は `Error` と出力してください
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
- 先頭が $1$ の入力データは、クエリ **PopTail()** を表します
また、入力される値は次の制約を満たします。
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- $S$ は英小文字のみからなる $1$ 文字以上 $10$ 文字以下の文字列
- **PopTail** クエリが少なくとも $1$ つ存在する
### 出力
各クエリに答えてください。
"""

Q = int(input())


class Node:
    def __init__(self, value="") -> None:
        self.nex = None
        self.prev = None
        self.value = value


nil = Node()
nil.nex = nil
nil.prev = nil


def insert(v: Node = None):
    v.nex = nil.nex
    v.prev = nil
    nil.nex = v
    (v.nex).prev = v


def remove():
    back = nil.prev
    if back == nil:
        return ("Error")
    else:
        ret = back.value
        nil.prev = back.prev
        (nil.prev).nex = nil
        del back
        return (ret)


for _ in range(Q):
    query = list(map(str, input().split()))
    if query[0] == "0":
        v = Node(query[1])
        insert(v)
    else:
        print(remove())
        
N = int(input().split())
A = list(map(int, input().split()))
counter = 0

while True:
    even_flag = True
    for a in A:
        if a % 2 != 0:
            even_flag = False
            break

    if not even_flag:
        break
    else:
        A = [n//2 for n in A]
        counter += 1
print(counter)