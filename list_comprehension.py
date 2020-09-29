# list comprehension

# old_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# new_list = []               #原始需用三行寫成的程式，可改用如下寫成一行
# for x in old_list: 
#     new_list.append(x*2)

# new_list = [x for x in old_list if x % 2 == 0]          #[2, 8, 34]
# new_list = [x for x in old_list if x >= 8]              #[8, 13, 21, 34, 55]
# new_list = [x for x in old_list if x <13]               #[1, 1, 2, 3, 5, 8]
# new_list = [x*2 for x in old_list if x %2 == 1]         #[2, 2, 6, 10, 26, 42, 110]
# new_list = [x*2 for x in old_list]                      #[2, 2, 4, 6, 10, 16, 26, 42, 68, 110]
# print(new_list)

# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# # create a list of days here
# days_list = [x//(60*60*24) for x in seconds ]
# print(days_list)


# 把 list 內的數值, 每項加上前項. 如 輸入 15325
# 得到結果 [1, 6, 9, 11, 16]
# numbers = [int(n) for n in input()]
# new_numbers = [x for x in numbers]

# for n in range(0, len(numbers)):
#     total = 0
#     for m in range(0, n + 1):
#         total += numbers[m]
#     new_numbers[n] = total
# print(new_numbers)

# 以下是別人的寫法
# a = [int(x) for x in input()]
# the_list = [sum(a[0:i]) for i in range(1, len(a) + 1)]

# print(the_list)

 