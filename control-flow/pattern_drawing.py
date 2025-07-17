# prompt the user to enter a positive number

pattern_size = (int(input("Enter the size of the pattern: ")))


row_count = 0
# while statement
while row_count < pattern_size:
    # for loop statement
    for col_count in range(pattern_size):
        print("*", end="")
    print("")

    row_count += 1
