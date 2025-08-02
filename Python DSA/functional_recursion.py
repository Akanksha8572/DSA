#  print sum of 1  to n 
# def func(n):
#     if n == 1:
#         return 1
#     return n+func(n-1)
# result = func(10)
# print(result)
# find the factorial of the number using recursion 
def func(n):
    if n == 0 or n == 1:
        return 1
    return n*func(n-1)
result = func(5)
print(result)
