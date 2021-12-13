board = [
    [" ", "0", "1","2"],
    ["0", "-", "-","-"],
    ["1", "-", "-","-"],
    ["2", "-", "-","-"]
]
def draw_board():
    for i in board:
        print(*i)

def check_win():
    if board[1][1]=="X" and board[1][2]=="X" and board[1][3]=="X":
        print("\033[1;31m Победил крестик \033[0;0m")
        return False
    elif board[2][1]=="X" and board[2][2]=="X" and board[2][3]=="X":
        print("\033[1;31m Победил крестик \033[0;0m")
        return False
    elif board[3][1] == "X" and board[3][2] == "X" and board[3][3] == "X":
        print("\033[1;31m Победил крестик \033[0;0m")
        return False
    elif board[1][1] == "X" and board[2][1] == "X" and board[3][1] == "X":
        print("\033[1;31m Победил крестик \033[0;0m")
        return False
    elif board[1][2] == "X" and myList[2][2] == "X" and board[3][2] == "X":
        print("\033[1;31m Победил крестик \033[0;0m")
        return False
    elif board[1][3] == "X" and board[2][3] == "X" and board[3][3] == "X":
        print("\033[1;31m Победил крестик \033[0;0m")
        return False
    elif board[1][1] == "X" and board[2][2] == "X" and board[3][3] == "X":
        print("\033[1;31m Победил крестик \033[0;0m")
        return False
    elif board[1][3] == "X" and board[2][2] == "X" and board[3][1] == "X":
        print("\033[1;31m Победил крестик \033[0;0m")
        return False
    elif board[1][1]=="0" and board[1][2]=="0" and board[1][3]=="0":
        print("\033[1;33m Победил нолик \033[0;0m")
        return False
    elif board[2][1]=="0" and board[2][2]=="0" and board[2][3]=="0":
        print("\033[1;33m Победил нолик \033[0;0m")
        return False
    elif board[3][1] == "0" and board[3][2] == "0" and board[3][3] == "0":
        print("\033[1;33m Победил нолик \033[0;0m")
        return False
    elif board[1][1] == "0" and board[2][1] == "0" and board[3][1] == "0":
        print("\033[1;33m Победил нолик \033[0;0m")
        return False
    elif board[1][2] == "0" and board[2][2] == "0" and board[3][2] == "0":
        print("\033[1;33m Победил нолик \033[0;0m")
        return False
    elif board[1][3] == "0" and board[2][3] == "0" and board[3][3] == "0":
        print("\033[1;33m Победил нолик \033[0;0m")
        return False
    elif board[1][1] == "0" and board[2][2] == "0" and board[3][3] == "0":
        print("\033[1;33m Победил нолик \033[0;0m")
        return False
    elif board[1][3] == "0" and board[2][2] == "0" and board[3][1] == "0":
        print("\033[1;33m Победил нолик \033[0;0m")
        return False
    else:
        return True

draw_board()

for j in range(1,5):
    a, b = map(int, input("Введи номер строки и столбца через пробел для Х ").split())
    a += 1
    b += 1
    board[a][b]="X"
    draw_board()
    if check_win() is False:
        break
    c, d = map(int, input("Введи номер строки и столбца через пробел для 0 ").split())
    c += 1
    d += 1
    board[c][d] = "0"
    draw_board()
    if check_win() is False:
        break
if check_win():
    print("\033[2;33m ****НИЧЬЯ**** \033[0;0m")