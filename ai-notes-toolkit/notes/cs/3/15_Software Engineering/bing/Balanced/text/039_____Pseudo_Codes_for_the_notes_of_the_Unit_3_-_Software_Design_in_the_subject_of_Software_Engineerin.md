### Pseudo Codes for the notes of the Unit 3 - Software Design in the subject of Software Engineering

- Pseudo code is a term which is often used in programming and algorithm based fields. It is a methodology that allows the programmer to represent the implementation of an algorithm.
- Pseudo code is a description of an algorithm using everyday wording, but molded to appear similar to a simplified programming language.
- Pseudo code can be used to illustrate different types of programming paradigms, such as imperative, functional, stack-based, etc.
- Pseudo code is not a standard or a formal language, and there is no fixed syntax or rules for writing it. However, some common conventions and guidelines are:
  - Use indentation to show the structure and hierarchy of the code.
  - Use keywords such as IF, THEN, ELSE, FOR, WHILE, REPEAT, UNTIL, etc to indicate the control flow statements.
  - Use comments to explain the logic and purpose of the code.
  - Use meaningful names for variables, functions, and parameters.
  - Use mathematical operators and symbols to represent arithmetic and logical operations.
  - Use parentheses, brackets, and braces to group expressions and statements.
  - Use pseudocode to describe the main steps of the algorithm, and avoid unnecessary details and low-level implementation details.
- Pseudo code examples:
  - Binary search pseudo code: Binary search is a searching algorithm that works only for sorted search space. It repeatedly divides the search space into half by using the fact that the search space is sorted and checking if the desired search result will be found in the left or right half.

  ```
  // Binary search pseudo code
  // Input: A sorted array A, a target value x
  // Output: The index of x in A, or -1 if not found
  // Assume the array is indexed from 0 to n-1

  Function BinarySearch(A, x)
    // Initialize the left and right pointers
    left = 0
    right = n-1
    // Repeat until the search space is exhausted
    While left <= right
      // Find the middle element
      mid = (left + right) / 2
      // Compare x with the middle element
      If x == A[mid]
        // x is found, return the index
        Return mid
      Else If x < A[mid]
        // x is in the left half, update the right pointer
        right = mid - 1
      Else
        // x is in the right half, update the left pointer
        left = mid + 1
    // x is not found, return -1
    Return -1
  ```
  - Seven-segment display counter pseudo code: A seven-segment display is a device that can display digits from 0 to 9 using seven LED segments. A counter is a device that can increment or decrement a value and display it on the seven-segment display.

  ```
  // Seven-segment display counter pseudo code
  // Input: A starting value n, a direction d (either + or -)
  // Output: The value n displayed on the seven-segment display, and updated according to the direction d
  // Assume the functions SegConvert() and Delay() are defined elsewhere

  Function Counter(n, d)
    // Initialize the value to n
    value = n
    // Repeat indefinitely
    While true
      // Convert the value to the binary representation for the seven-segment display
      B = SegConvert(value)
      // Display the binary representation on the seven-segment display
      Display(B)
      // Wait for some time
      Delay()
      // Update the value according to the direction
      If d == +
        // Increment the value, wrap around if it exceeds 9
        value = (value + 1) mod 10
      Else
        // Decrement the value, wrap around if it falls below 0
        value = (value - 1) mod 10
  ```