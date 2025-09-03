# Lower bound [smallest index such that nums[i]>= target]
nums = [1,1,1,2,3,4,5,6,7,7,7,9,12,12,13]
target = 1
n = len(nums)
lb = n
low = 0 
high = n-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] >= target:
        lb = mid
        high = mid-1
    else:
        low = mid+1
print(lb)
# TC = O(log N) N = num of element
# SC = O(1)
