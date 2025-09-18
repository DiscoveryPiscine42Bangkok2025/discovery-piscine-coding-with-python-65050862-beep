# checkmate.py

# --- ส่วนที่ 1: ฟังก์ชันผู้ช่วย (Helper Functions) ---

def find_positions(board):
    """ฟังก์ชันสำหรับสแกนกระดานเพื่อหาตำแหน่ง King และศัตรูทั้งหมด"""
    king_location = None
    enemy_locations = []
    # วนลูป 2 ชั้นเพื่อเดินดูทุกช่องบนกระดาน
    for row_num, row_str in enumerate(board):
        for col_num, piece in enumerate(row_str):
            if piece == 'K':
                king_location = (row_num, col_num)
            elif piece in "PBRQ":
                enemy_locations.append((row_num, col_num))
    return king_location, enemy_locations

def is_pawn_threatening(pawn_pos, king_pos):
    """ตรวจสอบว่า Pawn โจมตีถึง King หรือไม่ (โจมตีทแยงขึ้น 1 ช่อง)"""
    pawn_row, pawn_col = pawn_pos
    king_row, king_col = king_pos
    
    # Pawn ต้องอยู่แถวล่างกว่า King 1 แถว และอยู่คอลัมน์ซ้ายหรือขวา 1 ช่อง
    if king_row == pawn_row - 1 and abs(king_col - pawn_col) == 1:
        return True
    return False

def is_rook_threatening(rook_pos, king_pos, board):
    """ตรวจสอบว่า Rook โจมตีถึง King หรือไม่ (เช็คสิ่งกีดขวางด้วย)"""
    rook_row, rook_col = rook_pos
    king_row, king_col = king_pos

    # ถ้าไม่ได้อยู่แนวเดียวกัน ก็โจมตีไม่ได้แน่นอน
    if rook_row != king_row and rook_col != king_col:
        return False

    # กรณีอยู่ "แถวเดียวกัน" (แนวนอน)
    if rook_row == king_row:
        start_col = min(rook_col, king_col)
        end_col = max(rook_col, king_col)
        # วนลูปเช็ค "ช่องระหว่างกลาง"
        for c in range(start_col + 1, end_col):
            if board[rook_row][c] in "PBRQK":
                return False # เจอตัวขวาง!

    # กรณีอยู่ "คอลัมน์เดียวกัน" (แนวตั้ง)
    else: # elif rook_col == king_col
        start_row = min(rook_row, king_row)
        end_row = max(rook_row, king_row)
        # วนลูปเช็ค "ช่องระหว่างกลาง"
        for r in range(start_row + 1, end_row):
            if board[r][rook_col] in "PBRQK":
                return False # เจอตัวขวาง!

    return True # ถ้าไม่เจอตัวขวางเลย แสดงว่าโจมตีถึง

def is_bishop_threatening(bishop_pos, king_pos, board):
    """ตรวจสอบว่า Bishop โจมตีถึง King หรือไม่ (เช็คสิ่งกีดขวางด้วย)"""
    bishop_row, bishop_col = bishop_pos
    king_row, king_col = king_pos

    # ถ้าไม่ได้อยู่แนวทแยงเดียวกัน ก็โจมตีไม่ได้แน่นอน
    # ผลต่างของแถว กับ ผลต่างของคอลัมน์ ต้องเท่ากัน
    if abs(bishop_row - king_row) != abs(bishop_col - king_col):
        return False

    # หา "ทิศทาง" ที่จะเดินตรวจสอบ (ทีละ 1 ช่อง)
    # step_row จะเป็น 1 (ลง) หรือ -1 (ขึ้น)
    step_row = 1 if king_row > bishop_row else -1
    # step_col จะเป็น 1 (ขวา) หรือ -1 (ซ้าย)
    step_col = 1 if king_col > bishop_col else -1
    
    # เริ่มเดินจากช่องถัดจาก Bishop ไปในทิศทางของ King
    check_row = bishop_row + step_row
    check_col = bishop_col + step_col

    # เดินไปเรื่อยๆ จนกว่าจะถึงตำแหน่งของ King
    while (check_row, check_col) != (king_row, king_col):
        if board[check_row][check_col] in "PBRQK":
            return False # เจอตัวขวาง!
        check_row += step_row
        check_col += step_col

    return True # ถ้าไม่เจอตัวขวางเลย แสดงว่าโจมตีถึง

# --- ส่วนที่ 2: ฟังก์ชันหลัก (ผู้จัดการ) ---

def checkmate(board):
    """
    ฟังก์ชันหลักที่จะควบคุมการทำงานทั้งหมด
    1. ค้นหาตำแหน่ง
    2. วนลูปเช็คศัตรูทุกตัว
    3. ตัดสินผลลัพธ์
    """
    king_pos, enemy_list = find_positions(board)

    # Error Handling: ถ้าไม่เจอ King บนกระดาน
    if king_pos is None:
        print("Fail")
        return

    # วนลูปเช็คศัตรูทุกตัวที่หาเจอ
    for enemy_pos in enemy_list:
        enemy_row, enemy_col = enemy_pos
        enemy_piece = board[enemy_row][enemy_col]
        
        is_king_in_danger = False

        # --- แยกประเภทการโจมตีตามชนิดของหมาก ---
        if enemy_piece == 'P':
            if is_pawn_threatening(enemy_pos, king_pos):
                is_king_in_danger = True
        
        elif enemy_piece == 'R':
            if is_rook_threatening(enemy_pos, king_pos, board):
                is_king_in_danger = True

        elif enemy_piece == 'B':
            if is_bishop_threatening(enemy_pos, king_pos, board):
                is_king_in_danger = True

        elif enemy_piece == 'Q':
            # Queen คือการรวมความสามารถของ Rook และ Bishop
            # ถ้าโจมตีแบบ Rook ได้ "หรือ" โจมตีแบบ Bishop ได้ ก็ถือว่ารุก
            if is_rook_threatening(enemy_pos, king_pos, board) or \
               is_bishop_threatening(enemy_pos, king_pos, board):
                is_king_in_danger = True

        # ถ้าเจอตัวที่รุกได้แม้แต่ตัวเดียว
        if is_king_in_danger:
            print("Success")
            return # จบการทำงานทันที ไม่ต้องเช็คตัวอื่นต่อ

    # ถ้าวนเช็คครบทุกตัวแล้วไม่เจอตัวที่รุกได้เลย
    print("Fail")