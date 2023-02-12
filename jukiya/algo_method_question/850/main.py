"""
https://algo-method.com/tasks/850

### 問題文
$1$ から $N$ までの整数を右回りに円状に並べて、
$1$ から始めて右回りに、$1$ つおきに取り除いていきます (図は $N = 12$ の場合)。
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F9f45ddb3-8f4c-462a-b795-81c88b21d839%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-03-16+15.56.16.png)
最後に残る整数を答えてください。
たとえば $N = 12$ の場合、取り除かれるカードは
$1, 3, 5, 7, 9, 11, 2, 6, 10, 4, 12$
となって、最後に $8$ が残ります。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $10^6$ 以下の整数
### 出力
答えを出力してください。
"""
# 理解はしたと思うけどコードに落とすことが少し引っかかる
# N = int(input())
N = 1

nex, prev = [0 for _ in range(N+1)], [0 for _ in range(N+1)]

for i in range(1, N+1, 1):
    nex[i] = i + 1
    if i == N:
        nex[i] = 1
    prev[i] = i - 1
    if i == 1:
        prev[i] = N


num = 1
print(nex)
print(prev)

for i in range(N):
    prev[nex[num]] = prev[num]
    nex[prev[num]] = nex[num]
    num = nex[nex[num]]
    print(num)
    print(nex)
    print(prev)
print(num)
