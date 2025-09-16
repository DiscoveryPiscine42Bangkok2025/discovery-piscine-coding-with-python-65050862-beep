first_num = int(input("Enter the first number : \n"))
second_num = int(input("Enter the second number : \n"))
result = first_num*second_num
if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive")
else:
    print("The result is both positive and negative.")