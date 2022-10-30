"""
https://algo-method.com/tasks/1024

### 問題文
正の整数 $N, M$ が与えられます。
$3$ つの正の整数の組 $x, y, z$ であって、
- $x, y, z$ はそれぞれ $1$ 以上 $N$ 以下の整数である
- $x, y, z$ の総和は $M$ 以下である
という条件をともに満たすものが何個あるかを求めてください。
#### ヒント
<details><summary>z のループは不要</summary><div>
比較的すぐに思いつく解法は、$x, y, z$ をすべて調べる方法かもしれません。
しかしその方法では $O(N^{3})$ の計算量となります (考えてみてください)。
$O(N^{3})$ の解法では「時間切れ」となりますので、工夫が必要です。
実は、$x, y$ をすべて調べるだけでこの問題は解けます。
$x, y$ の値を決めると、$z$ のとりうる値の範囲は自動的に決まります。
これによって、$O(N^{2})$ の解法にすることができます。
</div></details>
### 入力
入力は次の形式で与えられます。
```IOExample
$N M$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $2000$ 以下の整数
- $M$ は $1$ 以上 $3N$ 以下の整数
### 出力
答えを出力してください。
"""

N, M = map(int, input().split())
counter = 0

for num_x in range(1, N+1):
    for num_y in range(1, N+1):
        max_z = min(N, M-num_x-num_y)
        if max_z <= 0:
            continue
        counter += max_z

print(counter)