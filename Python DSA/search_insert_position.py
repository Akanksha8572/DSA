# search the insert position
nums = [1,3,4,8,9,14,15,19,20,21]
target = 4
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