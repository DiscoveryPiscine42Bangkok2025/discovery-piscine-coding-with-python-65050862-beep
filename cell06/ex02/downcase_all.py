import sys
def downcase_it(text):
    return text.lower()
if len(sys.argv)>1:
    for i in sys.argv[1:]:
        lowercase_text = downcase_it(i)
        print(lowercase_text)
else:
    print("none")