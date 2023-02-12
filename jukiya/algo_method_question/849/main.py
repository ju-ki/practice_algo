"""
https://algo-method.com/tasks/849

### 問題文
$N$ 人がマラソン大会に参加しています。各人には $0, 1, \dots, N-1$ のエントリー番号が付けられています。
ある時点で、$1$ 位から順に、$A_0, A_1, \dots, A_{N-1}$ となっていました。
つまり先頭から $i$ 番目 (先頭を $0$ 番目とする) のランナーの番号は $A_i$ でした。
この状態から開始して、以下の $Q$ 個の現象が観測されました。
それぞれのクエリに答えてください。
- **Overtake($v$)**：ランナー $v$ が自分の前を走っている人を追い抜きました。このとき追い抜いたランナーの番号を答えてください。ただしランナー $v$ がすでに棄権していたり、前に誰もいないときは `Error` と出力してください
- **Dropout($v$)**：ランナー $v$ が棄権しました。ランナーの人数が $1$ 人減ります
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0$ $A_1$ $\dots$ $A_{N-1}$
$Q$
$query_0$
$query_1$
$\vdots$
$query_{Q-1}$
```
各 $query$ は、次のいずれかの形式で与えられます。
```IOExample
$0$ $v
```
```IOExample
$1$ $v$
```
- 先頭が $0$ の入力データは、クエリ **Overtake($v$)** を表します
- 先頭が $1$ の入力データは、クエリ **Dropout($v$)** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^5$ 以下の整数
- $A_0, A_1, \dots, A_{N-1}$ は $0, 1, \dots, N-1$ を並び替えたものである
- $Q$ は $1$ 以上 $10^5$ 以下の整数
- 各クエリにおいて $v$ は $0$ 以上 $N-1$ 以下の整数
- **Overtake** のクエリが少なくとも $1$ つ存在する
### 出力
答えを出力してください。
"""


# TLE:恐らく要素の取得に時間がかかっている説(恐らく正解であると思う)
class Node:
    def __init__(self, value="DUMMY_DATA") -> None:
        self.nex = None
        self.prev = None
        self.value = value


class pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class LinkedList:
    def __init__(self, nil) -> None:
        self.nil = nil
        self.head = None
        self.tail = None

    def push_head(self, v):
        v.nex = self.nil.nex
        self.nil.nex = v
        v.prev = self.nil
        v.nex.prev = v
        if self.tail is None:
            self.tail = v
        self.head = v

    def push_tail(self, v):
        v.prev = self.nil.prev
        self.nil.prev = v
        v.nex = self.nil
        v.prev.nex = v
        if self.tail is None:
            self.head = v
        self.tail = v

    def pop_head(self):
        head = self.nil.nex
        if head == self.nil:
            return "Error"
        self.nil.nex = head.nex
        self.head = head.nex
        (head.nex).prev = self.nil
        ret = head.value
        del head
        return ret

    def pop_tail(self):
        tail = self.nil.prev
        if tail == self.nil:
            return "Error"
        self.nil.prev = tail.prev
        self.tail = tail.prev
        (tail.prev).nex = self.nil
        ret = tail.value
        del tail
        return ret

    def find(self, first=None, second=None):
        if first is not None and second is not None:
            temp = self.nil
            temp = temp.nex
            while temp.value != "DUMMY_DATA":
                if temp.value == first.value:
                    first = temp
                if temp.value == second.value:
                    second = temp
                temp = temp.nex
            return first, second

        if first is None:
            temp = self.nil
            temp = temp.nex
            while temp.value != "DUMMY_DATA":
                if temp.value == second.value:
                    first = temp.prev
                    second = temp
                temp = temp.nex
        elif second is None:
            temp = self.nil
            temp = temp.nex
            while temp.value != "DUMMY_DATA":
                if temp.value == first.value:
                    first = temp
                    second = temp.nex
                temp = temp.nex
        return first, second

    def swap(self, x=None, y=None):
        if self.head.value == "DUMMY_DATA" or self.head.nex.value == "DUMMY_DATA" or x == y:
            return "Error"
        node1, node2 = self.find(x, y)
        if node1 is None or node2 is None or node1.value == "DUMMY_DATA":
            return "Error"
        ret = node1
        if node1 == self.head:
            self.head = node2
        elif node2 == self.head:
            self.head = node1
        if node1 == self.tail:
            self.tail = node2
        elif node2 == self.tail:
            self.tail = node1

        temp = None
        temp = node1.nex
        node1.nex = node2.nex
        node2.nex = temp

        if node1.nex is not None:
            node1.nex.prev = node1
        if node2.nex is not None:
            node2.nex.prev = node2

        temp = node1.prev
        node1.prev = node2.prev
        node2.prev = temp

        if node1.prev is not None:
            node1.prev.nex = node1
        if node2.prev is not None:
            node2.prev.nex = node2
        return ret.value

    def erase(self, v):
        current = self.nil
        current = current.nex
        while current.value != "DUMMY_DATA":
            if current.value == v.value:
                current_node = current
                current_node.prev.nex = current_node.nex
                current_node.nex.prev = current_node.prev
                del current_node
                break
            current = current.nex

    def print_node(self, N):
        current = self.nil
        current = current.nex
        while current.value != "DUMMY_DATA":
            print(str(current.value) + "=>", end="")
            current = current.nex
        print()

        # for _ in range(N):
        #     print(str(current.value) + "=>", end="")
        #     current = current.nex
        # print()

        # current = self.nil
        # current = current.prev
        # for _ in range(N):
        #     print(str(current.value) + "=>", end="")
        #     current = current.prev
        # print()

    def debug(self):
        print("Current Head: " + self.head.value)
        print("Current Tail: " + self.tail.value)



N = int(input())
A = list(map(int, input().split()))

nil = Node()
nil.nex = nil
nil.prev = nil
l = LinkedList(nil)

for a in A:
    v = Node(a)
    l.push_tail(v)

Q = int(input())


for i in range(Q):
    query_type, runner = map(int, input().split())
    if query_type == 0:
        v = Node(runner)
        print(l.swap(x=None, y=v))
    elif query_type == 1:
        v = Node(runner)
        l.erase(v)
