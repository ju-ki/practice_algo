n = int(input())
#最初の文字列を取得syutokusss
s = list(input())

for i in range(n - 1):
    t = list(input())
    new = []
    for elem in t:
        #もし存在するのであればnewに追加、元々の文字列を削除
        if elem in s:
            new.append(elem)
            s.remove(elem)
    #値を更新
    s = new

print(*sorted(s), sep='')
