"""
https://algo-method.com/tasks/848

### 問題文
$N$ 両の車両からなる列車の模型があります。
模型の各車両には $0$ から $N-1$ までの番号が付けられています。
各車両は、前方と後方に、他の $1$ 両の車両と接続できる機構を持っています。
車両を連結させることで、下図のように連結列車が構成されます。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F25e9060c-e647-4184-ba61-70451c570241%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-04-01+16.29.17.png)
はじめ、$N$ 個の車両はすべて分離している状態です。
その状態から開始して $Q$ 回のクエリが与えられます。
----
- **Connect($p, q$)**：車両 $p$ の前方に車両 $q$ をつなぎます
- **Contract($r$)**：車両 $r$ を分離します。車両 $r$ の前方と後方にそれぞれほかの車両がつながっているときは、それらの車両の前後をつないでください。車両 $r$ の前後にどの車両もつながっていないときは、何もしません
----
これらのクエリがすべて終了したとき、各車両はいくつかの連結列車に分かれた状態となります。
車両 $0$ を含む連結列車の車両数を答えてください。
なお **Connect($p, q$)** クエリが与えられるとき、
車両 $p$ の前方にも、車両 $q$ の後方にもほかの車両がつながっていないことが保証されるものとします。
さらに車両 $p, q$ が異なる連結列車に属することも保証されるものとします。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F24ab7740-0ed2-4833-b480-f9462b5da001%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-04-01+16.39.28.png)
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $Q$
$query_0$
$query_1$
$\vdots$
$query_{Q-1}$
```
各 $query$ は、次のいずれかの形式で与えられます。
```IOExample
$0$ $p$ $q$
```
```IOExample
$1$ $r$
```
- 先頭が $0$ の入力データは、クエリ **Connect($p, q$)** を表します
- 先頭が $1$ の入力データは、クエリ **Contract($r$)** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $Q$ は $1$ 以上 $1000$ 以下の整数
- 各クエリにおいて、$p, q, r$ は $0$ 以上 $N-1$ 以下の整数
- 各 **Connect** クエリによって、$p, q$ は問題文中に言及した制約を満たす
### 出力
答えを出力してください。
"""

N, Q = map(int, input().split())


class Node:
    def __init__(self, value="DUMMY_DATA") -> None:
        self.nex = None
        self.prev = None
        self.value = value

# 自己参照型で試したけどうまくいかなかったため別の解法でやる

# class LinkedList:
#     def __init__(self, nil) -> None:
#         self.nil = nil

#     def connect(self, p, q):
        
#         # # 初回または先頭に追加する時だけ
#         # # 先頭に追加する条件->self.nil.nex.value == q.value
#         # if self.nil.nex.value == q.value:
#         #     self.nil.nex = p
#         # #末尾に追加する条件
#         # elif self.prev.value == p.value:
#         #     self.nil.prev = q
#         # p.nex = q
#         # # 初回または先頭に追加する時だけ
#         # if self.nil.nex.value == q.value:
#         #     p.prev = self.nil
#         # elif self.prev.value == p.value:
#         #     q.nex = self.nil
#         # q.prev = p

#     def contract(self, r):
#         target = r
#         target.prev, target.nex = target.nex, target.prev
#         del target


# nil = Node()
# nil.nex = nil
# nil.prev = nil
# l = LinkedList(nil)

# for _ in range(Q):
#     query = list(map(int, input().split()))
#     query_type = query[0]
#     if query_type == 0:
#         p = Node(query[1])
#         q = Node(query[2])
#         l.connect(p, q)
#     elif query_type == 1:
#         r = Node(query[1])
#         l.contract(r)


nex = [-1 for _ in range(N)]
bak = [-1 for _ in range(N)]


for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]

    if query_type == 0:
        p, q = query[1], query[2]
        nex[p] = q
        bak[q] = p

    elif query_type == 1:
        r = query[1]
        if nex[r] != -1:
            bak[nex[r]] = bak[r]
        if bak[r] != -1:
            nex[bak[r]] = nex[r]
        nex[r] = -1
        bak[r] = -1

# ここが少し納得がいかない
ans, now = 0, 0
while now != -1:
    ans += 1
    now = nex[now]
now = 0
while now != -1:
    ans += 1
    now = bak[now]
ans -= 1
print(ans)