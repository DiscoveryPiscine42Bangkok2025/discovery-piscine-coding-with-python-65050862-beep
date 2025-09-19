from checkmate import checkmate

def main():
    board_text = """
R...
.K..
./B.
.*..
"""
    cleaned_text = board_text.strip()
    board_list = cleaned_text.split('\n')
    checkmate(board_list)

if __name__ == "__main__":
    main()