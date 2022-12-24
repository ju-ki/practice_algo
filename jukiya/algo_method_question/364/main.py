"""
https://algo-method.com/tasks/364

### 問題文
アルルはちょうど $N$ 個のお菓子を作ろうとしています。
アルルは毎日どちらかのプランでお菓子を作ることができます。
- プラン $1$：お菓子を $1$ つ作る。
- プラン $2$：全てのお菓子を分割して、個数を $3$ 倍にする。
ちょうど $N$ 個のお菓子を作るまで最短で何日かかるか答えてください。
### 入力
入力は次の形式から与えられます。
```IOExample
$N$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
### 出力
答えを出力してください。
"""

N = int(input())

#足していく場合だと最適解がとれない説
# counter = 0
# date_counter = 0

# while counter < N:
#     print(counter)
#     date_counter += 1
#     if counter * 3 < N and counter != 0:
#         counter *= 3
#     else:
#         counter += 1

# print(date_counter)


N = int(input())
counter = N
date_counter = 0

while counter > 0:
    date_counter += 1
    if counter % 3 == 0:
        counter /= 3
    else:
        counter -= 1
print(date_counter)