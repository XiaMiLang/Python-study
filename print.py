# \r 回到本行開頭位置
# \b 游標位置退一位
# end=""  設定行的結束符號為""
# end="/" 設定行的結束符號為"/"

# import time
# for i in range(10):
#     print("\r離城市退出還剩 {} 秒".format(9-i), end="/")
#     time.sleep(1)

# import time
# for i in range(10):
#     print("\r離城市退出還剩 {} 秒".format(9-i), end="")
#     time.sleep(1)
######################################################

# 實現動態Loading...效果
# flush引數主要是重新整理， 預設為 flush = False，不重新整理
# import time
# print("Loading", end = "")
# for i in range(6):
#     print(".", end = "", flush=True)
#     time.sleep(1)

# import time
# for i in range(6):
#     print("\rLoading" + "."*i, end="")
#     time.sleep(1)
#######################################################

# 實現刪除效果
# import time
# s = "枝上柳綿吹又少，天涯何處無芳草"
# l = len(s)
# for i in range(l):
#     print("\r" + s[:(l-1-i)] + " ", end="")
#     time.sleep(1)
#######################################################

print("I am = I'm")
print("I have = I've")
print("I will = I'll")
print("I had / would = I'd")

a = 1
b = 2
c = 1
print((a == b == c) == (1 or 2))