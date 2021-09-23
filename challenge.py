def tuple_added(nums, target):
    if type(nums) != list:
        raise TypeError("You are expected to insert a list")
    else:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                # if (type(i) == type(j)) and type(i) != type(target):
                #     raise TypeError("mismatched input and output types")
                # else:
                    if nums[i] + nums[j] == target:
                        return i, j


print(tuple_added([1, 2, 4, 6], target="sui"))
