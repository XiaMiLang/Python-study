# sentence = "London is the capital of Great Britain."
# sentence = sentence.lower()

# print(sentence.upper())
# sentence = sentence.replace("a", "x", 2)
# print(sentence)
# sentence.capitalize()
# print(sentence)
#########################################################

# python 內的字串內容是複製過去的，屬記憶體內的兩個不同位置 <--需確認如何說為正確
ins = input()
strings_to_delete = ["?", "!", ".", ">", ","]
print(ins)
ins = ins.lower()

for i in ins:
    for s in strings_to_delete:
        ins = ins.replace(s, "")

print(ins)
