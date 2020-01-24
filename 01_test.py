# for i in range(1, 10):
#     for j in range(1, 10):
#         # print(j, "*", i, "=", i*j, " ", end='')
#         # print('{j} * {i} = {result} '.format(j=j, i=i, result=i*j), end=' ')
#         print(f'{ j} * { i} = {j*i}  ', end='')
#         # print("%d*%d=%2d" % (j, i, j*i), end=" ")
#     print()
#

# all, at, once = 1, 10 ,15
# print(all)
# print(at)
# print(once)

# i = int(input("Please input i: "))
# j = int(input("Please input j: "))
# print(i, j)
# li = [[0]*i for jj in range(j)]
# for jj in range(j):
#     for ii in range(i):
#         li[jj][ii] = 90
# print (li)

# fib = [0]*100
# fib[0] = 1
# fib[1] = 1
# for i in range(2,100):
#     fib[i] = fib[i-1] + fib[i-2]
# for i in range(100):
#     print(i+1, fib[i])

# m = int(input("input number of rows: "))
# n = int(input("input number of columns: "))
# result = [[0]*m for nn in range(n)]
# for mm in range(m):
#     for nn in range(n):
#         result[nn][mm] = mm*nn
# print(result)

# m = int(input("input number of rows: "))
# # n = int(input("input number of columns: "))
# # result = [[0]*m for nn in range(n)]
# # for mm in range(m):
# #     for nn in range(n):
# #         result[nn][mm] = mm*nn
# # print(result)
# # for mm in result:
# #     print(mm)

# cc=[]
# c = input("please input: ")
# # print(c.split(" "))
# for i in range(int(len(c.split(" ")))):
#     cc.append(c.split(" ")[i])
# print(cc)
# print(cc[0])
# print(cc[1])
# print(cc[2])
# def triangle_check(a, b, c):
#     if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
#         print("Yes, this is a triangle")
#     else:
#         print("No, this is not a triangle")
# triangle_check(int(cc[0]), int(cc[1]), int(cc[2]))

# for i in range(1, 10):
#     print(str(i)*i)

# for i in range(1, 6):
# #     print(str(i)*i)
# # for i in range(6, 1, -1):
# #     print(str(i)*i)

# for i in range(1, 6):
#     print("*"*i)
# for i in range(6, 0, -1):
#     print("*"*i)

# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')
# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# from math import sqrt
# def isprime(x):
#     if x == 1:
#         return False
#     k = int(sqrt(x))
#     for j in range(2, k + 1):
#         if x % j == 0:
#             return False
#     return True
# for i in range(2, 101):
#     if isprime(i):
#         print(i, end=' ')  ###第一类输出
#         # print(i)  ###第二类输

# alpha=digit=0
# key = input("Please input: ")
# for n in key:
#     if n.isdigit():
#         digit+=1
#     if n.isalpha():
#         alpha+=1
# print("digits: ", digit)
# print("alphas: ", alpha)

# cc=[]
# # c = input("please input: ")
# # odd=even=0
# # # for i in range(int(len(c.split(" ")))):
# # # for i in range(len(c.split(" "))):
# # for i in c.split(" "):
# #     # cc.append(c.split(" ")[i])
# #     cc.append(i)
# # for letter in cc:
# #     print(letter)
# #     if (int(letter)%2==0):
# #         even+=1
# #     else:
# #         odd+=1
# # print("odd: ", odd)
# # print("even: ", even)

# from sympy import *
# x = Symbol('x')
# y = Symbol('y')
# z = Symbol('z')
# a = Symbol('a')
# b = Symbol('b')
# c = Symbol('c')
# f1 = 2*x-y
# f2 = 4*x-2*y
# print(solve([f1, f2]))

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for a in x:
#     print(type(a), a)
#     for b in x:
#         if b == a:
#             continue
#         for c in x:
#             if c == a or c == b:
#                 continue
#             for d in x:
#                 if d == a or d ==b or d == c:
#                     continue
#                 for e in x:
#                     if e == a or e == b or e == c or e == d:
#                         continue
#                     for f in x:
#                         if f == a or f == b or f == c or f ==d or f == e:
#                             continue
#                         for g in x:
#                             if g == a or g == b or g == c or g == d or g == e or g == f:
#                                 continue
#                             for h in x:
#                                 if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
#                                     continue
#                                 for i in x:
#                                     if i == a or i == b or i == c or i == d or i == e or i == f or i == g or i == h:
#                                         continue
#                                     for j in x:
#                                         if j == a or j == b or j == c or j == d or j == e or j == f or j == g or j == h or j == i:
#                                             continue
#                                         if (a+c+d == 19) and (a+d+e==18) and (b+c+f==11) and (d+e+g==16) and (f+h+i==17) and (g+h+j==22):
#                                             print(a, b, c, d, e, f, g, h, i, j)


# from sympy import *
# var('a b c d e f g h i j')
# print(solve([a+c+d-19, a+d+e-18, b+c+f-11, d+e+g-16, f+i+h-17, h+g+j-22]))

n = int(input("請輸入一個整數"))
sum = 1

for i in range(1, n):
    print (i)

