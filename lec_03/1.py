def two_terms_with_sum_x(nums, x):
    for i in range(len(nums - 1)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return nums[i], nums[j]
    return 0, 0
# O(n^2)
#             