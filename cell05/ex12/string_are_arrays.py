import sys
if len(sys.argv) == 2:
    input = sys.argv[1]
    z_count = input.count('z')
    if z_count > 0:
        print("z"*z_count)
    else:
        print("none")
else:
    print("none")