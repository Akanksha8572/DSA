#  four sum problem
#  brute approch 
nums = [1,0,-1,0,-2,2,5,9]
target = 0
# n = len(nums)
# my_set = set()
# if n < 4:
#     print()
# for i in range (0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 total = nums[i]+nums[j]+nums[k]+nums[l]
#                 if total == target:
#                     temp = [nums[i],nums[j],nums[k],nums[l]]
#                     temp.sort()
#                     my_set.add(tuple(temp))
# result = []
# for ans in my_set:
#     result.append(list(ans))
# print(result)
# # TC = O(N^4) and SC = O(N)
# # better approch
# for i in range(0,n):
#     for j in range(i+1,n):
#         hash_set = set()
#         for k in range(j+1,n):
#             fouth = target-(nums[i]+nums[j]+nums[k])
#             if fouth in hash_set:
#                 t = [nums[i],nums[j],nums[k], fouth]
#                 t.sort()
#                 my_set.add(tuple(t))
#             hash_set.add(nums[k])
# result = []
# for ans in my_set:
#     result.append(list(ans))
# print(result)
# TC = O(N^3) and SC =O(N)
# Optimal way 
def four_sum(nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(0,n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            k = j+1
            l = n-1
            while k<l:
                total = nums[i]+nums[j]+nums[k]+nums[l]
                if total == target:
                    ans.append([nums[i],nums[j],nums[k],nums[l]])
                    k += 1
                    l -= 1
                    while k<l and nums[k] == nums[k-1]:
                        k += 1
                    while l>k and nums[l] == nums[l+1]:
                        l -= 1
                elif total< target:
                    k += 1
                else:
                    l -= 1
    return  ans
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(four_sum(nums, target))            

