# sort an array or list using bubble sort 
nums = [1,4,2,6,8,6]
def bubble_sort(nums):
    n=len(nums)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
bubble_sort(nums)
print(nums)
# nums = [1, 4, 2, 6, 8, 6]

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):  # i from n-1 down to 0
        for j in range(0, i):     # j goes up to i-1
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

bubble_sort(nums)
print(nums)