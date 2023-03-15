### Pseudo Codes for the notes of the Unit 3 - Software Design in the subject of Software Engineering

- Pseudo code is a term which is often used in programming and algorithm based fields. It is a methodology that allows the programmer to represent the implementation of an algorithm. Simply, we can say that it’s the cooked up representation of an algorithm.
- Pseudo code is a description of an algorithm using everyday wording, but molded to appear similar to a simplified programming language. It is not a formal language, but rather a set of conventions and guidelines that can vary depending on the context and audience.
- Pseudo code can be used to communicate the main logic of an algorithm or a program without worrying about the syntax, data types, or implementation details of a specific programming language. It can also be used to test the correctness and efficiency of an algorithm before coding it.
- Pseudo code can be written in different styles and levels of abstraction, depending on the purpose and complexity of the algorithm. Some general rules for writing pseudo code are:
  - Use consistent indentation and spacing to show the structure and hierarchy of the algorithm.
  - Use keywords and symbols that are easy to understand and follow, such as IF, THEN, ELSE, WHILE, FOR, etc.
  - Use comments to explain the purpose and logic of each step or block of pseudo code.
  - Use meaningful names for variables, functions, and parameters that describe their roles and values.
  - Use capital letters for constants and literals, such as TRUE, FALSE, PI, etc.
  - Use parentheses, brackets, braces, or other symbols to enclose expressions, arrays, lists, etc.
  - Use pseudocode to describe the main steps of the algorithm, and call functions or subroutines for more detailed or repetitive tasks.
  - Use pseudocode to describe the input and output of the algorithm, and the preconditions and postconditions if applicable.
- Pseudo code examples: 
  - Binary search pseudo code: Binary search is a searching algorithm that works only for sorted search space. It repeatedly divides the search space into half by using the fact that the search space is sorted and checking if the desired search result will be found in the left or right half.

  ```
  // Binary search pseudo code
  // Input: A sorted array A of n elements, and a target value x
  // Output: The index of x in A, or -1 if x is not in A
  // Precondition: A is sorted in ascending order
  // Postcondition: If x is in A, then A[index] = x, where index is the output

  Function BinarySearch(A, x)
    // Initialize the lower and upper bounds of the search space
    low = 0
    high = n - 1
    // Repeat until the search space is exhausted or x is found
    While low <= high
      // Find the middle element of the search space
      mid = (low + high) / 2
      // Compare x with the middle element
      If x == A[mid]
        // x is found, return the index
        Return mid
      Else If x < A[mid]
        // x is in the left half, update the upper bound
        high = mid - 1
      Else
        // x is in the right half, update the lower bound
        low = mid + 1
    // x is not in A, return -1
    Return -1
  ```
  - Seven-segment display counter pseudo code: A seven-segment display is a device that can display decimal digits using seven LED segments. Each segment can be turned on or off by a binary value. A counter is a device that can increment or decrement a value by a certain amount. A seven-segment display counter is a device that can display the value of a counter using a seven-segment display.

  ```
  // Seven-segment display counter pseudo code
  // Input: A counter value C, and a delay time D
  // Output: The counter value displayed on a seven-segment display
  // Precondition: C is a non-negative integer, and D is a positive integer
  // Postcondition: The seven-segment display shows the value of C

  Function DisplayCounter(C, D)
    // Convert the counter value to a binary value
    B = BinConvert(C)
    // Convert the binary value to a seven-segment display value
    S = SegConvert(B)
    // Display the seven-segment display