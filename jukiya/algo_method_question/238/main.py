"""
https://algo-method.com/tasks/238

### 問題
整数 $X$ を文字列としてみると回文になっているとき、「$X$ は回文数である」と呼ぶことにします。
整数 $L$, $R$ が与えられるので、$L$ 以上 $R$ 以下の整数の中に回文数がいくつあるか数えるプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$L$ $R$
```
また、入力される値は次の制約を満たします。
- $L$ は $1$ 以上 $1000$ 以下の整数
- $R$ は $L$ 以上 $1000$ 以下の整数
### 出力
答えを出力してください。
"""

L, R = map(int, input().split())
counter = 0

# if L == R:
#     print(counter)
# else:
#     for num_i in range(L, R+1):
#         if len(str(num_i)) == 1:
#             counter += 1
#         else:
#             same_flag = True
#             li_str_i = list(str(num_i))
#             for str_j, rev_str_j in zip(li_str_i, reversed(li_str_i)):
#                 if str_j != rev_str_j:
#                     same_flag = False
#                     break
#             if same_flag:
#                 counter += 1
#     print(counter)


def get_palindrome_flag(N: int) -> bool:
    same_flag = True
    li_str_i = list(str(N))
    for str_j, rev_str_j in zip(li_str_i, reversed(li_str_i)):
        if str_j != rev_str_j:
            same_flag = False
            break
    return same_flag


for num_i in range(L, R+1):
    if get_palindrome_flag(num_i):
        counter += 1
print(counter)
