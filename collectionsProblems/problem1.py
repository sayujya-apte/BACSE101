nums = [1, 2, 2, 3, 4, 4, 5]
nums_unq = [] 

for i in nums:
    if i not in nums_unq:
        nums_unq.append(i)

print(nums_unq)

