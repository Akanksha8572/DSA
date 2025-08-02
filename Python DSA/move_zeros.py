# move zeros to the end , with in place changes 

nums = [1,2,3,45,60,0,3,4,0]
n = len(nums)
# temp = []
# for i in range (0,n):
#     if nums[i] != 0:
#         temp.append(nums[i])
# ntemp = len(temp)
# for i in range (0,ntemp):
#     nums[i] = temp[i]
# for i in range (ntemp,n):
#     nums[i]= 0
# print(nums)
# OPTTIMAL way
if len(nums) == 1:
    print(nums)
i = 0
while i < len(nums):
    if nums[i] == 0:
        break
    i +=1
if i == len(nums):
    print(nums)
j = i+1
while j < len(nums):
    if nums[j] != 0:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
    j += 1
print(nums)