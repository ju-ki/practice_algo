"""
https://algo-method.com/tasks/491

### 問題文
カメのアルルはごはんを買いにお店にきました。
お店には $0$ から $N-1$ までの番号が振られた $N$ 種類のごはんが売られています。
ごはん $i$ の価格は $A_i$ 円で、在庫が $B_i$ 個あります。
アルルが合計で $K$ 個のごはんを買うには最低何円払う必要がありますか。
### 入力
入力は次の形式で与えられます。
```IOExample
$N K$
$A_0 B_0$
$A_1 B_1$
$\vdots$
$A_{N-1} B_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $2$ 以上 $10^5$ 以下の整数
- $K$ は $1$ 以上 ($B$ の総和) 以下の整数
- $A_i$ は $1$ 以上 $10^5$ 以下の整数 $(0 \leq i \leq N-1)$
- $B_i$ は $1$ 以上 $10^5$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N, K = map(int, input().split())
pair = [tuple(map(int, input().split())) for _ in range(N)]

pair.sort()


ans = 0

for (a, b) in pair:
    num = min(K, b)
    K -= num
    ans += a * num
print(ans)