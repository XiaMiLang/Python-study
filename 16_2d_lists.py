number_grid =[[1, 2, 3],[4, 5, 6],[7, 8, 9],[0],]
print(number_grid[1][2])        # 6
# nested for loop
for row in number_grid:
    print(row)

for x in number_grid:
    for y in x:
        print(y)

