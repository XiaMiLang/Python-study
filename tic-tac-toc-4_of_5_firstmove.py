ins = input("Enter cells: ")
m = [i for i in ins]


def print_map():
    print("---------")
    print("| {} {} {} |".format(m[0], m[1], m[2]))
    print("| {} {} {} |".format(m[3], m[4], m[5]))
    print("| {} {} {} |".format(m[6], m[7], m[8]))
    print("---------")

def enter_the():
    ins_coordinates = input("Enter the coordinates: ")
    x, y = (ins_coordinates.split() +[None])[:2]

    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if x == 1 and y == 1:
            if m[6] == "X" or m[6] == "O":
                print(m[6])
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                m[6] = "X"

        if x == 2 and y == 1:
            if m[7] == "X" or m[7] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                m[7] = "X"

        if x == 3 and y == 1:
            if m[8] == "X" or m[8] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                m[8] = "X"

        if x == 1 and y == 2:
            if m[3] == "X" or m[3] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                m[3] = "X"

        if x == 2 and y == 2:
            if m[4] == "X" or m[4] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()         
            else:
                m[4] = "X"

        if x == 3 and y == 2:
            if m[5] == "X" or m[5] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                m[5] = "X"
                
        if x == 1 and y == 3:
            if m[0] == "X" or m[0] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                m[0] = "X"
                
        if x == 2 and y == 3:
            if m[1] == "X" or m[1] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                m[1] = "X"   
        
        if x == 3 and y == 3:
            if m[2] == "X" or m[2] == "O":
                print("This cell is occupied! Choose another one!")
                enter_the()
            else:
                m[2] = "X"
        if x > 3 or x < 0 or y > 3 or y < 0:
            print("Coordinates should be from 1 to 3!")
            enter_the()
    else:
        print("You should enter numbers!")
        enter_the()


print_map()
enter_the()
print_map()

