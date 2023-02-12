"""
https://algo-method.com/tasks/847

### 問題文
今回は**双方向連結リスト**を用いて、**デック**を実装します。
デックは、スタックとキューの機能を兼ね備えたものです。
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
- **PushTail($S$)**：文字列 $S$ 表すノードを**末尾**に挿入してください
- **PopHead()**：**先頭**のノードの文字列を出力して、そのノードを削除してください。ただし連結リストが空である場合は `Error` と出力してください
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
$1$ $S$
```
```IOExample
$2$
```
```IOExample
$3$
```
- 先頭が $0$ の入力データは、クエリ **PushHead($S$)** を表します
- 先頭が $1$ の入力データは、クエリ **PushTail($S$)** を表します
- 先頭が $2$ の入力データは、クエリ **PopHead()** を表します
- 先頭が $3$ の入力データは、クエリ **PopTail()** を表します
また、入力される値は次の制約を満たします。
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- $S$ は英小文字のみからなる $1$ 文字以上 $10$ 文字以下の文字列
- **PopTail** または **PopTail** クエリが少なくとも $1$ つ存在する
### 出力
各クエリに答えてください。
"""


class Node:
    def __init__(self, value="DUMMY_DATA") -> None:
        self.nex = None
        self.prev = None
        self.value = value


class LinkedList:
    def __init__(self, nil) -> None:
        self.nil = nil

    def push_head(self, v):
        v.nex = self.nil.nex
        self.nil.nex = v
        v.prev = self.nil
        v.nex.prev = v

    def push_tail(self, v):
        v.prev = self.nil.prev
        self.nil.prev = v
        v.nex = self.nil
        v.prev.nex = v

    def pop_head(self):
        head = self.nil.nex
        if head == self.nil:
            return "Error"
        self.nil.nex = head.nex
        (head.nex).prev = self.nil
        ret = head.value
        del head
        return ret

    def pop_tail(self):
        tail = self.nil.prev
        if tail == self.nil:
            return "Error"
        self.nil.prev = tail.prev
        (tail.prev).nex = self.nil
        ret = tail.value
        del tail
        return ret


# init
nil = Node()
nil.prev = nil
nil.nex = nil


Q = int(input())
l = LinkedList(nil)

for _ in range(Q):
    query = list(map(str, input().split()))
    query_type = query[0]
    if query_type == "0":
        v = Node(query[1])
        l.push_head(v)
    elif query_type == "1":
        v = Node(query[1])
        l.push_tail(v)
    elif query_type == "2":
        answer = l.pop_head()
        print(answer)
    elif query_type == "3":
        answer = l.pop_tail()
        print(answer)