# emp = open("emp.txt", "r")      # r= read, w=write, a=append
# print(emp.read())
# print(emp.readable())
# print(emp.readlines()[0])
# for em in emp.readlines():
#     print(em)

# emp = open("emp.txt", "a")        # r= read, w=write, a=append
# emp.write("Toby -  Human Resources")    #把 "Toby - Human Resources" 加入到了 emp.txt 的最後一行接續
# emp.write("\nKelly - Customer Service")
# emp.close()

# emp = open("emp.txt", "w")          # r= read, w=write, a=append
# emp.write("Toby -  Human Resources")
# emp.write("\nKelly - Customer Service")     # 把這兩行覆蓋寫入 emp.txt
# emp.close()

# emp = open("emp1.txt", "w")          # 因為 emp1.txt 不存在，所以 python 會新建一個 emp1.txt
# emp.write("Toby -  Human Resources")
# emp.write("\nKelly - Customer Service")     # 把這兩行覆蓋寫入 emp1.txt
# emp.close()

emp = open("eemp.html", "w")          # 因為 eemp.html 不存在，所以 python 會新建一個 eemp.html
emp.write("<p> Hello, How are you? <p>")
emp.close()