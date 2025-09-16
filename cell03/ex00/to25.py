num = int(input("Enter a number less than 25\n"))
if num > 25:
        print("Error")
else:
    number_list = []
    num1 = num
    while num1 <= 25:
        number_list.append(num1)
        num1 += 1
    for num in number_list :
        print(f"Inside the loop, my variable is {num}")