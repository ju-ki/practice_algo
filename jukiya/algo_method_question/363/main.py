"""
https://algo-method.com/tasks/363

### 問題文
カメのアルルは今日 $N$ 個の予定が入っています。
$i$ 番目の予定は時刻 $S_i$ に開始し、時刻 $T_i$ に終了します。
それぞれの予定は途中参加や途中退出することができませんが、開始時刻と終了時刻が被る予定には共に参加することができます。
アルルはできるだけ多くの予定に参加したいと考えています。
最大でいくつの予定に参加することができますか。
### 入力
入力は次の形式から与えられます。
```IOExample
$N$
$S_0 T_0$
$S_1 T_1$
$\vdots$
$S_{N-1} T_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $S_i$ は $1$ 以上 $10000$ 以下の整数 $(0 \leq i \leq N-1)$
- $T_i$ は $1$ 以上 $10000$ 以下の整数 $(0 \leq i \leq N-1)$
- $T_i$ は $S_i$ より大きい $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""
N = int(input())
ST = [list(map(int, input().split())) for _ in range(N)]

ST.sort(key=lambda x: (x[1], x[0]))

counter = 0
current_time = 0

#何かが足りない->うまく言葉に表現できないが何か飛ばしている？

# for idx in range(1, len(ST)):
#     for idx2 in range(idx, len(ST)):
#         current_st = ST[idx]
#         next_st = ST[idx2]
#         if current_time <= next_st[0]:
#             counter += 1
#             current_time = current_st[1]
#             break
# print(counter)


#nextとの比較が悪かったぽい
for s, t in ST:
    if current_time <= s:
        current_time = t
        counter += 1
print(counter)