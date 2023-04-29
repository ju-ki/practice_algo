grid = [list(input()) for _ in range(8)]
row = ["a", "b", "c", "d", "e", "f", "g", "h"]

# reversedを使ったバージョンで試す
for i in range(8):
    for j in range(8):
        if grid[i][j] == "*":
            print(row[j] + str(8 - i))
            break