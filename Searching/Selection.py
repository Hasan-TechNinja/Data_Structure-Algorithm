def Selection(nums):
    length = len(nums)
    for i in range(length-1):
        minpos = i
        for j in range(i, length):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
nums = [ 5, 3, 8, 6, 7, 2]
result = Selection(nums)
print(result)