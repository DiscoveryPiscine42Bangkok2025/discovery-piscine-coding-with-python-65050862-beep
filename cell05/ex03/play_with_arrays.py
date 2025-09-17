num = [2,8,9,48,8,22,-12,2]
new_num =[]
for i in num:
    if i >5:
        j = i+2
        if j not in new_num:
            new_num.append(j)
print(f"Original: {num}")
print(f"New number: {new_num}")