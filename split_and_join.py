# # split example
# definition = input()  # 'Coin of the realm is the legal money of the country' 
# print()
# print(definition)

# print(definition.split())
# # ['Coin', 'of', 'the', 'realm', 'is', 'the', 'legal', 'money', 'of', 'the', 'country']

# print(definition.split("legal"))
# # ['Coin of the realm is the ', ' money of the country']

# # maxsplit example
# print(definition.split("of", 1))
# # ['Coin ', ' the realm is the legal money of the country']

# print(definition.split("of"))
# # ['Coin ', ' the realm is the legal money ', ' the country']

# # If the separator doesn't occur in the string, 
# # then the result of the method is a list with the original string as its only element:
# print(definition.split("what"))

# # Thus, in all cases split() allows us to convert a string into a list.
# # It may also be useful to read input directly into several variables with split():
# name, surname = input().split()  # Forrest Gump
# print(name)     # Forrest
# print(surname)  # Gump
# It's pretty efficient when you know the exact number of input values. 
# In case you don't, it's likely to result in ValueError with a message 
# telling you either that there are too many values to unpack or not enough of them. So keep that in mind!
################################################################################

# join a list
# word_list  = ["dog", "cat", "rabbit", "parrot"]
# print(" ".join(word_list))  # "dog cat rabbit parrot"
# print("".join(word_list))  # "dogcatrabbitparrot"
# "_".join(word_list)  # "dog_cat_rabbit_parrot"
# " and ".join(word_list)  # "dog and cat and rabbit and parrot"

# join only works on strings. If its integers, it will not work
# you will need to convert integers to strings
# int_list = [1, 2, 3]
# " ".join(int_list)  # TypeError!

# str_list = ["1", "2", "3"]
# " ".join(str_list)  # "1 2 3"

# split multiple lines
# splitlines() example
# \r 回到本行開頭位置
# long_text = 'first line\nsecond line\rthird line\r\nfourth line'
# print(long_text)
# print(long_text.splitlines())
# ['first line', 'second line', 'third line', 'fourth line']

# The method has an optional argument keepends that has a True or False value.
# If keepends = True linebreaks are included in the resulting list:
# keepends
# long_text = 'first line\nsecond line\rthird line\r\nfourth line'
# long_text.splitlines(keepends=True)
# ['first line\n', 'second line\r', 'third line\r\n', 'fourth line']
##########################################################################

# ins = input().split()
# count = 0
# for i in ins:
#     if i == "A":
#         count +=1
# result = count / len(ins)
# print(round(result, 2))

# ins = input().split()
# print(round(ins.count("A") / len(ins), 2))
#############################################################################

# random_numbers = ["1", "22", "333", "4444", "55555"]
# print("\n".join(random_numbers))
###################################################################

ins = input().title().split()

# for i in range(len(ins)):
#     ins[i] = ins[i].title()

# ins[0] = str(ins[0].lower)
# print(ins[0])

# ins[0] = ins[0].replace(ins[0], ins[0].lower())
ins[0] = ins[0].lower()

result = "".join(ins)
print(result)