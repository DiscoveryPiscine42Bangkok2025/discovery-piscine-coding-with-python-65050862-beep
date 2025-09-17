age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
i = 0
y = 0
for i in range(3):
    y += 10
    print(f"In {y} years, you'll be {age+y} years old.")