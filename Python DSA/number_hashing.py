n =[1,2,2,3,6,78,3,4,5,6,7,8]
m = [22,1,3,44,5,4,66,67,7,8,7,87,90,0]
# constrains : 1) 1>= n[i]<=10  ,2) n can have 10^8 elements   ,3)m can have 10^8 elements
# brute way , TC = o(n*m) or SC = O(1)
for num in m:
    count = 0 
    for x in n:
        if x == num:
            count += 1
    print (count)
# optimal way using hashing , TC = O(n+m) or SC = o(11) or O(1)
# hash_list = [0] * 11  # Index 0 to 10
# for num in n:
#     if 1 <= num <= 10:
#         hash_list[num] += 1

# # Output frequencies for numbers in list m
# for x in m:
#     if 1 <= x <= 10:
#         print(hash_list[x])
#     else:
#         print(0)
#  using dictinary
# freq_map = dict()
# for i in range (0, len(n)):
#     if n[i] in freq_map:
#         freq_map[n[i]] += 1
#     else:
#         freq_map[n[i]] = 1
        
# for x in m:
#     if x < 1 or x > 10:
#         print(0)
#     else:
#         print(freq_map[x])
