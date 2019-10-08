# try:
#     number= int(input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid Input")

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    # print("Divided by zero")
    print(err)
except ValueError as err:
    print("Invalid Input! ", err)
