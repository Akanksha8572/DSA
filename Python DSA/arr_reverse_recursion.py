# reverse an array using recursion 
# nums = [1, 2, 3, 4, 5, 6 ,7]
# def func(nums, left, right):
#     if left >= right:
#         return
#     nums[left],nums[right] = nums[right],nums[left]
#     func(nums, left+1, right-1)
#     return nums

# result = func(nums, 0, len(nums) - 1)
# print(result)
# nums = [1, 2, 3, 4, 5, 6, 7]
# left = 0
# right = len(nums) - 1

# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]
#     left += 1
#     right -= 1

# print(nums)

# s = "nitin"
# def func(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# print(func("nwern"))
# using recursion 
s = "nitin"
def func(s, left, right):
    if left >= right:
        return True
    if left != s[right]:
        return False
    return func(s, left + 1, right - 1)
func(s, 0, len(s) - 1)
print (s)