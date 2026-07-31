# Pseudo Codes for the notes of the Unit 3 - Software Design in the subject of Software Engineering

- Pseudo code is a term which is often used in programming and algorithm based fields. It is a methodology that allows the programmer to represent the implementation of an algorithm. Simply, we can say that it’s the cooked up representation of an algorithm.
- Pseudo code is a description of an algorithm using everyday wording, but molded to appear similar to a simplified programming language. It is not a formal language, but rather a set of conventions and guidelines that can vary depending on the context and audience.
- Pseudo code can be used to communicate the main logic of an algorithm or a program without worrying about the syntax, data types, or implementation details of a specific programming language. It can also be used to test the correctness and efficiency of an algorithm before coding it.
- Pseudo code can be written in different styles and levels of abstraction, depending on the purpose and complexity of the algorithm or program. Some common features of pseudo code are:
  - Use of indentation and white space to show the structure and hierarchy of the code.
  - Use of keywords and symbols to indicate the control flow, such as IF, THEN, ELSE, WHILE, FOR, etc.
  - Use of comments to explain the purpose and functionality of the code.
  - Use of variables and constants to store and manipulate data.
  - Use of functions or procedures to modularize and reuse the code.
  - Use of input and output statements to interact with the user or other systems.
- Pseudo code examples: Here are some examples of pseudo code for some common algorithms and problems in software engineering. Note that these are not the only possible ways to write pseudo code, and different situations may require different styles and conventions.

  - Binary search: Binary search is a searching algorithm that works only for sorted search space. It repeatedly divides the search space into half by using the fact that the search space is sorted and checking if the desired search result will be found in the left or right half.

  ```
  // Pseudo code for binary search
  // Assume that the array A is sorted in ascending order and has n elements
  // Assume that the target value is x
  // Return the index of x in A, or -1 if x is not found

  Function BinarySearch(A, x)
    // Initialize the lower and upper bounds of the search space
    low = 0
    high = n - 1
    // Repeat until the search space is exhausted or the target is found
    While low <= high
      // Find the middle element of the search space
      mid = (low + high) / 2
      // Compare the middle element with the target
      If A[mid] == x
        // Target found, return the index
        Return mid
      Else If A[mid] < x
        // Target is in the right half, update the lower bound
        low = mid + 1
      Else
        // Target is in the left half, update the upper bound
        high = mid - 1
    // Target not found, return -1
    Return -1
  ```

  - Seven-segment display counter: A seven-segment display is a device that can display digits from 0 to 9 using seven LED segments. Each segment can be turned on or off by a binary value. The following table shows the binary values for each digit.

  | Digit | A | B | C | D | E | F | G |
  | ----- | - | - | - | - | - | - | - |
  | 0     | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
  | 1     | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
  | 2     | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
  | 3     | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
  | 4     | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
  | 5     | 1 | 0 | 1 | 1 | 0 | 1 | 1 |
  | 6     | 1 | 0 | 1 | 1 | 1 | 1 |