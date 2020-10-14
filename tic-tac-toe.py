print("Enter cells: ")
ins = input()
m = [i for i in ins]

print("---------")
print("| {} {} {} |".format(m[0], m[1], m[2]))
print("| {} {} {} |".format(m[3], m[4], m[5]))
print("| {} {} {} |".format(m[6], m[7], m[8]))
print("---------")

count_x = m.count("X")
count_o = m.count("O")

def who_wins():
    wins_count = 0
    if m[0] == m[1] == m[2]:
        wins_count += 1
        winner = "{} wins".format(m[2])
    if m[3] == m[4] == m[5]:
        wins_count += 1
        winner = "{} wins".format(m[5]) 
    if m[6] == m[7] == m[8]:
        wins_count += 1
        winner = "{} wins".format(m[8]) 
    if m[0] == m[3] == m[6]:
        wins_count += 1
        winner = "{} wins".format(m[6]) 
    if m[1] == m[4] == m[7]:
        wins_count += 1
        winner = "{} wins".format(m[7]) 
    if m[2] == m[5] == m[8]:
        wins_count += 1
        winner =  "{} wins".format(m[8]) 
    if m[0] == m[4] == m[8]:
        wins_count += 1
        winner =  "{} wins".format(m[8]) 
    if m[2] == m[4] == m[6]:
        wins_count += 1
        winner = "{} wins".format(m[6])

    if wins_count > 1:
        print("Impossible")
    elif wins_count == 0:
        if count_o - count_x >= 2 or count_x - count_o >= 2:
            print("Impossible")
        elif count_o + count_x < 9:
            print("Game not finished")
        else:
            print("Draw")
    elif wins_count == 1:
        print(winner)
    
who_wins()                                