"""
https://algo-method.com/tasks/824

### 問題文
$10$ 個の整数 $3, 1, 4, 1, 5, 9, 2, 6, 5, 3$ が一列に与えられます。
左から $k$ 番目の整数の値を答えてください。
ただし、**最も左の数字は左から $0$ 番目**と数えることにします。
### 入力
入力は次の形式で与えられます。
```IOExample
$k$
```
また、入力される値は次の制約を満たします。
- $k$ は $0$ 以上 $9$ 以下の整数
### 出力
答えを出力してください。
"""

num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
k = int(input())
print(num_list[k])