"""

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j`
such that nums[i] + nums[j] == target and i != j

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

"""


# Time complexity = O(n)
# Space complexity = O(n)



def two_integer_sum(nums, target):


    sum = dict()
    
    for n in range(len(nums)):
        temp = target - nums[n]
        if temp in sum:
            first = sum.get(temp)
            second = n
            return [first, second]
        else:
            sum[nums[n]] = n



nums = [3, 4, 5, 6]
target = 7

print(two_integer_sum(nums, target)) # [0, 1]


nums = [4, 5, 6]
target = 10

print(two_integer_sum(nums, target)) # [0, 2]



nums = [5, 5]
target = 10

print(two_integer_sum(nums, target)) # [0, 1]