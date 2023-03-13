## 7. WAP to find the greatest of three numbers.

- To write a program to find the greatest of three numbers, we need to compare the three numbers and return the one that is largest.
- One way to compare the numbers is to use the `if-else` statement, which executes a block of code if a condition is true, or another block of code if the condition is false.
- For example, we can write the following pseudocode to find the greatest of three numbers:

```
// Declare three variables to store the numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

// Compare the numbers and print the largest one
if num1 > num2 and num1 > num3 then
  print("The greatest number is " + num1)
else if num2 > num1 and num2 > num3 then
  print("The greatest number is " + num2)
else
  print("The greatest number is " + num3)
end if
```

- Another way to compare the numbers is to use the `max` function, which returns the largest value from a set of values.
- For example, we can write the following pseudocode to find the greatest of three numbers using the `max` function:

```
// Declare three variables to store the numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

// Use the max function to find the largest number
greatest = max(num1, num2, num3)

// Print the result
print("The greatest number is " + greatest)
```

- Both methods will produce the same output, but the `max` function is more concise and easier to use.
- A possible mnemonic to remember the `max` function is to think of the word "maximum", which means the highest or most extreme degree of something. The `max` function returns the maximum value from a set of values.