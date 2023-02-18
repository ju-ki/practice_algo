"""
https://algo-method.com/tasks/882

### 問題文
カメのアルルは普段 ToDo リストを作ってタスクを管理しています。
アルルは ToDo リストが空である状態から開始して、$Q$ 回の操作を行いました。
$i$ 回目の操作は次のいずれかです。
#### **Set($S_i$)**
新しくタスク $S_i$ を ToDo リストにセットします。
#### **Do()**
ToDo リストの中のタスクのうち**最もはやく追加されたもの**を消化します。
このとき消化したタスクを出力してください。
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
$0$ $S_i$
```
```IOExample
$1$
```
- 先頭が $0$ の入力データは、クエリ **Set($S_i$)** を表します
- 先頭が $1$ の入力データは、クエリ **Do()** を表します
また、入力される値は次の制約を満たします。
- $Q$ は $1$ 以上 ${10}^5$ 以下の整数
- **Set** クエリにおいて、$S_i$ は英小文字からなる、長さ $1$ 以上 $10$ 以下の文字列
- **Do** クエリが呼ばれるとき、ToDo リストには $1$ つ以上のタスクが残っている
### 出力
答えを出力してください。
"""

# O(N**2)だからと思ったからTLEになると思ったけど通った
# ライブラリ使った方がいいかもしれない
Q = int(input())
task_list = []

for _ in range(Q):
    query = list(map(str, input().split()))
    query_type = query[0]
    if query_type == "0":
        task_list.append(query[1])
    elif query_type == "1":
        print(task_list.pop(0))