"""
https://algo-method.com/tasks/839

### 問題文
$N$ 人が SNS を使用しています。各ユーザーは $0, 1, \dots, N-1$ と番号付けられています。
この SNS ではフォロー関係は一方向的です。
ユーザー $x$ がユーザー $y$ をフォローしても、ユーザー $y$ がユーザー $x$ をフォローするとは限りません。
どのユーザーも誰もフォローしていない状態から開始して、$Q$ 回のクエリが与えられました。
それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **Follow($x, y$)**：ユーザー $x$ がユーザー $y$ をフォローします。もともとフォローしている場合は何もしません
- **Unfollow($x, y$)**：ユーザー $x$ がユーザー $y$ のフォローを外します。もともとフォローしていない場合は何もしません
- **CountFollowers($z$)**：ユーザー $z$ をフォローしている人が何人いるかを答えてください
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
$0$ $x$ $y$
```
```IOExample
$1$ $x$ $y$
```
```IOExample
$2$ $z$
```
- 先頭が $0$ の入力データは、クエリ **Follow($x, y$)** を表します
- 先頭が $1$ の入力データは、クエリ **Unfollow($x, y$)** を表します
- 先頭が $2$ の入力データは、クエリ **CountFollowers($z$)** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $5000$ 以下の整数
- $Q$ は $1$ 以上 $10^{5}$ 以下の整数
- 各クエリで $x, y, z$ は $0$ 以上 $N-1$ 以下の整数
- 各クエリで $x \neq y$
- **CountFollowers** のクエリが少なくとも $1$ つ存在する
### 出力
各 **CountFollowers** クエリに対して、答えを一行ずつ出力してください。
"""

# 最初のアイデア
# [[] * N]の二次元配列を作成して、内側のリストにフォローした人を追加していく予定だった
# なぜかfollow_list[0].append(1)とすると全部の配列に1が追加された


N, Q = map(int, input().split())

follow_list = [[0 for _ in range(N)] for _ in range(N)]
counter_list = [0] * N


for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]

    if query_type == 0:
        x, y = query[1], query[2]
        if follow_list[x][y] == 0:
            follow_list[x][y] = 1
            counter_list[y] += 1
    elif query_type == 1:
        x, y = query[1], query[2]
        if follow_list[x][y] == 1:
            follow_list[x][y] = 0
            counter_list[y] -= 1
    elif query_type == 2:
        print(counter_list[query[1]])