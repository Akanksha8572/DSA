# Find the number that appears odd number of times
arr = [5,3,3,7,1,7,1]
# brute 
hash_map = {}
for num in arr:
    hash_map[num] = hash_map.get(num,0)+1
for key in hash_map:
    if hash_map[key] == 1:
        print(key)
# TC = O(N)+O(N/2+1)
# Optimal 
ans = 0
for num in arr:
    ans = ans^num
print(ans)