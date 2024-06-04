""""

Given an interger array `nums`, return `True` if any value appears more than once in the array, 
otherwise return `False`.


"""



# Time complexity = O(n)
# Space complexity = O(n)



def contains_duplicate(nums):

    unique_number = set()

    for n in nums:
        if n in unique_number:
            return True
        else:
            unique_number.add(n)


    return False








nums = [1, 2, 3, 3] # True
nums = [1, 2, 3, 4] # False



print(contains_duplicate(nums))




