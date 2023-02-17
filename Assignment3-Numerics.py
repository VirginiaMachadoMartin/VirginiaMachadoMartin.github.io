# Convert base 10 number from user input to other bases

#Ask user for input
i = int(input("Please enter a number to convert: "))

# Convert to binary
b = bin(i)
print("Here is your number in binary: " + str(b))

# Convert to oct
o = oct(i)
print("Here is your number in base 8: " + str(o))

# Convert to hex
h = hex(i)
print("Here is your number in base 16 " + str(h))

print("Thank you for participating. If you're unsure of what these outputs mean, google it! :) ")