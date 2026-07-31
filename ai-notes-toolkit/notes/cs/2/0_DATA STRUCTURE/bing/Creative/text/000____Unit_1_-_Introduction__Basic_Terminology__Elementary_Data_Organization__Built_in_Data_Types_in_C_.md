## Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT)

- Basic Terminology
  - Data: A collection of facts or values that can be processed by a computer.
  - Data Structure: A way of organizing and storing data in a computer memory or disk, such that it can be accessed and modified efficiently.
  - Data Type: A classification of data that defines the possible values, operations and representation of data.
  - Primitive Data Type: A data type that is predefined by the programming language and has a fixed size and range of values. Examples: int, char, float, double, etc.
  - Derived Data Type: A data type that is derived from one or more primitive data types or other derived data types. Examples: array, pointer, structure, union, etc.
  - User-defined Data Type: A data type that is defined by the user using the features of the programming language. Examples: enum, typedef, etc.

- Elementary Data Organization
  - Linear Data Organization: A way of organizing data such that each element has a unique successor and predecessor, except the first and last element. Examples: array, linked list, stack, queue, etc.
  - Non-linear Data Organization: A way of organizing data such that each element can have more than one successor or predecessor. Examples: tree, graph, etc.

- Built in Data Types in C
  - int: A data type that represents an integer value. It can be signed (positive or negative) or unsigned (positive only). The size and range of int depends on the compiler and the system architecture. Typically, it is 2 or 4 bytes long and can store values from -32768 to 32767 or -2147483648 to 2147483647.
  - char: A data type that represents a single character. It can be signed or unsigned. The size of char is 1 byte and it can store values from -128 to 127 or 0 to 255, depending on the character set used. It can also be used to store small integers.
  - float: A data type that represents a floating-point value. It can store real numbers with a decimal point and an exponent. The size of float is 4 bytes and it can store values from 1.2E-38 to 3.4E+38 with a precision of 6 digits.
  - double: A data type that represents a double-precision floating-point value. It can store real numbers with a higher precision and range than float. The size of double is 8 bytes and it can store values from 2.3E-308 to 1.7E+308 with a precision of 15 digits.

- Algorithm
  - An algorithm is a finite set of instructions or steps that defines a procedure to solve a problem or perform a task.
  - An algorithm should have the following characteristics:
    - Input: An algorithm should have zero or more inputs that are the data or values to be processed.
    - Output: An algorithm should have one or more outputs that are the results or values produced by the algorithm.
    - Definiteness: An algorithm should have clear and unambiguous instructions that can be executed in a finite amount of time.
    - Finiteness: An algorithm should have a finite number of instructions and should terminate after a finite number of steps.
    - Effectiveness: An algorithm should have instructions that are simple and feasible to execute by a computer or a human.

- Efficiency of an Algorithm
  - The efficiency of an algorithm is a measure of how well it performs in terms of time and space resources required to solve a problem or perform a task.
  - The time efficiency of an algorithm is the amount of time it takes to execute the algorithm for a given input size. It depends on the number and complexity of the instructions, the speed of the processor, the input data, etc.
  - The space efficiency of an algorithm is the amount of memory or storage space it requires to execute the algorithm for a given input size. It depends on the size and type of the data, the number and size of the variables, the data structures used, etc.

- Time and Space Complexity
  - The time complexity of an algorithm is a function that expresses the relationship between the input size and the time required to execute the algorithm. It is usually denoted by T(n), where n is the input size.
  - The space complexity of an algorithm is a function that expresses the relationship between the input size and the space required to