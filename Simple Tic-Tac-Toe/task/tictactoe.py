def print_board():
    print("-" * 8)
    for i in range(3):
        print("| {0} {1} {2} |".format(in_string[i * 3], in_string[i * 3 + 1], in_string[i * 3 + 2]))
    print("-" * 8)
    return

in_string = input("Enter cells:")
pieces = [0, 0, 0]
result_string = ["Draw", "X wins", "O wins", "Impossible", "Game not finished"]
x = 0
y = 0
print_board()

winner = 0
if in_string[2] + in_string[4] + in_string[6] == "XXX" or in_string[0] + in_string[4] + in_string[8] == "XXX" or in_string[0:3] == "XXX" or in_string[3:6] == "XXX" or in_string[6:9] == "XXX" or in_string[0] + in_string[3] + in_string[6] == "XXX" or in_string[1] + in_string[4] + in_string[7] == "XXX"  or in_string[2] + in_string[5] + in_string[8] == "XXX":
    winner += 1
if in_string[2] + in_string[4] + in_string[6] == "OOO" or in_string[0] + in_string[4] + in_string[8] == "OOO" or in_string[0:3] == "OOO" or in_string[3:6] == "OOO" or in_string[6:9] == "OOO" or in_string[0] + in_string[3] + in_string[6] == "OOO" or in_string[1] + in_string[4] + in_string[7] == "OOO"  or in_string[2] + in_string[5] + in_string[8] == "OOO":
    winner += 2
for piece in in_string:
    if piece == "X":
        pieces[0] += 1
    elif piece == "O":
        pieces[1] += 1
    else:
        pieces[2] += 1

if pieces[0] > pieces[1] +1 or pieces[1] > pieces[0] + 1:
    winner = 3
if winner == 0 and pieces[2] > 0:
    winner = 4

if winner < 4:
    print(result_string[winner])
else:
    while True:
        x, y = input("Enter the coordinates:").split()
        x = int(x)
        y = int(y)
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
        elif in_string[(x - 1) * 3 + y - 1] != "_":
            print("This cell is occupied! Choose another one!")
        else:
            break

in_string = in_string[:(x - 1) * 3 + y - 1] + "X" + in_string[(x - 1) * 3 + y:]

print_board()



