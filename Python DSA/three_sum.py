# 3 Sum
# arr = [-1,0,1,2,-1,-4]
# arr[i]+arr[j]+arr[k] = 0
# i != j != k
# brute full approch
# n = len(arr)
# arr_set = set()
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if arr[i]+arr[j]+arr[k] == 0:
#                 temp_list = [arr[i],arr[j],arr[k]]
#                 temp_list.sort()
#                 arr_set.add(tuple(temp_list))
# print([list(ans) for ans in arr_set])
#  for this TC = O(N^3) ans SC = O(no of truplets)
# better approch 
# result = set()
# for i in range(0,n):
#     my_set = set()
#     for j in range(i+1,n):
#         third = -(arr[i]+arr[j])
#         if third in my_set:
#             temp = [ arr[i],arr[j],third]
#             temp.sort()
#             result.add(tuple(temp))
#         my_set.add(arr[j])
# print([list(ans) for ans in result])
# TC = O(N^2) and SC = O(N)+O(no of triplet)
# OPTIMAL approch
nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums: list[int]) -> list[list[int]]:
    ans = []
    n = len(nums)
    nums.sort()
    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return ans

# Call and print
print(three_sum(nums))
#  TC = O(NlogN)+O(N^2) and SC = O(1) or SC = O(no of triplets)


