def a_func(nums: list, target: int):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


sample_list = [2, 7, 11, 15]
print(a_func(sample_list, target=26))
