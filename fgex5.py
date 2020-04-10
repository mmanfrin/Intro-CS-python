# finger Exercise 5 (3.2)

# Let s be a string that contains s sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'.
# Write a program that prints the sum of the numbers in s.

def finger(s):
    """Sum of string itens
    
    Arguments:
        numbers {string} -- string of integers sepparated by commas
    """
    
    add = 0 #storing sum
    splitted = s.split(',') #split the string by commas
    for i in splitted:
        print(i)
        add += float(i) #sum
    
    return f'Sum of itens: {add}'

s = '1.23,2.4,3.123'

print(finger(s))