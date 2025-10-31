# ENSF 692 Spring 2025
# May 13 Lab 3
# Exercise 3 - Solutions

# Add comments to explain the functionality of this program

# Input Method 1
# This method allows the user to input their name, and then it displays the name as their first input.
print('\n')
print("***METHOD 1***")
input1 = input("Please enter your name: ")
print("This is the first input:", input1)


# Input Method 2
# This method allows the user to input x, as it will then display x. Otherwise it will ask again.
print('\n' * 2)
print("***METHOD 2***")
while True:
    input2 = input("I am looking for specific input. You must type x: ")
    if input2 == "x":
        break
print("This is the second input: " + input2)


# Rewrite Input Method 2 so that no break statement is necessary

print('\n' * 2)
print("***METHOD 2***")

input2 = ""

while input2 != 'x':
    input2 = input("I am looking for specific input. You must type x: ")
    if input2 == "x":
        print("Terminated")

print("This is the second input: " + input2)
