def tuple_added(nums, target):
    if type(nums) != list:
        raise TypeError("You are expected to insert a list")
    else:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


print(tuple_added(2.4, target="sui"))
