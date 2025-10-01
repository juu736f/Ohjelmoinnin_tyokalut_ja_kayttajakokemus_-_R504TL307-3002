# Exercise 2: Indentation Error
# Task: Fix the indentation error in this code
# The program should print numbers from 1 to 5

def print_numbers():
    for i in range(1, 6): # This line has wrong indentation!
        print(f"Number: {i}") # This line has wrong indentation!

print_numbers()

# Expected output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5