# check if the array is sorted or not 
# TC = O (N) where N is length of an array, SC = O(1)
nums = [1, 2, 32,4 ,5,6,7]
n = len(nums)
is_sorted = True
for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        is_sorted = False
        break
print(is_sorted)
