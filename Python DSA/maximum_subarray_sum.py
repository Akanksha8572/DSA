# find  the maximum subarray sum 
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
# brute
total = 0
maxi = float('-inf')
# for i in range (0,n):
#     total = 0
#     for j in range(i,n):
#         total = total+nums[j]
#         maxi = max(maxi, total)
# print(maxi)
# optimal
for i in range(0,n):
    total = total + nums[i]
    maxi = max(maxi, total)
    if total < 0:
        total = 0
print(maxi)