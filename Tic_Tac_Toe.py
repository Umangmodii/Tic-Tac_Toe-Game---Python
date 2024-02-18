# Tic Tac Toe Using Python
# By Umang Modi

def sum(a, b, c):
    return a + b + c

def Boards(xstate, ystate):
    zero = xstate[0] if xstate[0] else (ystate[0] if ystate[0] else "0")
    one = xstate[1] if xstate[1] else (ystate[1] if ystate[1] else "1")
    two = xstate[2] if xstate[2] else (ystate[2] if ystate[2] else "2")
    three = xstate[3] if xstate[3] else (ystate[3] if ystate[3] else "3")
    four = xstate[4] if xstate[4] else (ystate[4] if ystate[4] else "4")
    five = xstate[5] if xstate[5] else (ystate[5] if ystate[5] else "5")
    six = xstate[6] if xstate[6] else (ystate[6] if ystate[6] else "6")
    seven = xstate[7] if xstate[7] else (ystate[7] if ystate[7] else "7")
    eight = xstate[8] if xstate[8] else (ystate[8] if ystate[8] else "8")

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")

def checkwin(xstate, ystate):
    wins = (
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    )

    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("X Won the Match!")
            return 1
        if sum(ystate[win[0]], ystate[win[1]], ystate[win[2]]) == 3:
            print("O Won the Match!")
            return 0

    return -1

if __name__ == "__main__":
    xstate = ["", "", "", "", "", "", "", "", ""]
    ystate = ["", "", "", "", "", "", "", "", ""]
    turn = 1

    print("Welcome to Tic Tac Toe Game\n")

    while True:
        Boards(xstate, ystate)

        if turn == 1:
            print("X's Chance")
            value = int(input("Enter a value : "))
            if xstate[value] == "":
                xstate[value] = "X"
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("O's Chance")
            value = int(input("Enter a value : "))
            if ystate[value] == "":
                ystate[value] = "O"
            else:
                print("Invalid move. Try again.")
                continue

        cwin = checkwin(xstate, ystate)
        if cwin != -1:
            print("Match Over")
            break
        turn = 1 - turn
