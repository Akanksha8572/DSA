# srock bye and sell 
prices = [7,2,1,5,6,4,8]
# maxi_profit = 0
n = len(prices)
# for i in range(0,n):
#     for j in range(i+1, n):
#         if prices[j] > prices[i]:
#             p = prices[j]-prices[i]
#             maxi_profit = max(maxi_profit, p)
# print(maxi_profit)
# TC = O(N^2), SC= O(1)
# Optimal way 
max_profit = 0
min_price = float('inf')  # Keep track of the lowest price so far

for i in range(0, n):
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit, prices[i] - min_price)

print(max_profit)
# TC = O(N) , SC = O(1)