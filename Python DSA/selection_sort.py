# sort an array using selection sorting method in ASD
nums = [5, 7, 8, 9 ,3, 1 ,2]
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
                print(f"New min index at position {j} with value {nums[j]}")
        nums[i], nums[min_idx] = nums[min_idx], nums[i]  # ✅ swap outside the inner loop

selection_sort(nums)
print(nums)

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] > nums[min_idx]:
                min_idx = j
                print(f"New min index at position {j} with value {nums[j]}")
        nums[i], nums[min_idx] = nums[min_idx], nums[i]  # ✅ swap outside the inner loop

selection_sort(nums)
print(nums)