###check the print factor or divisors #TC O(N)#SC = O (k)  where  k is the number of the factor
# def is_factor(n):
#     num = n
#     result = []
#     for i in range (1, num+1):
#         if num % i == 0 :
#             result.append(i)
#     return result            

# print(is_factor(20))
## better solution for this #TC O(N)#SC = O (k)  where  k is the number of the factor
# def is_factor(n):
#     num = n
#     result = []
#     for i in range(1, (num//2)+1):
#         if num % i == 0:
#             result.append(i)

#     result.append(num)
#     return result
    
# print(is_factor(10))
# optimal way of doing that ## time complexity for is (sqrt(n))+O(N log N)# SC = O(k), where k is the number of the factor
from math import sqrt
def is_factor(n):
    num = n
    result = []
    for i in range (1, int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            if num//i != i:
                result.append(num//i)
    result.sort()
    return result
print(is_factor(36))


