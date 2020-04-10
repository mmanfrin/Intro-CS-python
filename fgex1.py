# finger Exercise 1 (2.2)

# Write a program that examines three variables - X, Y, Z and prints the largest odd number among them.
# If none of them are odd, it should print a message to that effect.

def finger(numbers):
    """Print the largest odd number
    
    Arguments:
        numbers {list} -- list of integers
    """
    
    greater = 0 #storing largest number
    
    for i in numbers:
        if i%2 != 0 and i > greater: #check if odd and if larger than greater
            greater = i
    
    if greater == 0: # True if none are odd, greater var not changed
        return 'None of the numbers are odd.'
    
    return 'The largest odd number is: ' + str(greater)

lista1 = [1, 3, 5, 4, 9, 7]
lista2 = [0, 2, 6, 4]
lista3 = [100, 350, 437, 1939, 2, 4]

print(finger(lista1))
print(finger(lista2))
print(finger(lista3))