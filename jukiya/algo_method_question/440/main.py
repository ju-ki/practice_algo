"""
https://algo-method.com/tasks/440

### 問題文
選択ソートは、与えられたいくつかの要素を、
所定の順序にしたがって並び替えるソートアルゴリズムです。
選択ソートには次の特徴があります (要素の個数を $N$ とします)。
- 与えられた配列以外の記憶領域が不要 (in-place であるといいます)
- 計算量は $O(N^2)$ (最悪時、平均時、最良時すべてについて)
以下に示すアルゴリズムは、
サイズ $N$ の配列 $A$ を昇順に並び替える選択ソートの動作を表したものです。
----
$k=0, 1, \cdots, N-2$ について次の処理を行う。
1. $A[k], A[k+1], \cdots, A[N-1]$ のうち値が最も小さい要素を $1$ つを選択する。
   ただし、該当する要素が複数ある場合はそのうち最も前にある要素を選択する。
2. $A[k]$ と選んだ要素を交換する。
3. $A$ の各要素を空白区切りで出力する。
---
このアルゴリズムを実装し、配列 $A$ がソートされる過程を出力してください。
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
配列 $A$ がソートされる過程を $N-1$ 行で出力してください。
ただし、上述のアルゴリズムのステップ $3$ で配列 $A$ を出力するたびに、改行を入れてください。
"""

N = int(input())
A = list(map(int, input().split()))

for num_i in range(len(A) - 1):
    min_value = A[num_i]
    swapped_flag = False
    for num_j in range(num_i+1, len(A)):
        if min_value > A[num_j]:
            min_value = A[num_j]
            swap_id = num_j
            swapped_flag = True
    if swapped_flag:
        A[num_i], A[swap_id] = min_value, A[num_i]
    print(*A)