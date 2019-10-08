lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tiffany"]
print(friends)
print(friends.extend(lucky_numbers))    #不能這樣印?
friends.extend(lucky_numbers)       # 把 friends 資料加長
print(friends)
friends.append(lucky_numbers)       # 把 friends 資料加 [lucky_numbers]
#friends.append("ApendMike", "appendJason", "appendJeff") # append 只能加一個 argument(參數)
print(friends)
print(friends[-1])

print(friends)
friends.insert(1, "Jack")       #插入到位置1
print(friends)
friends.remove("Jack")          #直接填上要移除的東西
print(friends)
#friends.clear()         #移除所有內容
friends.pop()           #把名單踢出一個, 如無指定就是踢最後一個
print(friends.index("Jim"))     #找到Jim的index位置
print(friends.count("Jim"))     #數一下有多少個Jim
friendsss = ["Daniel", "Jack", "Apple", "Banana"]
print(friendsss)    #如果函式收到的是一個可變物件（比如字典或者列表）的引用，就能修改物件的原始值——相當於傳址。
bb = friendsss
print(bb)
bb.sort()
print(bb)
print(friendsss)
name = "Jeff"       #如果函式收到的是一個不可變物件（比如數字、字元或者元組）的引用，就不能直接修改原始物件——相當於傳值
nn=name
nn = "Ximo"
print(name)
print(nn)
friendsss.reverse()
print(friendsss)        #把序列倒反過來
friends2 = friends.copy()   #複製過去
print(friends)
print(friends2)
friends2.insert(1, "Ximo")
print(friends)
print(friends2)
