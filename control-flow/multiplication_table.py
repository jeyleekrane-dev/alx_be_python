number = input("Enter a number to see its multiplication table: ")
number = int(number)

# for loop
for range in range(1, 11):
    print(f"{number} * {range} = {number*range}")
