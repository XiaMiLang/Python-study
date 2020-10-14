

# any() 只要任一有True, 即返回True
# True 可用 1 表示, False 可用 0 表示
# 事實上, 除了 0 以外的所有數字都視為 True
andy_results = [False, False]
print(any(andy_results))        # False

Tom_results = []
print(any(Tom_results))         # False


# all() 全存在則返回 True
# 但是, 如果為空值, 也返回 True

print(all(Tom_results))         # True


# 注意, any(), all() 也可用來評估非布爾值
# 空序列, 空list, 如零, 常量None 會被當作 False
# 非空序列, 則被當成True
rocket_science_scores = [0, -0, 0.0, +0]
any(rocket_science_scores)  # False
all(rocket_science_scores)  # False

math_scores = [0, 1, 2, 3]
any(math_scores)  # True
all(math_scores)  # False

biology_scores = [1, 2, 3, 4]
any(biology_scores)  # True
all(biology_scores)  # True

scores = [1, 2, 3, 4]
boolean_scores = [score >= 3 for score in scores]  # [False, False, True, True]
print(any(boolean_scores))  # True
print(all(boolean_scores))  # False

# any() 也可用來當作很好的檢查工具
# 如檢查情人節禮物, 如內容物為單數, 則印出"非好禮物"
box = [10, 20, 33]

if any([candy % 2 for candy in box]):
    print("It is not a proper gift.")
else:
    print("Perfect!")
#########################################################

# 印出1000內的質數
odds = []
for x in range(2, 1000):
    for y in range(2, x):
        if x % y == 0:
           break
    else:
        odds.append(x)
print(odds)
###########################################################

prime_numbers = []
for n in range(2, 1000):
    if all(n % i for i in range(2, n)):
        prime_numbers.append(n)
print(prime_numbers)
############################################

prime_numbers = [n for n in range(2, 1000) if all(n % i != 0 for i in range(2, n - 1))]
###########################################################

prime_numbers = [n for n in range(2, 1001) if not any(n % i == 0 for i in range(2, n))]
#############################################################

prime_numbers = []
prime_numbers.append(2)
for i in range(3, 100):
    if all(i % k for k in range(2, i)):
        prime_numbers.append(i)
#############################################################

prime_numbers = [i for i in range(2, 1001)
                 if all(i % j for j in range(2, i))]
