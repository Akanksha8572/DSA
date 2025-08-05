# two sum 
nums = [2,3,4,5,6,7,8,9,1]
target = 17
# brute 
n= len(nums)
# for i in range (0,n-1):
#     for j in range (i+1,n):
#         if nums[i]+nums[j] == target:
#             print(i,j)
# optimal
hash_map = {}
remaining = 0
for i in range (0,n):
    remaining = target - nums[i]
    if remaining in hash_map:
        print (hash_map[remaining], i)

    hash_map[nums[i]] = i