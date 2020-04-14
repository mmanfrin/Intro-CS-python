# finger Exercise 6 (4.1.1)

# Write a function isIn that accepts two strings as arguments and return True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operation in.

def isIn(str1, str2):
    """Check if str is in other
    
    Arguments:
        str1 {str} -- string 1
        str2 {str} -- string 2
    
    Returns:
        boolean -- True if is in
    """
    
    if str1 in str2 or str2 in str1:
        return True
    
    return False

str1 = 'bbababbabbbbbaaabbab'
str2 = 'abba'

print(isIn(str1, str2))