# find target index using liner searcch 
nums = [5, 3, 4,5,4,7,10]
target = 4
n = len(nums)
for i in range (0, n):
    if nums[i] == target:
        print(i)