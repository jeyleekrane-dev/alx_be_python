pattern_size = input("Enter the size of the pattern: ")
pattern_size = int(pattern_size)

row_count = 0
# while statement
while row_count < pattern_size:
    # for loop statement
    for col_count in range(pattern_size):
        print("*", end="")
    print("")
    row_count += 1
