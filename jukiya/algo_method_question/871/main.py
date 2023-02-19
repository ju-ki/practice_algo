"""
https://algo-method.com/tasks/871

### 問題文
$N$ 人が SNS を使用しています。各ユーザーは $0, 1, \dots, N-1$ と番号付けられています。
この SNS ではフォロー関係は一方向的です。
ユーザー $x$ がユーザー $y$ をフォローしても、ユーザー $y$ がユーザー $x$ をフォローするとは限りません。
どのユーザーも誰もフォローしていない状態から開始して、$Q$ 回のクエリが与えられました。
それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **Follow($x, y$)**：ユーザー $x$ がユーザー $y$ をフォローします。もともとフォローしている場合は何もしません
- **Unfollow($x, y$)**：ユーザー $x$ がユーザー $y$ のフォローを外します。もともとフォローしていない場合は何もしません
- **CountSameFollowers($z$)**：ユーザー $z$ のフォロワーとまったく同一のフォロワーをもつユーザーの人数 (ユーザー $z$ 自身は含めない) を答えてください
なお、ユーザー $x$ とユーザー $y$ が同一のフォロワーをもつとは、
ユーザー $x$ をフォローしているユーザーの集合と、ユーザー $y$ をフォローしているユーザーの集合が一致することを言います。
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
- 先頭が $2$ の入力データは、クエリ **CountSameFollowers($z$)** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $Q$ は $1$ 以上 $1000$ 以下の整数
- 各クエリで $x, y, z$ は $0$ 以上 $N-1$ 以下の整数
- 各クエリで $x \neq y$
### 出力
各 **CountSameFollowers** クエリに対して、答えを一行ずつ出力してください。
"""

from collections import defaultdict

N, Q = map(int, input().split())

follower_list = [[0 for _ in range(N)] for _ in range(N)]

counter_list = defaultdict(int)

for follower_arr in follower_list:
    counter_list[tuple(follower_arr)] += 1


for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]
    if query_type == 0:
        x, y = query[1], query[2]

        if follower_list[y][x] == 0:
            counter_list[tuple(follower_list[y])] -= 1
            follower_list[y][x] = 1
            counter_list[tuple(follower_list[y])] += 1
    elif query_type == 1:
        x, y = query[1], query[2]
        if follower_list[y][x] == 1:
            counter_list[tuple(follower_list[y])] -= 1
            follower_list[y][x] = 0
            counter_list[tuple(follower_list[y])] += 1
    elif query_type == 2:
        z = query[1]
        print(counter_list[tuple(follower_list[z])] - 1)