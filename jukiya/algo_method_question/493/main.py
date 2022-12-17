"""
https://algo-method.com/tasks/493

### 問題文
アルルの通う学校には $N$ 人の生徒がいます。
それぞれの生徒には $0$ から $N-1$ までの番号が割り振られています。
ある日 $N$ 人が一斉に数学と英語のテストを受けたところ、順位表は次のようになりました。
順位は $2$ 教科の合計点が高い順に並んでおり、合計点が同じ場合はランダムに並んでいます。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2Fda45d72a-e576-4824-b52e-8857c86dbf6a%2F2-7-1.png)
アルルは数学の順位が気になったため、この表を次のように並び替えることにしました。
----
数学の点数が**高い**人が順位表の上に来るように並び替える。
ただし、数学の点数が同じ人同士の場合は合計点の**低い**人が上に来るようにする。
また、数学の点数も合計点も同じ人同士の場合はもとの順序関係を保つようにする。
----
順位表を並び替えた結果を出力してください。
### 入力
入力は次の形式から与えられます。
```IOExample
$N$
$S_0 A_0 B_0$
$S_1 A_1 B_1$
$\vdots$
$S_{N-1} A_{N-1} B_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^5$ 以下の整数
- $S_i$ は英小文字からなる長さ $1$ 以上 $10$ 以下の文字列 $(0 \leq i \leq N-1)$
- $A_i$ は $0$ 以上 $10^5$ 以下の整数 $(0 \leq i \leq N-1)$
- $B_i$ は $0$ 以上 $10^5$ 以下の整数 $(0 \leq i \leq N-1)$
- 与えられたデータは問題文で説明された順序で並んでいる。
### 出力
$N$ 行で答えを出力してください。
ただし、 $i$ 行目には「並び替えた後の順位表における、上から $i$ 番目の人の名前、算数の点数、英語の点数」を空白区切りで出力してください。
"""



N = int(input())
data = [tuple(map(str, input().split())) for _ in range(N)]

# キーを二つ以上設定できる
data.sort(key=lambda x: (-int(x[1]), int(x[1]) + int(x[2])))

# 入れ替えが前後でしか発生していない
# for num_i in range(1, N):
#     top_data = data[num_i-1]
#     current_data = data[num_i]
#     top_sum = int(top_data[1]) + int(top_data[2])
#     current_sum = int(current_data[1]) + int(current_data[2])
#     if int(current_data[1]) > int(top_data[1]):
#         data[num_i], data[num_i-1] = data[num_i-1], data[num_i]
#     elif int(current_data[1]) == int(top_data[1]):
#         if current_sum < top_sum:
#             data[num_i], data[num_i-1] = data[num_i-1], data[num_i]
#     else:
#         continue

for ans_data in data:
    print(*ans_data)