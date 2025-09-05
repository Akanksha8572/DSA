# find the first and last occurrence of a given number in sorted array
nums = [1,2,3,3,3,3,3,5,6,8,8,9,10]
target = 8
# brute approch
n = len(nums)
first = -1
last = -1
for i in range(0,n):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
    
print(first,last)
# OPTIMAL way 
lb = -1
low = 0 
high = n-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] >= target:
        lb = mid
        high = mid-1
    else:
        low = mid+1
ub = -1
low = 0 
high = n-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] > target:
        ub = mid
        high = mid-1
    else:
        low = mid+1
print(lb,ub-1)