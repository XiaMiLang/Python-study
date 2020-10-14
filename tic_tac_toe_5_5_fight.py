Go = True
m = [" "] * 9

moves = 0

def print_map():
    print("---------")
    print("| {} {} {} |".format(m[0], m[1], m[2]))
    print("| {} {} {} |".format(m[3], m[4], m[5]))
    print("| {} {} {} |".format(m[6], m[7], m[8]))
    print("---------")

def check_X_or_O(location):
    global moves
    if moves % 2 == 0:
        m[location] = "X"
        moves += 1
    else:
        m[location] = "O"
        moves += 1

def enter_the():
    global m
    ins_coordinates = input("Enter the coordinates: ")
    x, y = (ins_coordinates.split() +[None])[:2]
    # global moves
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if x == 1 and y == 1:
            if m[6] == "X" or m[6] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                check_X_or_O(6)

        if x == 2 and y == 1:
            if m[7] == "X" or m[7] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                check_X_or_O(7)

        if x == 3 and y == 1:
            if m[8] == "X" or m[8] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                check_X_or_O(8)
                # m[8] = "X"

        if x == 1 and y == 2:
            if m[3] == "X" or m[3] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                check_X_or_O(3)
                # m[3] = "X"

        if x == 2 and y == 2:
            if m[4] == "X" or m[4] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()         
            else:
                check_X_or_O(4)
                # m[4] = "X"

        if x == 3 and y == 2:
            if m[5] == "X" or m[5] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                check_X_or_O(5)
                # m[5] = "X"
                
        if x == 1 and y == 3:
            if m[0] == "X" or m[0] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                check_X_or_O(0)
                # m[0] = "X"
                
        if x == 2 and y == 3:
            if m[1] == "X" or m[1] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                check_X_or_O(1)
                # m[1] = "X"   
        
        if x == 3 and y == 3:
            if m[2] == "X" or m[2] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                check_X_or_O(2)
                # m[2] = "X"
        if x > 3 or x < 0 or y > 3 or y < 0:
            print("Coordinates should be from 1 to 3!")
            enter_the()
    else:
        print("You should enter numbers!")
        enter_the()

wins_count = False
winner = ""

def who_wins():
    global m
    global winner
    global wins_count

    count_x = m.count("X")
    count_o = m.count("O")

    if m[0] == m[1] and m[0] == m[2] and m[0] != " ":
        wins_count = True
        winner = "{} wins".format(m[2])
    if m[3] == m[4] and m[3] == m[5] and m[3] != " ":
        wins_count = True
        winner = "{} wins".format(m[5]) 
    if m[6] == m[7] and m[6] == m[8] and m[6] != " ":
        wins_count = True
        winner = "{} wins".format(m[8]) 
    if m[0] == m[3] and m[0] == m[6] and m[0] != " ":
        wins_count = True
        winner = "{} wins".format(m[6]) 
    if m[1] == m[4] and m[1] == m[7] and m[1] != " ":
        wins_count = True
        winner = "{} wins".format(m[7])  
    if m[2] == m[5] and m[2] == m[8] and m[2] != " ":
        wins_count = True
        winner =  "{} wins".format(m[8]) 
    if m[0] == m[4] and m[0] == m[8] and m[0] != " ":
        wins_count = True
        winner =  "{} wins".format(m[8]) 
    if m[2] == m[4] and m[2] == m[6] and m[2] != " ":
        wins_count = True
        winner = "{} wins".format(m[6])
    
    while wins_count == True:
        print(winner)
        exit()

    while count_o + count_x == 9:
        print("Draw")
        exit()

print_map()


while Go == True:
    enter_the()
    print_map()
    who_wins()



