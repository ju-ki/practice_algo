"""
https://algo-method.com/tasks/844

### 問題文
今回は**連結リスト**を用いて解ける問題を解きます。
**連結リスト**とは、下図のように、各要素をポインタとよばれる「矢印」によって 1 列に繋いだものです。
各ノードに対して、「次のノードはどれか」を表すポインタをもたせます。下図の場合、
- 「佐藤」ノー ドの次が「鈴木」ノードで
- その次が「高橋」ノードで
- その次が「伊藤」ノー ドで
- その次が「山本」ノードで
- 「山本」ノード の次は何もない状態となっています。
なお、何もないことを表すダミーノード `nil` (**番兵**とも呼びます) を用意しています。
`nil` の次のノードは、先頭のノード「佐藤」となっています。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F03bcb6e1-9f26-46ca-b42c-ccc853bc9a90%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-03-27+10.26.28.png)
連結リストが空であるとは、ダミーノード `nil` しかない状態を言います。
その状態で、「山本」ノードを挿入すると、下図のようになります。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F68f97d01-acd4-4c99-b11e-29c52daf8c8d%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-03-27+15.29.42.png)
続けてさらに、
- `nil` の直後に「伊藤」ノードを挿入する
- `nil` の直後に「高橋」ノードを挿入する
- `nil` の直後に「鈴木」ノードを挿入する
- `nil` の直後に「佐藤」ノードを挿入する
という挿入操作を順に行うことで、最初の図に示した連結リストが作れます。
以上の手順を参考にして、連結リストを構築してください。
具体的には、空の連結リスト (`nil` のみがある状態) から開始して、$Q$ 回のクエリが与えられます。
それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **Insert($S$)**：文字列 $S$ を新たに挿入してください (`nil` の直後に挿入してください)
- **Output($k$)**：連結リストを先頭ノード (`nil` の直後のノード) から開始して $k$ 個分の文字列を順に一行に出力してください。ただし途中で `nil` ノードに到達した場合は処理を打ち切ります
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
$1$ $k$
```
- 先頭が $0$ の入力データは、クエリ **Insert($S$)** を表します
- 先頭が $1$ の入力データは、クエリ **Output($k$)** を表します
また、入力される値は次の制約を満たします。
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- $S$ は英小文字のみからなる $1$ 文字以上 $10$ 文字以下の文字列
- $k$ は $1$ 以上 $10$ 以下の整数
- **Output** クエリの $k$ の総和は $2 \times {10}^5$ 以下
- **Output** クエリが少なくとも $1$ つ存在する
- $query_0$ は **Insert** のクエリである
### 出力
各 **Output** クエリに対して一行ずつ出力してください。
"""

Q = int(input())

# color_list = []
# for _ in range(Q):
#     query = list(map(str, input().split()))
#     if int(query[0]) == 0:
#         color_list.append(query[1])
#     else:
#         idx = int(query[1])
#         print(*reversed(color_list[-idx:]))


class Node:
    def __init__(self, value="") -> None:
        self.nex = None
        self.value = value


nil = Node()
nil.nex = nil


def insert(v):
    v.nex = nil.nex
    nil.nex = v


for _ in range(Q):
    query = list(map(str, input().split()))
    if query[0] == "0":
        v = Node(query[1])
        insert(v)
    else:
        v = nil
        for _ in range(int(query[1])):
            v = v.nex
            if v == nil:
                break
            print(v.value, end=" ")
        print()