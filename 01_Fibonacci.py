def fib(n):
    a, b, sum = 1, 1, 0
    if n==0:
        print(0)
    if n==1 or n==2:
        print(1)
    if n>=3:
        for i in range(n-2):
            sum = a+b
            a = b
            b = sum
        print(sum)
num = int(input('How many Fibonacci numbers do you want?'))
fib(num)

# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return a
# # 输出了第10个斐波那契数列
# num = int(input('How many Fibonacci numbers do you want?'))
# print(fib(num))