def tuple_added(nums, target):
    if type(nums) == str:
        raise TypeError("You inserted string, list of ints expected")
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j