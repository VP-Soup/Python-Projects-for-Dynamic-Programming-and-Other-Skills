def maxContiguousSum(nums):
    final_max = nums[0]
    temp_max = nums[0]
    for i in range(1, len(nums)):
        temp_max = max(nums[i], temp_max + nums[i])
        final_max = max(temp_max, final_max)
    return final_max

# time: O(n)
# space: O(1)