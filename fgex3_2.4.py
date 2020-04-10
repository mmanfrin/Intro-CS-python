# finger Exercise 3 (2.4)

# Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.

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
        return 'None of the numbers entered are odd.'
    
    return 'The largest odd number is: ' + str(greater)

numbers = int(input('How many number do you wish to enter: '))

lista = []

for i in range(numbers):
    entry = int(input(f'Enter a integer({i+1}): '))
    lista.append(entry)

# print(lista)

print(finger(lista))