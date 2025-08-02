nums = [5,6,7,7,1,1,3,3,3]
# freq_map = dict()
# for i in range (0, len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]] += 1
#     else:
#         freq_map[nums[i]] = 1
# print(freq_map[1])
# method 2
hash_map = {}
n = len(nums)
for i in range (0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
print(hash_map)