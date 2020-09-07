# Write a function is_even that will return true if the passed-in number is even.
def is_even(x):
    even = input("Will it be even?:")
    x = even
    if int(x) % 2 == 0:
        return True
    else:
        return False
is_even(4)
    
# YOUR CODE HERE

# Read a number from the keyboard
##num = input("Enter a number: ")
##num = int(num)
##print(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def num_is_even(input):
    if int(input % 2 == 0):
        print("Even!")
    else:
        print('Odd')
    return num_is_even(2)
# YOUR CODE HERE






##
