# search in rotated sorted array 
# nums = [1,4,5,6,8,9,10,11,15,20]
# target = 4
# temp = -1
# # brute fouce approch 
# n = len(nums)
# for i in range(0,n):
#     if nums[i] == target:
#         temp = i
#         break
#     else:
#         temp = 0
# print(temp)
# TC = O(N) and SC = O(1)
# optimal way 
nums = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]
target = 4
n = len(nums)
low = 0 
high = n-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
        print(mid)
        break
    if nums[mid] <= nums[high]:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        if nums[low] <= target <= nums[mid]:
            high = mid-1
        else:
            low = mid+1
else:
    print(-1)
# TC = O( log N) and SC = 0(1)