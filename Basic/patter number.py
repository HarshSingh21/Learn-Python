print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print(" ")
