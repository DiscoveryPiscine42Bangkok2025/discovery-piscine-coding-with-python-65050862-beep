def greetings(name):
    if not name:
        name = "noble stranger"
    if name.isnumeric():
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

def main():
    name = str(input())
    greetings(name)
main()