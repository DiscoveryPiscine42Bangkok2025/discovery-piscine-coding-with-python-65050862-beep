import sys
if len(sys.argv) != 3:
    print('none')
    sys.exit()
try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
except ValueError:
    print('none')
    sys.exit()
number_range = list(range(start, end + 1))
print(number_range)