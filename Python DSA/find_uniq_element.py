#  TC = O(2N), sc =O(N)
nums  = [1,1,1,2,2,2,3,3,3,4,5,5,5,6,6,6,7,7,8,8,8,9]
n = len(nums)
# freq_map = {}
# for i in range(0,n):
#     freq_map [nums[i]] = 0
# j = 0
# for k in freq_map:
#     nums[j] = k
#     j += 1
# print(j)
# print(nums) 
# optimal way TC  = O(N), SC = O(1)
if n == 1:
    print("1")
i = 0
j= i+1
while j < n:
    if nums[j] != nums[i]:
        i += 1
        nums[i],nums[j] = nums[j],nums[i]
    j += 1
print(i+1)
