import sys
if len(sys.argv) == 2:
    para1 = sys.argv[1]
    user_input = input("What was the parameter? ")
    if user_input == para1:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")