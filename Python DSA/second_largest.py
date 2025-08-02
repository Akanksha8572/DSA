# nums = [23, 45,61,55,33,77,66,7,6,99]
# TC = O(N) AND SC = O(1)
# largest = float('-inf')
# s_largest = float('-inf')
# n = len(nums) - 1
# for i in range(0, n):
#     if nums[i] > largest:
#         largest = nums[i]
# for i in range(0,n):
#     if nums[i] > s_largest and nums[i] <= largest:
#         s_largest = nums[i]

# print(s_largest) 
# optimal way --- TC = O(N) AND SC = O(1)
nums = [23, 45,61,55,33,77,66,7,6,99]
largest = float('-inf')
s_largest = float('-inf')
n = len(nums)
for i in range(0, n):
    if nums[i]> largest:
        s_largest = largest
        largest = nums[i]
    elif nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]
print(s_largest)