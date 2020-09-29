# original list
# school = [["Mary", "Jack", "Tiffany"], ["Brad", "Claire"], ["Molly", "Andy", "Carla"]]
# print(school)

# student_list = []
# for class_group in school:
#     for student in class_group:
#         student_list.append(student)
# print(student_list)

# student_list = [student for class_group in school for student in class_group]
# print(student_list)
##############################################################

# matrix = [[j for j in range(5)] for i in range(2)]
# print(matrix)

# matrix = []
# for i in range(2):
#     matrix.append([])
#     for j in range(5):
#         matrix[i].append(j)
# print(matrix)
##############################################################

# nested_letters = ["a", "b", ["c", "d"], "e"]
# new_nes = []
# for nes in nested_letters:
#     for n in nes:
#         new_nes.append(n)
# print(new_nes)

# nested_letters = ["a", "b", ["c", "d"], "e"]
# print([n for nes in nested_letters for n in nes])
###############################################################

# country_list = [["Moscow", "Cheboksary", "Sochi"], ["Paris", "Lyon", "Nice"],
#                 ["New York", "Dallas", "San Francisco"]]

# long_cities = []
# for country in country_list:
#     for city in country:
#         if len(city) >= 6:
#             print(city)
#             long_cities.append(city)
# print(long_cities)
############################################################

# str_numbers = input()
# int_numbers = [int(n) for n in str_numbers ]
# # numbers_len = len(numbers)
# # list_numbers = list(numbers)
# result_list_numbers = []
# for n in range(0, len(int_numbers)-1):
#     result_list_numbers.append((int_numbers[n] + int_numbers[n+1])/2)

# print(result_list_numbers)
#############################################################

# print("Enter cells: ")
# ins = input()
# m = []
# for i in ins:
#     m.append(i)
# # m = [i for i in ins]

# print("---------")
# print("| {} {} {} |".format(m[0], m[1], m[2]))
# print("| {} {} {} |".format(m[3], m[4], m[5]))
# print("| {} {} {} |".format(m[6], m[7], m[8]))
# print("---------")

# count_x = m.count("X")
# count_o = m.count("O")

# def who_wins():
#     wins_count = 0
#     if m[0] == m[1] == m[2]:
#         wins_count += 1
#         winner = "{} wins".format(m[2])
#     if m[3] == m[4] == m[5]:
#         wins_count += 1
#         winner = "{} wins".format(m[5]) 
#     if m[6] == m[7] == m[8]:
#         wins_count += 1
#         winner = "{} wins".format(m[8]) 
#     if m[0] == m[3] == m[6]:
#         wins_count += 1
#         winner = "{} wins".format(m[6]) 
#     if m[1] == m[4] == m[7]:
#         wins_count += 1
#         winner = "{} wins".format(m[7]) 
#     if m[2] == m[5] == m[8]:
#         wins_count += 1
#         winner =  "{} wins".format(m[8]) 
#     if m[0] == m[4] == m[8]:
#         wins_count += 1
#         winner =  "{} wins".format(m[8]) 
#     if m[2] == m[4] == m[6]:
#         wins_count += 1
#         winner = "{} wins".format(m[6])

#     if wins_count > 1:
#         print("Impossible")
#     elif wins_count == 0:
#         if count_o - count_x >= 2 or count_x - count_o >= 2:
#             print("Impossible")
#         elif count_o + count_x < 9:
#             print("Game not finished")
#         else:
#             print("Draw")
#     elif wins_count == 1:
#         print(winner)

# who_wins()
#####################################################

