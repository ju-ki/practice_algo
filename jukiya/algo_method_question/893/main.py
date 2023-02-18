"""
https://algo-method.com/tasks/893

### 問題文
カメのアルルは $N$ 日間ゲームをプレイしました。
$0, 1, \dots, N-1$ 日目のスコアは $A_0, A_1, \dots, A_{N-1}$ でした。
初日は最も調子が悪く、$A_0 = 0$ であったことが保証されます。
各日に対して、「最後にその日よりも調子が悪かった日」からその日までの日数を**スパン**と呼ぶことにします。
各 $i = 1, 2, \dots, N-1$ に対して、$i$ 日目のスパンを求め、一行ずつ出力してください。
より正確には、
- $A_j < A_i$
- $j < i$
をどちらも満たす最大の $j$ を求め、$i - j$ の値を出力してください。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2Fb530eb50-e969-4825-b3ae-08ab37b835dc%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-05-01+0.59.40.png)
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \ldots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $2 \times 10^{5}$ 以下の整数
- $A_0 = 0$ である
- $A_i$ は $1$ 以上 $10^{9}$ 以下の整数 $(1 \leq i \leq N-1)$
### 出力
答えを一行ずつ、$N-1$ 行に出力してください。
"""


# やっていることは理解できたけどまだ少し不安
N = int(input())
A = list(map(int, input().split()))
worse_list = []
worse_list.append([0, 0])

for i in range(1, N):
    a = A[i]

    while a <= worse_list[-1][0]:
        worse_list.pop()
    answer = i - worse_list[-1][1]
    worse_list.append([a, i])
    print(answer)

