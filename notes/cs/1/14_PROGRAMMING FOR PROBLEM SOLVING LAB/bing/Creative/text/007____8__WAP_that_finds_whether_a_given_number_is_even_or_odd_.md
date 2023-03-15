## 8. WAP that finds whether a given number is even or odd.

- A number is even if it is divisible by 2 without any remainder.
- A number is odd if it is not divisible by 2 or has a remainder of 1 when divided by 2.
- To find whether a given number is even or odd, we can use the modulo operator (%) which returns the remainder of a division operation.
- The modulo operator (%) can be used as follows: `number % 2`
- If the result of `number % 2` is 0, then the number is even.
- If the result of `number % 2` is 1, then the number is odd.
- Here is a pseudocode for the program that finds whether a given number is even or odd:

```
// Input a number from the user and store it in a variable called number
number = input("Enter a number: ")

// Use the modulo operator (%) to find the remainder of number divided by 2 and store it in a variable called remainder
remainder = number % 2

// If the remainder is 0, then the number is even
if remainder == 0:
  // Print "The number is even" to the output
  print("The number is even")
// Else, the number is odd
else:
  // Print "The number is odd" to the output
  print("The number is odd")
```