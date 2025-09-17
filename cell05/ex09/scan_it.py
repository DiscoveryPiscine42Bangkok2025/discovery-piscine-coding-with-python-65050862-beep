import sys
import re
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    search = sys.argv[2]
    matches = re.findall(keyword, search)
    match_count = len(matches)
    if match_count > 0:
        print(match_count)
    else:
        print("none")
else:
    print("none")