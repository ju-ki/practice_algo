"""
https://algo-method.com/tasks/361

### 問題文
カメのアルルは、 $N$ 個の荷物と $M$ 個の箱を持っています。
$1$ つの箱には $1$ つの荷物を詰めることができます。
荷物には $0$ から $N-1$ までの番号が振られており、荷物 $i$ の重さは $A_i$ です。
また、箱には $0$ から $M-1$ までの番号が振られており、箱 $i$ の制限容量は $B_i$ です。
箱 $i$ には重さが $B_i$ 以下の荷物を $1$ つ詰めることができます。
なお、箱の番号が大きくなるほど、箱の容量は増加していくものとします。
つまり $B_0 \le B_1 \le \dots \le B_{M-1}$ となっています。
アルルはできるだけ多くの荷物を箱に詰めようと考えています。
最大でいくつの荷物を箱に詰めることができるか答えてください。
### 入力
入力は以下の形式から与えられます。
```IOExample
$N$ $M$
$A_0 A_1 \cdots A_{N-1}$
$B_0 B_1 \cdots B_{M-1}$
```
また、入力される値は以下の制約を満たします。
- $N, M$ は $1$ 以上 $1000$ 以下の整数
- $A_i$ は $1$ 以上 $10^9$ 以下の整数 $(1 \leq i \leq N)$
- $B_i$ は $1$ 以上 $10^9$ 以下の整数 $(1 \leq i \leq M)$
- $B_0 \leq B_1 \leq \cdots \leq B_{M-1}$
### 出力
答えを出力してください。
"""


# 普通に間違っている
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# box_list = [False] * M

# A.sort(reverse=True)

# for idx_a, num_a in enumerate(A):
#     for idx_b, num_b in enumerate(B):
#         if num_a <= num_b and not box_list[idx_b]:
#             box_list[idx_b] = True

# counter = 0

# for box in box_list:
#     if box:
#         counter += 1
# print(counter)

#Bもソートしないと最適にならないのでは?+ box_listの数+1する必要性
# breakしていなかった


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

box_list = [False] * (M+1)

A.sort(reverse=True)
B.sort(reverse=True)

for idx_a, num_a in enumerate(A):
    for idx_b, num_b in enumerate(B):
        if num_a <= num_b and not box_list[idx_b]:
            box_list[idx_b] = True
            break

counter = 0

for box in box_list:
    if box:
        counter += 1
print(counter)