## 17. WAP to find the sum of digits of the entered number.

To find the sum of digits of a number, you can write a program that performs the following steps:

1. Read the number from the user as input.

2. Convert the number to a string representation.

3. Initialize a variable to store the sum of the digits.

4. Loop through each character in the string representation of the number.

5. For each character, convert it to an integer and add it to the sum of the digits.

6. Repeat the process for all characters in the string representation of the number.

7. Print the sum of the digits.

Here is an example of a program in Python that implements these steps:

```
# Read the number from the user
number = int(input("Enter a number: "))

# Convert the number to a string representation
number_str = str(number)

# Initialize a variable to store the sum of the digits
sum_of_digits = 0

# Loop through each character in the string representation of the number
for digit in number_str:
    # Convert the character to an integer and add it to the sum of the digits
    sum_of_digits += int(digit)

# Print the sum of the digits
print("The sum of the digits is", sum_of_digits)
```

This program can be used to find the sum of digits of any number entered by the user. By breaking down the number into its individual digits and summing them, you can quickly and easily calculate the sum of the digits of a number.
