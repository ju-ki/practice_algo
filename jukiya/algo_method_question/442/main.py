"""
https://algo-method.com/tasks/442

### 問題文
クイックソートは、与えられたいくつかの要素を、
所定の順序にしたがって並び替えるソートアルゴリズムです。
クイックソートには次の特徴があります (要素の個数を $N$ とします)。
- 部分問題を再帰的に解くアルゴリズムである (分割統治法)
- 最悪時の計算量は $O(N^2)$
- 最良時と平均時の計算量は $O(N \log N)$
以下に示すアルゴリズムは、
サイズ $N$ の配列 $A$ を昇順に並び替えるクイックソートの動作を表したものです。
----
$A[X] (X = \lfloor \frac{N}{2} \rfloor)$ を軸としてソートを行う。
1. 空の配列 $L, R$ を用意し、次の操作を $i=0, 1, \cdots, N-1$ について行う。
   1. $i = X$ ならば何も行わない。
   2. $i \neq X$ かつ $A[i] \lt A[X]$ ならば $A[i]$ を $L$ の末尾に追加する。
   3. $i \neq X$ かつ $A[i] \geq A[X]$ ならば $A[i]$ を $R$ の末尾に追加する。
3. $L, R$ をクイックソートを用いて再帰的にソートする。空配列の場合は何も行わない。
4. $L$ の要素, $A[X]$, $R$ の要素をこの順につなげてできる配列を出力する。
---
このアルゴリズムを実装し、配列 $A$ をソートした結果を出力してください。
ただし、 $\lfloor X \rfloor$ は 「$X$ を超えない最大の整数」を示します。
例えば、$\lfloor 3.14 \rfloor = 3, \lfloor 10 \rfloor = 10$ です。
### 入力
入力は次の形式から与えられます。
```IOExample
$N$
$A_0 A_1 \cdots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $A_i$ は $1$ 以上 $N$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを $1$ 行で出力してください。
"""

N = int(input())
A = list(map(int, input().split()))


def quick_sort(X):
    if len(X) == 0:
        return []
    medium = len(X) // 2
    L, R = [], []
    for num_i in range(len(X)):
        if num_i == medium:
            continue
        if X[num_i] < X[medium]:
            L.append(X[num_i])
        elif X[num_i] > X[medium]:
            R.append(X[num_i])
    L = quick_sort(L)
    R = quick_sort(R)
    L.append(X[medium])
    L.extend(R)
    return L


ans = quick_sort(A)
print(*ans)

# ans_list = []
# L_list = []
# R_list = []
# for num_i in range(len(A) - 1):
#     medium = N // 2
#     if A[num_i] < A[medium] and num_i != medium:
#         L_list.append(A[num_i])
#     elif A[num_i] > A[medium] and num_i != medium:
#         R_list.append(A[num_i])
# ans_list += L_list
# ans_list += A[medium]
# ans_list += R_list
# print(*ans_list)
