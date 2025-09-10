# Find the minimum in rotated sorted array
# array should be sorted 
# nums = [4,5,6,7,0,1,2]
nums = [7,8,9,1,2,3,4]
# brute force approch 
n = len(nums)
mini = float('inf')
for i in range (0,n):
    mini = min(mini,nums[i])
print(mini)
# TC - O(N),SC - O(1)
# Optimal approch
n = len(nums)
low = 0
high = n-1
mini = float('inf')
while low <= high:
    mid = (low+high)//2
    if nums[mid] <= nums[high]:
        mini = min(mini,nums[mid])
        high = mid-1
    else:
        mini = min(mini,nums[low])
        low = mid+1
print(mini)
# TC = O(log N), SC = O(1)