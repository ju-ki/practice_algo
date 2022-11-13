"""
https://algo-method.com/tasks/646

### 問題文
亀のアルルは確定申告に備えて、すべての領収書を次のようなタイトルで保存しています。
```IOExample
整理番号_領収書名_YYYYMMDD.pdf
```
アルルに代わって、大量の領収書の中からある年ある月のレシートの領収署名を抽出してください。
※ ここで、「YYYYMMDD」は西暦 4 桁の年・2 桁の月・2 桁の日の合計 8 桁からなる、ある特定の日付を表す数字列のことです。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $Y$ $M$
$S_0$
$S_1$
$\vdots$
$S_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $Y$ は $1900$ 以上 $2021$ 以下の整数
- $M$ は $1$ 以上 $12$ 以下の整数
- $S_i$ は問題文中のような $1000$ 文字以下の文字列であり、以下の条件を満たす。
  - 任意文字数の数字があり、次に `_` が現れる。
  - この間の文字列が出力すべき「領収書名」である。
  - その後に `_` が現れ、日付を表す 8 桁の数字列、`.pdf` の順に現れる。
    - 「領収書名」に `_` は含まれない。つまり、 $S_i$ の中には `_` がちょうど 2 回だけ含まれる。
### 出力
Y 年 M 月の領収書の領収書名を、領収書ごとに改行区切りで出力して下さい。
"""
# import re

# N, Y, M = map(int, input().split())

# for _ in range(N):
#   S = input()
#   pattern = r'[^_]+(?!=_' + str(Y).zfill(4) + str(N).zfill(2) + '\d{2}\.pdf)'
#   ans = re.search(pattern, S)
#   if ans:
#     print(ans.group(0))
    
    
import re

N, Y, M = map(int, input().split())

for _ in range(N):
  S = input()
  # r'[^_]+(?!=_' + str(Y).zfill(4) + str(N).zfill(2) + '\d{2}\.pdf)'
  # r'[^_]+(?=_' + str(Y).zfill(4) + str(M).zfill(2) + '\d{2}\.pdf)'
  pattern = r'[^_]+(?=_' + str(Y).zfill(4) + str(M).zfill(2) + '\d{2}\.pdf)'
  ans = re.search(pattern, S)
  if ans:
    print(ans.group(0))