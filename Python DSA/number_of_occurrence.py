# count the occurrence of number in a sorted array with duplicate
nums = [1,2,3,3,3,3,3,3,5,6,8,9,9,10]
target = 3
# make sure the array should sorted 
# brute force approch
n = len(nums)
first = -1
last = -1
for i in range(0,n):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
if first == -1:
    print(0)
print(last-first+1)
# TC = O(N) and  SC = O(-1)
# optimal way
def lower_bound(nums,target):
    n = len(nums)
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
    return lb
def upper_bound(nums,target):
    n = len(nums)
    ub = n
    low = 0 
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid]> target:
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub
lb = lower_bound(nums,target)
if lb == -1:
    print(0)
else:
    ub = upper_bound(nums,target)
    print(ub-lb)
# TC = O(2logN) = O(log N) and SC = O(1)
