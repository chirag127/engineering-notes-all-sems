## 8. WAP that finds whether a given number is even or odd.

- A number is even if it is divisible by 2 without any remainder.
- A number is odd if it is not divisible by 2 or has a remainder of 1 when divided by 2.
- To find whether a given number is even or odd, we can use the modulo operator (%) which returns the remainder of a division operation.
- The modulo operator (%) can be used as follows: `number % divisor`
- If the remainder is 0, then the number is divisible by the divisor. If the remainder is not 0, then the number is not divisible by the divisor.
- To check if a number is even or odd, we can use the modulo operator (%) with 2 as the divisor.
- If the remainder is 0, then the number is even. If the remainder is 1, then the number is odd.
- Here is a pseudocode for a program that finds whether a given number is even or odd:

```
// Read a number from the user
input number

// Check if the number is even or odd using the modulo operator (%)
if number % 2 == 0
  // If the remainder is 0, then the number is even
  print "The number is even."
else
  // If the remainder is not 0, then the number is odd
  print "The number is odd."
end if
```