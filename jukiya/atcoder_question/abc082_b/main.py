s = list(input())
t = list(input())

s.sort()
t.sort()
t.reverse()

print('Yes' if s < t else 'No')
