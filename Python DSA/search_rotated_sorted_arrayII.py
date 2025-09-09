# search in rotated sorted array 
nums = [10,11,11,12,12,13,13,13,1,2,3,4]
target = 12
# brute 
# n = len(nums)
# for i in range(0,n):
#     if nums[i] == target:
#         result = 'true'
#         break
#     else:
#         result = 'false'
# print(result)
# TC = O(N) and SC = O(1)
# optimal way
n = len(nums)
low = 0
high = n-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
        print('true')
        break
    if nums[low] == nums[mid] == nums[high]:
        low += 1
        high -= 1
        continue
    if nums[mid] <= nums[high]:
        if nums[mid] < target <= nums[high]:
            low = mid+1
        else:
            high = mid-1
    else:
        if nums[low] <= target < nums[mid]:
            high = mid-1
        else:
            low = mid+1
else:
    print('false') 
# on avg case TC = O(N) and SC = O(1)
# on worst case TC =(N/2) ans SC = O(1)

