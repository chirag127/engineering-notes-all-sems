## 13. WAP to find the factorial of a given number.

- The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.
- The factorial of zero, 0!, is defined as 1 by convention.
- The factorial function can be implemented using a loop or recursion in most programming languages.
- Here is a pseudocode for finding the factorial of a given number n using a loop:

```
factorial = 1
for i from 1 to n
  factorial = factorial * i
end for
return factorial
```

- Here is a pseudocode for finding the factorial of a given number n using recursion:

```
function factorial(n)
  if n == 0 or n == 1
    return 1
  else
    return n * factorial(n-1)
  end if
end function
```

- The time complexity of both the loop and recursion methods is O(n), where n is the input number.
- The space complexity of the loop method is O(1), as it uses a constant amount of memory.
- The space complexity of the recursion method is O(n), as it uses a stack to store the recursive calls.