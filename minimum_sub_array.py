def minimum_size(nums,s):
    total = left = 0
    result = len(nums) + 1
    for right, n in enumerate(nums):
        total += n
        while total >= s:
            print "in here",  left, right
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
            print result
    return result if result <= len(nums) else 0