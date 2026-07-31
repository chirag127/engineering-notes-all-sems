## 20.WAP to convert binary number into decimal number and vice versa.

Binary numbers are composed of only 0s and 1s, and each digit represents a power of 2. Decimal numbers are composed of digits from 0 to 9, and each digit represents a power of 10. To convert a binary number into a decimal number, we need to multiply each digit by its corresponding power of 2 and add them up. To convert a decimal number into a binary number, we need to divide the number by 2 repeatedly and record the remainders as the digits of the binary number.

Here is a pseudocode for converting a binary number into a decimal number:

```
# Input: a binary number as a string
# Output: a decimal number as an integer

# Initialize a variable to store the decimal number
decimal = 0

# Loop through the binary number from right to left
for i from length of binary - 1 to 0:

  # Get the current digit as an integer
  digit = binary[i] as integer

  # Calculate the power of 2 corresponding to the position of the digit
  power = length of binary - 1 - i

  # Multiply the digit by the power of 2 and add it to the decimal number
  decimal = decimal + digit * 2^power

# Return the decimal number
return decimal
```

Here is a pseudocode for converting a decimal number into a binary number:

```
# Input: a decimal number as an integer
# Output: a binary number as a string

# Initialize a variable to store the binary number
binary = ""

# Loop while the decimal number is positive
while decimal > 0:

  # Divide the decimal number by 2 and get the remainder
  remainder = decimal mod 2

  # Convert the remainder to a string and prepend it to the binary number
  binary = remainder as string + binary

  # Divide the decimal number by 2 and update it
  decimal = decimal / 2

# Return the binary number
return binary
```