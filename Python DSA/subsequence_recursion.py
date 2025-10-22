# print all the subsequences
nums = [1,2,3]
result = [ ]

def func(index,subset):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    func(index+1, subset)
    subset.pop()
    func(index+1,subset)
func(0,[])
print(result)
