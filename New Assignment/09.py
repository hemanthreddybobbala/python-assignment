def min_max_sum(nums):
    if not nums:
        return None
    else:
        return min(nums), max(nums), sum(nums)
nums = [1,2,3,4,5,6,45,80]
print(min_max_sum(nums))
