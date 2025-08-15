# Rearrange array element bu sign
nums = [5,10,-3,-1,-10,6]
n = len(nums)
# pos = []
# neg = []

# # Separate positive and negative numbers
# for i in range(n):
#     if nums[i] >= 0:
#         pos.append(nums[i])
#     else:
#         neg.append(nums[i])

# # Rebuild nums with alternating pos and neg
# for i in range(n // 2):
#     nums[2 * i] = pos[i]
#     nums[2 * i + 1] = neg[i]

# print(nums)
# TC = O(n+n/2) , SC = o(N)
# OPTIMAL 
result = [0] *n
posindex = 0
negindex = 1
for i in range(0,n):
    if nums[i] >= 0:
        result[posindex] = nums[i]
        posindex += 2
    else:
        result[negindex] = nums[i]
        negindex +=2
print(result)
# TC = O(N), SC = O(1)


