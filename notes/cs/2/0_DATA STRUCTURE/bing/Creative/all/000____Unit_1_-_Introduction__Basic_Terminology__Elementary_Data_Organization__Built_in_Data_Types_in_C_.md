# Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT)

- Basic Terminology
  - Data: A collection of facts or values that can be processed by a computer.
  - Data Structure: A way of organizing and storing data in a computer memory or disk, such that it can be accessed and modified efficiently.
  - Data Type: A classification of data that defines the possible values, operations and representations of the data.
  - Primitive Data Type: A data type that is predefined by the programming language and has a fixed size and range of values. Examples are int, char, float, double, etc.
  - Derived Data Type: A data type that is derived from one or more primitive data types or other derived data types. Examples are array, pointer, structure, union, etc.
  - User-defined Data Type: A data type that is defined by the user using the features of the programming language. Examples are enum, typedef, class, etc.

- Elementary Data Organization
  - Linear Data Organization: A way of organizing data such that each element has a unique successor and predecessor, except the first and last element. Examples are array, linked list, stack, queue, etc.
  - Non-linear Data Organization: A way of organizing data such that each element can have more than one successor or predecessor. Examples are tree, graph, etc.
  - Sequential Data Organization: A way of organizing data such that the elements are stored in a contiguous memory location and can be accessed by their position or index. Examples are array, string, etc.
  - Non-sequential Data Organization: A way of organizing data such that the elements are stored in a non-contiguous memory location and can be accessed by their logical relationship or pointer. Examples are linked list, tree, graph, etc.

- Built in Data Types in C
  - int: A data type that represents an integer value. It can be signed or unsigned, and can have different sizes depending on the compiler and platform. The range of values is typically from -2^(n-1) to 2^(n-1)-1, where n is the number of bits allocated for the int type.
  - char: A data type that represents a character value. It can be signed or unsigned, and has a fixed size of 1 byte. The range of values is typically from -128 to 127 for signed char, and from 0 to 255 for unsigned char. It can also be used to store small integers.
  - float: A data type that represents a floating-point value. It has a fixed size of 4 bytes, and can store decimal numbers with a precision of about 6 digits. The range of values is typically from -3.4E38 to 3.4E38.
  - double: A data type that represents a double-precision floating-point value. It has a fixed size of 8 bytes, and can store decimal numbers with a precision of about 15 digits. The range of values is typically from -1.7E308 to 1.7E308.
  - void: A data type that represents no value. It is used to indicate that a function does not return any value, or that a pointer does not point to any valid memory location.

- Algorithm
  - An algorithm is a finite sequence of well-defined steps or instructions that can be executed by a computer to solve a problem or perform a task.
  - An algorithm has the following characteristics:
    - Input: An algorithm may take zero or more inputs from the user or another source.
    - Output: An algorithm may produce zero or more outputs as the result of the computation or action.
    - Definiteness: Each step of an algorithm must be clear and unambiguous, and must have a specific meaning.
    - Finiteness: An algorithm must terminate after a finite number of steps, and must not have any infinite loop or recursion.
    - Effectiveness: Each step of an algorithm must be feasible and executable by a computer, and must not involve any human intuition or creativity.

- Efficiency of an Algorithm
  - The efficiency of an algorithm is a measure of how well it performs in terms of time and space resources required to execute it.
  - The time efficiency of an algorithm is the amount of time taken by the algorithm to complete its execution for a given input size. It depends on the number and complexity of the operations performed by the algorithm, and the speed of the computer.
  - The space efficiency of an algorithm is the amount of memory or