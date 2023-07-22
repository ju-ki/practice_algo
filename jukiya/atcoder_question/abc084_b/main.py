import re

A, B = map(int, input().split())
S = input()
A = '{' + '{0}'.format(A) + '}'
B = '{' + '{0}'.format(B) + '}'
cond = r"[0-9]{0}-[0-9]{1}".format(A, B)

result = re.match(cond, S)

print('Yes') if result else print('No')