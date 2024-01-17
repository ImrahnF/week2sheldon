# 1. input two numbers and check if first number is a multiple of 2nd number
# 2. write an if statement that assigns 1 to x if y is greater than 0
# 3. write an if statement that increases pay by 3% if score is greater than 90
# 4. input a number and check if it is even or odd

# [from the above, one of these will be on Quiz 1]

# 1. // input two numbers and check if first number is a multiple of 2nd number \\
inp1 = input("Enter the first number: ")
inp2 = input("Enter the sedond number: ")

x = int(inp2)%int(inp1)

if x == 0:
    print(inp1, "is a multiple of", inp2)
else:
    print("This is not a multiple")
