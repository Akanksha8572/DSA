#  find the missing number in an array 
nums = [0,1,2,3,5,6,7,8,9]
n = len(nums)
# Brute 
# for i in range (0, n+1):
#     if i not in nums:
#         print(i)
# # Better 
# freq = {}
# for i in range (0, n+1):
#     freq[i] = 0
# for nums in nums:
#     freq[nums] = 1
# for k, v in freq.items():
#     if v == 0:
#         print(k)
# optimal
print((n * (n + 1)) // 2 - sum(nums))
