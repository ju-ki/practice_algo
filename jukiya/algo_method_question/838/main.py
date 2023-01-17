"""
https://algo-method.com/tasks/838

### 問題文
$N$ 人が SNS を使用しています。各ユーザーは $0, 1, \dots, N-1$ と番号付けられています。
どのユーザーも誰もフォローしていない状態から開始して、$Q$ 回のクエリが与えられました。
それぞれのクエリに答えてください。
各クエリは、次のいずれかです。
- **Follow($x, y$)**：ユーザー $x$ がユーザー $y$ をフォローします。このとき、ユーザー $y$ がユーザー $x$ をフォローするとは限りません。また、もともとフォローしている場合は何もしません
- **GetFollowers($z$)**：ユーザー $z$ をフォローしているユーザーの番号を**小さい順に**すべて出力してください。ただしユーザー $z$ が誰にもフォローされていない場合は "No" と出力してください
これらのクエリの実行例については、入力例 1・出力例 1 を参考にしてください。
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
$1$ $z$
```
- 先頭が $0$ の入力データは、クエリ **Follow($x, y$)** を表します
- 先頭が $1$ の入力データは、クエリ **GetFollowers($z$)** を表します
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $Q$ は $1$ 以上 $1000$ 以下の整数
- 各クエリで $x, y, z$ は $0$ 以上 $N-1$ 以下の整数
- 各クエリで $x \neq y$
- **GetFollowers** のクエリが少なくとも $1$ つ存在する
### 出力
各 **GetFollowers** クエリに対して、答えを一行ずつ出力してください。
"""

N, Q = map(int, input().split())
follower_list = [[] for _ in range(N+1)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        follower_list[query[2]].append(query[1])
    else:
        if len(follower_list[query[1]]) > 0:
            follower_list[query[1]] = list(set(follower_list[query[1]]))
            follower_list[query[1]].sort()
            print(*follower_list[query[1]])
            # follower_list[query[1]] = [str(num) for num in follower_list[query[1]]]
            # print(" ".join(follower_list[query[1]]))
            # follower_list[query[1]] = [int(num) for num in follower_list[query[1]]]
        else:
            print("No")