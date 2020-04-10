# finger Exercise 4 (3.1)

# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.
# If no such pair of integers exists, it should print a message to that effect.

integer = int(input("Please enter an integer greater than 1: "))
isFound = False
if integer < 0:
    isNeg = True
for pwr in range(2, 6):
    for root in range(2, abs(integer)+1):
        if root**pwr >= abs(integer):
            break
    #Now we'll compare root**power with integer if the power is even
    #or root**power with abs(integer) if power is ood and later replace the sign of root
    if root**pwr == integer or (root**pwr == abs(integer) and pwr%2 != 0):
        isFound = True
        break
if isFound == False:
    print("No root/pwr pair exists for this intger between the given range.")
else:
    if integer < 0:
        root = -root
    print(str(root) + "**" + str(pwr) + " = " + str(integer))