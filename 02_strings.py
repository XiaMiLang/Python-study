c_name = "John"
C_age = "31"
print("my name is", c_name,"and my age is", C_age)
print("my name is " + c_name + " and my age is " + C_age)

phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])        #印出位置0的字母, G
print(phrase[0:3])      #印出位置0~2的字母, Gir
print(phrase[3])        #印出位置3的字母, a
print(phrase.index("a"))    #印出a的位置
print(phrase.index("Acad"))    #印出Acad的位置
# print(phrase.index("z"));    #當要找的字不在當中時，會報錯
print(phrase.replace("Giraffe", "cat")) #取代(舊字, 新字)

