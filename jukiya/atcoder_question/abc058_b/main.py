O = list(input())
E = list(input())
NE = len(E)
NO = len(O)
ans = ""

for i in range(NE):
    ans += O[i]
    ans += E[i]

if NO - NE == 1:
    ans += O[-1]
print(ans)
