S = "dreameraser"
# maerdesare

divide_list = ["dream", "dreamer", "erase", "eraser"]
reversed_S = "".join(list(reversed(S)))

can_divide = True
counter = 0
for i in range(len(reversed_S)):
    can_divide2 = False
    for j in range(4):
        divide = divide_list[j]
        reversed_divide = "".join(list(reversed(divide)))
        if reversed_S[counter:len(divide) + counter] == reversed_divide:
            can_divide2 = True
            counter += len(divide)
    if counter >= len(S):
        break
    if not can_divide2:
        can_divide = False
        break

print('YES') if can_divide else print('NO')
