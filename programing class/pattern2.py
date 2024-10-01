num = int(input("Enter the num: "))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        if i == 1:
            # First row: print numbers 1 to num with space in between
            print(j, end=" ")
        if i > 1 and j == 1:
            # Remaining rows: print the row number first
            print(i, end=" ")
    # Move to the next line after each row
    print()
