## Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT)

- Basic Terminology: 
  - Data: A collection of facts or values that can be processed by a computer.
  - Data Structure: A way of organizing and storing data in a computer memory or disk, such that it can be accessed and modified efficiently.
  - Data Type: A classification of data that specifies the possible values, operations and representation of the data.
  - Primitive Data Type: A data type that is predefined by the programming language and has a fixed size and range of values. Examples are int, char, float, double, etc.
  - Derived Data Type: A data type that is derived from one or more primitive data types or other derived data types. Examples are array, pointer, structure, union, etc.
  - User-defined Data Type: A data type that is defined by the user using the features of the programming language. Examples are enum, typedef, class, etc.

- Elementary Data Organization: 
  - Linear Data Structure: A data structure in which the data elements are arranged in a linear or sequential order. Examples are array, linked list, stack, queue, etc.
  - Non-linear Data Structure: A data structure in which the data elements are not arranged in a linear or sequential order. Examples are tree, graph, heap, etc.
  - Static Data Structure: A data structure that has a fixed size and cannot be resized during the execution of the program. Examples are array, structure, etc.
  - Dynamic Data Structure: A data structure that can grow or shrink in size during the execution of the program. Examples are linked list, tree, graph, etc.

- Built in Data Types in C: 
  - int: A data type that represents an integer value. It can be signed or unsigned, and can have different sizes depending on the compiler and platform. The range of values for int is usually -2^31 to 2^31-1 for signed int, and 0 to 2^32-1 for unsigned int.
  - char: A data type that represents a single character. It can be signed or unsigned, and has a size of 1 byte. The range of values for char is usually -128 to 127 for signed char, and 0 to 255 for unsigned char.
  - float: A data type that represents a floating-point value. It has a size of 4 bytes, and can store decimal numbers with a precision of about 6 digits. The range of values for float is usually -3.4E38 to 3.4E38.
  - double: A data type that represents a double-precision floating-point value. It has a size of 8 bytes, and can store decimal numbers with a precision of about 15 digits. The range of values for double is usually -1.7E308 to 1.7E308.

- Algorithm: A finite set of well-defined and unambiguous steps or instructions that can be followed to solve a problem or perform a task.
  - Example: An algorithm to find the maximum element in an array of n elements.
    - Step 1: Initialize a variable max to the first element of the array.
    - Step 2: Loop through the array from the second element to the last element.
    - Step 3: For each element, compare it with max. If the element is greater than max, update max to the element.
    - Step 4: Return max as the output.

- Efficiency of an Algorithm: A measure of how well an algorithm performs in terms of time and space resources required to execute it.
  - Time Complexity: The amount of time required by an algorithm to complete its execution for a given input size. It is usually expressed as a function of the input size, denoted by n.
  - Space Complexity: The amount of memory or space required by an algorithm to store the data and variables during its execution for a given input size. It is also usually expressed as a function of the input size, denoted by n.
  - Example: The time and space complexity of the algorithm to find the maximum element in an array of n elements are:
    - Time Complexity: O(n), because the algorithm loops through the array once, and performs a constant number of operations for each element.
    - Space Complexity: O(1), because the algorithm only uses a fixed amount of space to store the variable max, regardless of the input size.

- Asymptotic notations: Big