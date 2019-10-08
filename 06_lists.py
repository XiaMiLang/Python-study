friends = ["Kevin", "Karen", "Jim"]
print(friends)        #把 friends 所有資料印出
print(friends[0])       #把 friends 第 0 位資料印出
print(friends[1])       #把 friends 第 1 位資料印出
print(friends[2])       #把 friends 第 2 位資料印出
print(friends[1:])       #把 friends 第 1 位及後面資料印出
print(friends[:1])       #把 friends 第 1 位之前資料印出
print(friends[-1])       #把 friends 從後面數, 第 1 位資料印出
print(friends[-2])       #把 friends 從後面數, 第 2 位資料印出
print(friends[-3])       #把 friends 從後面數, 第 3 位資料印出
friends[1]="Mike"       #將friends[1]改為 "Mike"
print(friends[1])

test = ["Kevin", 999, False]
print(test)        #把 friends 所有資料印出
print(test[0])       #把 friends 第 0 位資料印出
print(test[1])       #把 friends 第 1 位資料印出
print(test[2])       #把 friends 第 2 位資料印出
print(test[1:])       #把 friends 第 1 位及後面資料印出
print(test[:1])       #把 friends 第 1 位之前資料印出
print(test[1]*2)        #test[1]資料型態為數值
print(test[2]==False)   # test[2] 資料為 boolean 值(不是字串), 所以答案為 True