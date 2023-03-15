### Pseudo Codes for the notes of the Unit 3 - Software Design in the subject of Software Engineering

- Pseudocode is a step-by-step description of an algorithm or a system using simple English language text.
- Pseudocode does not use any specific programming language syntax or keywords, but rather follows some general conventions and structures .
- Pseudocode is intended for human reading and understanding, not for machine execution.
- Pseudocode can help programmers to plan and organize their coding logic, test their algorithms, and communicate their ideas to others.
- Pseudocode can also be used to document the design and functionality of a software system.

Some common components and pros of pseudocode are:

- **Variables**: Pseudocode can use variables to store and manipulate data. Variables can have descriptive names and can be of any data type, such as numbers, strings, booleans, arrays, etc.
- **Operators**: Pseudocode can use operators to perform arithmetic, logical, and relational operations on variables and values. Operators can be symbols or words, such as +, -, *, /, AND, OR, NOT, <, >, =, etc.
- **Input and Output**: Pseudocode can use input and output statements to interact with the user or other systems. Input statements can use keywords such as READ, GET, INPUT, etc. Output statements can use keywords such as WRITE, PRINT, DISPLAY, etc.
- **Selection**: Pseudocode can use selection statements to control the flow of execution based on some conditions. Selection statements can use keywords such as IF, THEN, ELSE, ELSEIF, ENDIF, CASE, SWITCH, etc.
- **Iteration**: Pseudocode can use iteration statements to repeat a block of code for a certain number of times or until a condition is met. Iteration statements can use keywords such as FOR, TO, BY, WHILE, DO, UNTIL, REPEAT, etc.
- **Functions**: Pseudocode can use functions to modularize and reuse code. Functions can have names, parameters, and return values. Functions can use keywords such as FUNCTION, PROCEDURE, SUBROUTINE, RETURN, CALL, etc .
- **Comments**: Pseudocode can use comments to explain the purpose and logic of the code. Comments can use symbols or keywords such as //, #, REMARK, etc.

Some pros of pseudocode are:

- It is easy to write and read, as it uses natural language and simple syntax.
- It is independent of any programming language, so it can be translated into any language of choice.
- It can help to identify and fix errors and bugs before writing the actual code.
- It can facilitate communication and collaboration among programmers, designers, and stakeholders .

Here are some examples of pseudocode for some common algorithms and problems:

- Binary search: This algorithm searches for a target value in a sorted array by repeatedly dividing the array into two halves and checking if the target is in the left or right half.

```
FUNCTION binary_search(array, target)
  // initialize the left and right pointers
  left = 0
  right = length of array - 1
  // loop until the pointers cross or the target is found
  WHILE left <= right
    // calculate the middle index
    mid = (left + right) / 2
    // check if the target is at the middle
    IF array[mid] = target
      // return the index of the target
      RETURN mid
    ELSE IF array[mid] < target
      // move the left pointer to the right of the middle
      left = mid + 1
    ELSE
      // move the right pointer to the left of the middle
      right = mid - 1
    ENDIF
  ENDWHILE
  // return -1 if the target is not found
  RETURN -1
ENDFUNCTION
```

- Factorial: This function calculates the factorial of a positive integer n, which is the product of all integers from 1 to n.

```
FUNCTION factorial(n)
  // check if n is valid
  IF n < 0
    // print an error message
    PRINT "Invalid input"
    // return 0
    RETURN 0
  ELSE IF n = 0 OR n =