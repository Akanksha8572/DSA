# find the largest elements in array 
# method 1
# nums = [1,3,4-56, 34,99,6,2,55]
# largest = nums[0]
# n = len(nums) - 1
# for i in range(0, n):
#     if nums[i] > largest:
#         largest = nums[i]
# print(largest) 
# method 2
nums = [1,3,4-56, 34,99,6,2,55]
largest = float('-inf')
n = len(nums) - 1
for i in range(0, n):
    if nums[i] > largest:
        largest = nums[i]
print(largest) 
