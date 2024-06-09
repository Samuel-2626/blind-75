"""

Given two strings `s` and `t`, return `True` if the two strings are anagrams of each other, 
otherwise return `False`.

An anagram is a string that contains the exact same characters as another string, but the order
of the character can be different.

"""

# Time complexity = O(n)
# Space complexity = O(n)


def is_anagram(s, t):


    string_1 = dict()
    string_2 = dict()
    
    for char in s:
        if char not in string_1:
            string_1[char] = 1
        else:
            temp = string_1.get(char)
            temp += 1
            string_1.update({char: temp})

    
    #print(string_1)


    for char in t:
        if char not in string_2:
            string_2[char] = 1
        else:
            temp = string_2.get(char)
            temp += 1
            string_2.update({char: temp})


    #print(string_2)


    for char in string_1:
        temp_1 = string_1.get(char)
        temp_2 = string_2.get(char)
        
        if temp_1 != temp_2:
            return False
        

    return True





print(is_anagram("racecar", "carrace"))
print(is_anagram("jar", "jam"))