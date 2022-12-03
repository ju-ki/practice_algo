"""
https://algo-method.com/tasks/518

### 問題文
次のような頂点数 $N$ の二分木があります。
木の根は頂点 $0$ で、 $0 \leq i \leq \lfloor\frac{N}{2}\rfloor-1$ について頂点 $i$ の左側の子は頂点 $2i+1$、 (存在するならば)右側の子は頂点 $2i+2$ です。
頂点の値は長さ $N$ の配列 $A = [A_0, A_1, \cdots, A_{N-1}]$ によって表され、頂点 $i$ の値は前から $i$ 番目の要素が管理しています。(図は $N=6$ の例です。)
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F591c7bb2-4870-412d-9f22-439a56e8f50c%2F5-7-1.png)
この木の頂点を次の条件を満たすように並び替えることを考えます。
(条件をみたす構造のことを**ヒープ木**といいます。)
```Statement
すべての頂点 $i (0 \leq i \leq N-1)$ について、頂点 $i$ の値は頂点 $i$ のすべての子ノードの値以上である。
```
次の手順をなぞって、頂点を条件を満たすように並び替えてください。
----
1. 変数 $x$ に $\lfloor\frac{N}{2}\rfloor-1$ を代入する。
2. $x \geq 0$ を満たす間次の処理を繰り返し行う。
   1. $k = x$ とおき、次の処理を繰り返し行う。
      1. 頂点 $k$ が子ノードを持たなければ処理を終了する。
      2. $A[k]$, $A[2k+1]$ (頂点 $k$ の左側の子ノード), (もし存在すれば) $A[2k+2]$ (頂点 $k$ の右側の子ノード) の値を比較し最大値を持つノードを選択する。
         ただし、最大値を持つノードが複数ある場合は頂点 $k$, 頂点 $2k+1$, 頂点 $2k+2$ の順に選択する。
         1. 頂点 $k$ を選択した場合
            処理を終了する。
         2. 頂点 $2k+1$ を選択した場合
            $A[k]$ と $A[2k+1]$ を入れ替え $k$ の値を $2k+1$ に更新する。
         3. 頂点 $2k+2$ を選択した場合
            $A[k]$ と $A[2k+2]$ を入れ替え $k$ の値を $2k+2$ に更新する。
   2. $x$ の値を $1$ だけ減らす。
----
### 入力
入力は次の形式から与えられます。
```IOExample
$N$
$A_0 A_1 \cdots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^5$ 以下の整数
- $A_i$ は $1$ 以上 $10^9$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
ソート後の $A$ について、すべての要素を前から順に空白区切りで出力してください。
"""
debug = True

if debug:
    N = 6
    A = [3, 1, 4, 1, 5, 9]
else:
    N = int(input())
    A = list(map(int, input().split()))


if debug:
    for x in range(len(A) // 2 - 1, -1, -1):
        print(x)
        k = x
        while True:
            left = A[2*k+1] if 2*k+1 < len(A) else 0
            right = A[2*k+2] if 2*k+2 < len(A) else 0
            print(left, right)
            if left == 0 and right == 0:
                break
            elif A[k] >= left and A[k] >= right:
                break
            elif left >= right:
                A[k], A[2*k+1] = A[2*k+1], A[k]
                k = 2*k+1
            else:
                A[k], A[2*k+2] = A[2*k+2], A[k]
                k = 2*k+2
        print(*A)
else:
    def build_heap(v):
        for x in range(len(v)//2-1, -1, -1):
            k = x
            while True:
                left = v[2*k+1] if 2*k+1<len(v) else 0
                right = v[2*k+2] if 2*k+2<len(v) else 0
                if left == 0 and right == 0:
                    break
                elif v[k]>=left and v[k]>=right:
                    break
                elif left >= right:
                    v[k], v[2*k+1] = v[2*k+1], v[k]
                    k = 2*k+1
                else:
                    v[k], v[2*k+2] = v[2*k+2], v[k]
                    k = 2*k+2
    build_heap(A)
    print(*A)