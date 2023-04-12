

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



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of basic terminology for data structure.

# Basic Terminology for Data Structure

## Data Structure
- A data structure is a specialized format for organizing and storing data in a computer program so that it can be accessed and used efficiently .
- Data structures provide a means of managing large amounts of data, enabling efficient searching, sorting, insertion, and deletion of data.
- Data structures are classified into two types: linear and non-linear.
  - Linear data structures arrange the data in sequential order, such as arrays, lists, stacks, queues, etc.
  - Non-linear data structures arrange the data in hierarchical or network order, such as trees, graphs, heaps, etc.

## Algorithm
- An algorithm is a finite set of instructions or logic, written in a specific order, to perform a specific task or to solve a problem.
- An algorithm can be expressed in various forms, such as pseudocode, flowchart, natural language, etc.
- An algorithm has the following characteristics:
  - Input: An algorithm must have zero or more inputs, which are the data or information to be processed by the algorithm.
  - Output: An algorithm must have one or more outputs, which are the results or outcomes of the algorithm.
  - Definiteness: An algorithm must have clear and unambiguous instructions, which can be executed in a finite amount of time.
  - Finiteness: An algorithm must have a finite number of steps, which means it must terminate after a certain point.
  - Effectiveness: An algorithm must be able to perform the required operations on the input data and produce the desired output.

## Efficiency of an Algorithm
- The efficiency of an algorithm is a measure of how well the algorithm performs in terms of time and space, or how fast and how much memory the algorithm uses to solve a problem.
- The efficiency of an algorithm depends on various factors, such as the size and nature of the input data, the hardware and software environment, the programming language, etc.
- The efficiency of an algorithm can be analyzed using two methods: empirical analysis and theoretical analysis.
  - Empirical analysis involves running the algorithm on a computer with different input data and measuring the actual time and space used by the algorithm.
  - Theoretical analysis involves using mathematical models and formulas to estimate the time and space complexity of the algorithm, without actually running the algorithm.

## Time and Space Complexity
- Time complexity is a measure of how much time an algorithm takes to execute as a function of the size of the input data.
- Space complexity is a measure of how much memory an algorithm uses to execute as a function of the size of the input data.
- Time and space complexity are usually expressed using the big O notation, which describes the upper bound or the worst-case scenario of the algorithm's performance.
- For example, an algorithm with a time complexity of O(n) means that the algorithm's running time increases linearly with the size of the input data, and an algorithm with a space complexity of O(1) means that the algorithm's memory usage is constant regardless of the size of the input data.

## Asymptotic Notations
- Asymptotic notations are mathematical tools that are used to describe the behavior of functions or algorithms as the input size approaches infinity.
- Asymptotic notations are useful for comparing the efficiency of different algorithms and ignoring the constant factors and lower-order terms that are insignificant for large input sizes.
- There are three common asymptotic notations: big O, big theta, and big omega.
  - Big O notation represents the upper bound or the worst-case scenario of a function or an algorithm. For example, O(n) means that the function or the algorithm grows at most linearly with the input size.
  - Big theta notation represents the tight bound or the average-case scenario of a function or an algorithm. For example, Θ(n) means that the function or the algorithm grows exactly linearly with the input size.
  - Big omega notation represents the lower bound or the best-case scenario of a function or an algorithm. For example, Ω(n) means that the function or the algorithm grows at least linearly with the input size.

## Time-Space Trade-off
- Time-space trade-off is a concept that describes the trade-off or the balance between the time and space complexity



# Elementary Data Organization

## Basic Terminology

- **Data**: Data refers to a value or a set of values that represent some information or facts. For example, the name, age, and height of a person are data.
- **Data item**: Data item refers to a single or a group of values within the data. For example, the name of a person is a data item.
- **Data type**: Data type refers to the category or classification of data items based on their values and operations that can be performed on them. For example, integer, float, char, and string are some data types in C.
- **Built-in data type**: Built-in data type refers to the data type that is predefined and supported by the programming language. For example, int, float, char, and double are some built-in data types in C.
- **Derived data type**: Derived data type refers to the data type that is defined by the programmer using the built-in data types and other data structures. For example, array, structure, union, and pointer are some derived data types in C.
- **Data structure**: Data structure refers to a specialized format for organizing and storing data. Data structure is designed to suit a specific purpose and to facilitate the access and manipulation of data. For example, array, file, record, table, tree, and graph are some data structures.
- **Abstract data type (ADT)**: Abstract data type refers to a logical or mathematical model for a particular organization of data and the operations that can be performed on it. ADT hides the implementation details of the data structure and provides an interface to the user. For example, stack, queue, list, and set are some ADTs.

## Elementary Data Organization

- **Elementary data organization** refers to the basic ways of organizing and storing data in memory. It includes the following concepts:
  - **Bit**: Bit is the smallest unit of data that can be stored in memory. It can have only two values: 0 or 1.
  - **Byte**: Byte is a group of 8 bits. It can store one character or a small integer value.
  - **Word**: Word is a group of bytes. The size of a word depends on the architecture of the computer. It can be 16 bits, 32 bits, or 64 bits. It can store a large integer value or a floating-point value.
  - **Address**: Address is a unique identifier for a location in memory. It is usually represented by a hexadecimal number. For example, 0x1234 is an address.
  - **Pointer**: Pointer is a variable that stores the address of another variable or data item. It can be used to access or modify the data item indirectly. For example, int *p = &x; is a pointer declaration in C, where p is a pointer to an integer variable x.
  - **Array**: Array is a derived data type that stores a collection of data items of the same type in a contiguous block of memory. Each data item can be accessed by its index or position in the array. For example, int a[10]; is an array declaration in C, where a is an array of 10 integers.
  - **Structure**: Structure is a derived data type that stores a collection of data items of different types in a single unit. Each data item can be accessed by its name or member. For example, struct student {char name[20]; int roll; float marks;}; is a structure declaration in C, where student is a structure that contains three data items: name, roll, and marks.
  - **Union**: Union is a derived data type that stores a collection of data items of different types in a single unit. However, only one data item can be stored at a time. The size of the union is equal to the size of the largest data item. For example, union data {int x; float y; char z;}; is a union declaration in C, where data is a union that can store either an integer, a float, or a character.



# Built in Data Types in C

- Built in data types (also called fundamental types) are specified by the C language standard and are built into the compiler.
- Built in data types are not defined in any header file.
- Built in data types determine the size and range of values that can be stored in a variable, as well as the operations that can be performed on it .
- The C language provides the four basic arithmetic type specifiers: `char`, `int`, `float` and `double`, and the modifiers `signed`, `unsigned`, `short`, and `long`.
- The following table summarizes some commonly used built in data types in C along with their description, size and range   .

| Data Type | Description | Size (in bytes) | Range |
| --- | --- | --- | --- |
| `char` | Character or small integer | 1 | -128 to 127 or 0 to 255 |
| `unsigned char` | Unsigned character or small integer | 1 | 0 to 255 |
| `signed char` | Signed character or small integer | 1 | -128 to 127 |
| `int` | Integer | 2 or 4 | -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647 |
| `unsigned int` | Unsigned integer | 2 or 4 | 0 to 65,535 or 0 to 4,294,967,295 |
| `short` | Short integer | 2 | -32,768 to 32,767 |
| `unsigned short` | Unsigned short integer | 2 | 0 to 65,535 |
| `long` | Long integer | 4 or 8 | -2,147,483,648 to 2,147,483,647 or -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| `unsigned long` | Unsigned long integer | 4 or 8 | 0 to 4,294,967,295 or 0 to 18,446,744,073,709,551,615 |
| `float` | Single precision floating point | 4 | +/- 3.4e +/- 38 (~7 digits) |
| `double` | Double precision floating point | 8 | +/- 1.7e +/- 308 (~15 digits) |
| `long double` | Extended precision floating point | 10 | +/- 3.4e +/- 4932 (~19 digits) |
| `void` | Valueless special purpose | - | - |

- The exact sizes and ranges of values for the built in data types are implementation dependent , meaning they may vary depending on the compiler and the system architecture.
- The `sizeof` operator can be used to determine the size of a data type or a variable in bytes .
- For example, `sizeof(int)` returns the size of an `int` data type, and `sizeof(x)` returns the size of the variable `x`.
- The `void` data type is a special type that has no value and is used to indicate an empty set of parameters or return type for a function   .
- For example, `void func(void)` is a function that takes no parameters and returns nothing.



# Algorithm for the notes of the Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT) in the subject of DATA STRUCTURE

- An algorithm is a finite sequence of well-defined steps that solves a problem or performs a task.
- An algorithm can be expressed in different ways, such as natural language, pseudocode, flowchart, or programming language.
- An algorithm has the following properties:
  - Input: An algorithm may take zero or more inputs.
  - Output: An algorithm must produce at least one output.
  - Definiteness: Each step of an algorithm must be clear and unambiguous.
  - Finiteness: An algorithm must terminate after a finite number of steps.
  - Effectiveness: Each step of an algorithm must be feasible and executable.
  - Correctness: An algorithm must produce the correct output for all valid inputs.
- The efficiency of an algorithm is a measure of how well it uses the resources, such as time and space, to solve a problem or perform a task.
- The time complexity of an algorithm is the amount of time it takes to execute as a function of the input size.
- The space complexity of an algorithm is the amount of memory it uses as a function of the input size.
- The asymptotic notation is a way of expressing the growth rate of a function, such as time or space complexity, as the input size approaches infinity.
- The most common asymptotic notations are:
  - Big Oh (O): It gives the upper bound of a function, meaning that the function is always less than or equal to a constant multiple of another function.
  - Big Theta (Θ): It gives the tight bound of a function, meaning that the function is always between a constant multiple of another function and another constant multiple of the same function.
  - Big Omega (Ω): It gives the lower bound of a function, meaning that the function is always greater than or equal to a constant multiple of another function.
- The time-space trade-off is a situation where an algorithm can be improved in terms of time complexity by using more space, or vice versa.
- An abstract data type (ADT) is a logical description of a set of data and the operations that can be performed on the data, without specifying how the data is stored or how the operations are implemented.
- An ADT can be implemented using different data structures, such as arrays, linked lists, stacks, queues, trees, graphs, etc.
- An ADT has the following advantages:
  - Abstraction: It hides the details of the data representation and implementation from the user, allowing the user to focus on the problem-solving logic.
  - Encapsulation: It protects the data from being manipulated or accessed in an unauthorized or incorrect way, ensuring data integrity and consistency.
  - Modularity: It allows the data and the operations to be organized into separate modules, making the code easier to understand, maintain, and reuse.



# Efficiency of an Algorithm

- The efficiency of an algorithm is a property of an algorithm that relates to the amount of computational resources used by the algorithm.
- The computational resources can be time, memory, disk space, bandwidth, etc.
- The efficiency of an algorithm can be measured by analyzing its resource usage for different input sizes.
- The efficiency of an algorithm can be affected by the choice of data structures, the implementation of the algorithm, and the hardware and software environment.
- The efficiency of an algorithm can be expressed using asymptotic notations, which are mathematical languages that use meaningful statements about the resource usage of an algorithm as the input size grows indefinitely .
- The most common asymptotic notations are Big O, Big Theta, and Big Omega, which represent the upper bound, the tight bound, and the lower bound of the resource usage of an algorithm, respectively.
- A space-time or time-memory tradeoff is a way of solving a problem in less time by using more storage space, or vice versa .
- A space-time tradeoff can be useful when one resource is more abundant or cheaper than the other, or when one resource is more critical or desirable than the other.
- An abstract data type (ADT) is a logical description of a set of data and the operations that can be performed on the data, without specifying how the data is stored or how the operations are implemented.
- An ADT defines the behavior and properties of the data, but not the details of the implementation.
- An ADT can be implemented using different data structures, such as arrays, linked lists, stacks, queues, trees, etc.
- An ADT can be used to design and analyze algorithms, as it provides a high-level and abstract view of the data and the operations.



# Time and Space Complexity

## Introduction

- Time and space complexity are two measures of the efficiency of an algorithm.
- Time complexity refers to the amount of time required by an algorithm to execute for a given input size.
- Space complexity refers to the amount of memory (or storage) required by an algorithm to execute for a given input size.
- Both time and space complexity depend on the input size, the algorithm design, and the implementation details.

## Basic Terminology

- Input size: The number of elements or the size of the data that the algorithm operates on. For example, the input size for sorting an array of n numbers is n, and the input size for searching a key in a binary tree of n nodes is n.
- Algorithm: A finite set of well-defined steps or instructions to solve a problem or perform a task. For example, the algorithm for sorting an array of numbers can be described as follows:

  - Step 1: Compare the first two elements of the array and swap them if they are out of order.
  - Step 2: Repeat step 1 for the next pair of elements until the end of the array is reached.
  - Step 3: Repeat steps 1 and 2 until no swaps are made in a pass through the array.

- Efficiency of an algorithm: The measure of how well an algorithm performs in terms of time and space. For example, the efficiency of the sorting algorithm above can be improved by using a different algorithm, such as merge sort or quick sort, that can sort the array in fewer comparisons and swaps.

## Time Complexity

- Time complexity is the measure of how long an algorithm takes to execute for a given input size. It is usually expressed as a function of the input size, denoted by n.
- For example, the time complexity of the sorting algorithm above can be expressed as T(n) = O(n^2), where T(n) is the time function and O(n^2) is the asymptotic notation for the upper bound of the time function.
- Asymptotic notation is a way of describing the growth rate of a function as the input size approaches infinity. It ignores the constant factors and lower-order terms that do not affect the long-term behavior of the function. There are three common asymptotic notations:

  - Big Oh notation: O(f(n)) represents the upper bound of a function, meaning that the function is always less than or equal to some constant multiple of f(n) for sufficiently large n. For example, O(n^2) means that the function is always less than or equal to c*n^2 for some constant c and for all n > n0, where n0 is some threshold value.
  - Big Theta notation: Θ(f(n)) represents the tight bound of a function, meaning that the function is always between some constant multiples of f(n) for sufficiently large n. For example, Θ(n^2) means that the function is always between c1*n^2 and c2*n^2 for some constants c1 and c2 and for all n > n0, where n0 is some threshold value.
  - Big Omega notation: Ω(f(n)) represents the lower bound of a function, meaning that the function is always greater than or equal to some constant multiple of f(n) for sufficiently large n. For example, Ω(n^2) means that the function is always greater than or equal to c*n^2 for some constant c and for all n > n0, where n0 is some threshold value.

- The asymptotic notation helps to compare the efficiency of different algorithms by focusing on the dominant term of the time function. For example, O(n^2) is more efficient than O(n^3), but less efficient than O(n) or O(log n).
- The time complexity of an algorithm can be analyzed by counting the number of basic operations or steps performed by the algorithm for a given input size. For example, the sorting algorithm above performs n-1 comparisons and swaps in the first pass, n-2 in the second pass, and so on, until 1 in the last pass. Therefore, the total number of comparisons and swaps is (n-1) + (n-2) + ... + 1 = n*(n-1)/2, which is O(n^2).

## Space Complexity

- Space complexity is the measure of how much memory (or storage) an algorithm requires to execute for a given input size. It is usually expressed as a function of the input size, denoted by n.
- For example, the space complexity of the sorting algorithm above can be expressed as S(n) = O(n), where S(n) is the space function and O(n) is the asymptotic notation



# Asymptotic notations: Big Oh, Big Theta and Big Omega

- Asymptotic notations are mathematical tools that help us to analyze the efficiency of an algorithm in terms of its time and space complexity.
- They allow us to compare the performance of different algorithms for the same problem, and to ignore the constant factors and lower-order terms that are insignificant for large inputs.
- There are three common asymptotic notations: Big Oh, Big Theta and Big Omega.

## Big Oh notation

- Big Oh notation, denoted by O(f(n)), represents the upper bound of the time or space complexity of an algorithm.
- It means that the algorithm will take at most O(f(n)) time or space to execute for any input of size n.
- For example, if an algorithm has a time complexity of O(n^2 + 3n + 5), it means that the algorithm will take at most n^2 + 3n + 5 steps to complete for any input of size n.
- To simplify the notation, we can drop the lower-order terms and the constant factors, and write the time complexity as O(n^2).
- This is because as n grows large, the n^2 term will dominate the other terms, and the constant factors will not affect the order of growth.
- Big Oh notation gives us an upper bound, but it does not guarantee that the algorithm will always take O(f(n)) time or space. It only means that the algorithm will never take more than O(f(n)) time or space.

## Big Theta notation

- Big Theta notation, denoted by Θ(f(n)), represents the tight bound of the time or space complexity of an algorithm.
- It means that the algorithm will take exactly Θ(f(n)) time or space to execute for any input of size n, within a constant factor.
- For example, if an algorithm has a time complexity of Θ(n^2), it means that the algorithm will take n^2 steps to complete for any input of size n, plus or minus some constant factor.
- Big Theta notation gives us a precise estimate of the algorithm's performance, but it is harder to find than Big Oh notation.
- To prove that an algorithm has a time or space complexity of Θ(f(n)), we need to show that there exist two positive constants c1 and c2 such that c1 * f(n) <= T(n) <= c2 * f(n) for all sufficiently large n, where T(n) is the actual time or space complexity of the algorithm.

## Big Omega notation

- Big Omega notation, denoted by Ω(f(n)), represents the lower bound of the time or space complexity of an algorithm.
- It means that the algorithm will take at least Ω(f(n)) time or space to execute for any input of size n.
- For example, if an algorithm has a time complexity of Ω(n^2), it means that the algorithm will take n^2 steps or more to complete for any input of size n.
- Big Omega notation gives us a lower bound, but it does not guarantee that the algorithm will always take Ω(f(n)) time or space. It only means that the algorithm will never take less than Ω(f(n)) time or space.



# Time-Space Trade-off

- A time-space trade-off is a situation where an algorithm or program trades increased space usage with decreased time, or vice versa.
- Here, space refers to the data storage consumed in performing a given task (RAM, HDD, etc), and time refers to the time consumed in performing the task.
- A time-space trade-off can be applied to the problem of data storage. If data is stored uncompressed, it takes more space but access takes less time than if the data were stored compressed (since compressing the data reduces the amount of space it takes, but it takes time to run the decompression algorithm)  .
- A time-space trade-off can also be applied to the problem of algorithm design. For example, some sorting algorithms, such as insertion sort, use less space but more time than other sorting algorithms, such as merge sort, which use more space but less time.
- The choice of the best algorithm or program depends on the available resources and the requirements of the task. Sometimes, a balance between time and space can be achieved by using a hybrid approach that combines different techniques.
- Time-space trade-offs are important to consider in the field of data structures, as different data structures have different advantages and disadvantages in terms of time and space complexity. For example, arrays have constant time access but fixed size, while linked lists have variable size but linear time access.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content on the topic of Abstract Data Types (ADT) for the notes of the Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT) in the subject of DATA STRUCTURE.

# Abstract Data Types (ADT)

- An abstract data type (ADT) is a mathematical model of a data structure that specifies the type of data stored, the operations supported and the behavior of those operations.
- An ADT does not specify how the data structure is implemented, only the interface that it provides to the user or other data structures.
- An ADT can be implemented using different data structures, such as arrays, linked lists, trees, etc. The choice of implementation depends on the efficiency and complexity of the operations.
- An ADT can be defined using a specification language, such as pseudocode, that describes the syntax and semantics of the operations.
- An ADT can be represented using an abstract data type diagram, which shows the name of the ADT, the data stored, the operations supported and the parameters and return values of those operations.

## Examples of ADTs

- Some common examples of ADTs are:

  - Stack: A linear data structure that stores data in a last-in first-out (LIFO) order. It supports two operations: push (insert an element at the top) and pop (remove and return the element at the top).
  - Queue: A linear data structure that stores data in a first-in first-out (FIFO) order. It supports two operations: enqueue (insert an element at the rear) and dequeue (remove and return the element at the front).
  - List: A linear data structure that stores a sequence of data elements. It supports operations such as insert, delete, search, traverse, etc.
  - Set: A collection of data elements that does not allow duplicates. It supports operations such as add, remove, contains, union, intersection, etc.
  - Map: A collection of key-value pairs that associates a unique key with a value. It supports operations such as put, get, remove, containsKey, containsValue, etc.
  - Graph: A data structure that represents a set of vertices and a set of edges that connect pairs of vertices. It supports operations such as addVertex, addEdge, removeVertex, removeEdge, adjacent, degree, etc.

## Benefits of ADTs

- Some benefits of using ADTs are:

  - Abstraction: ADTs hide the details of the implementation and provide a clear and simple interface to the user. This allows the user to focus on the problem-solving logic rather than the data structure details.
  - Encapsulation: ADTs encapsulate the data and the operations on the data in a single entity. This prevents unauthorized access or modification of the data and ensures data integrity and consistency.
  - Modularity: ADTs allow the implementation of the data structure to be changed or replaced without affecting the user or other data structures. This facilitates code reuse, maintenance and testing.
  - Generality: ADTs can be defined for any type of data and any set of operations. This allows the user to create custom data structures that suit their specific needs and applications.



# Unit 2 - Arrays and Linked Lists

## Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- An array can be single-dimensional or multi-dimensional, depending on the number of dimensions or subscripts used to specify an element.
- A single-dimensional array is a linear array, where each element is identified by a single index. For example, `A[5]` is a single-dimensional array of size 5, and `A[3]` refers to the fourth element of the array.
- A multi-dimensional array is an array of arrays, where each element is identified by a combination of indices. For example, `B[3][4]` is a two-dimensional array of size 3 by 4, and `B[2][1]` refers to the second element of the third row of the array.
- The representation of arrays in memory depends on the order of storing the elements, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the two-dimensional array `B[3][4]` is stored as `B[0][0], B[0][1], B[0][2], B[0][3], B[1][0], B[1][1], B[1][2], B[1][3], B[2][0], B[2][1], B[2][2], B[2][3]`.
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the two-dimensional array `B[3][4]` is stored as `B[0][0], B[1][0], B[2][0], B[0][1], B[1][1], B[2][1], B[0][2], B[1][2], B[2][2], B[0][3], B[1][3], B[2][3]`.
- The index formulae for accessing an element of an array depend on the order of storage, the base address of the array, the size of each element, and the number of dimensions.
- For a single-dimensional array `A[n]` stored in row major order, with base address `BA` and element size `ES`, the address of `A[i]` is given by `BA + i * ES`.
- For a two-dimensional array `B[m][n]` stored in row major order, with base address `BA` and element size `ES`, the address of `B[i][j]` is given by `BA + (i * n + j) * ES`.
- For a three-dimensional array `C[p][q][r]` stored in row major order, with base address `BA` and element size `ES`, the address of `C[i][j][k]` is given by `BA + (i * q * r + j * r + k) * ES`.
- For an n-dimensional array `D[d1][d2]...[dn]` stored in row major order, with base address `BA` and element size `ES`, the address of `D[i1][i2]...[in]` is given by `BA + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in-1 * dn + in) * ES`.
- The index formulae for accessing an element of an array stored in column major order can be derived by reversing the order of the indices and the dimensions in the formulae for row major order.
- Arrays are used to store and manipulate data in various applications, such as matrices, vectors, tables, lists, strings, etc.
- Sparse matrices are matrices that have a large number of zero elements, and only a few non-zero elements. Storing sparse matrices as arrays can waste a lot of memory space and computation time.
- Sparse matrices can be represented more efficiently by using different techniques, such as linked lists, arrays of lists, coordinate lists, compressed row storage, compressed column storage, etc.

## Linked Lists

- A linked list is a linear data structure, where each element is a separate object that contains a data field and a pointer field that links to the next element.
- A linked list can be implemented using either an array or a pointer.
- An array implementation of a linked list uses a fixed-size array to store the data and the next index of each element. For example, the linked list `



# Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Arrays: Definition, Single and Multidimensional Arrays

- An array is a collection of homogeneous elements stored in a contiguous memory location for better access and easier calculation by the system.
- An array is a data structure consisting of a collection of elements, each identified by at least one array index or key.
- An array is an assortment of similar types of data, while a list can include dissimilar data values.
- An array can be of any type, including an array type.
- An array can be single-dimensional or multidimensional, depending on the number of dimensions or indices it has.
- A single-dimensional array is a linear array that has one index or key for each element. It can be represented as a row or a column of elements.
- A multidimensional array is an array that has more than one index or key for each element. It can be represented as a matrix or a table of elements, or a higher-dimensional structure.
- The number of dimensions or indices of an array is also called its rank or order.
- The size or length of an array is the number of elements it can hold.
- The position of each element in an array can be computed from its index or key by a mathematical formula.
- An array can be declared, initialized, accessed, modified, and iterated using different syntaxes and methods depending on the programming language.

## Representation of Arrays: Row Major Order, and Column Major Order

- Row major order and column major order are two ways of storing multidimensional arrays in linear memory.
- Row major order means that the elements of a multidimensional array are stored row by row, or that the row index varies faster than the column index.
- Column major order means that the elements of a multidimensional array are stored column by column, or that the column index varies faster than the row index.
- The choice of row major order or column major order affects the computation of the memory address of an element in a multidimensional array, as well as the traversal order of the array.
- Different programming languages use different conventions for the representation of arrays. For example, C and C++ use row major order, while Fortran and MATLAB use column major order.

## Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

- The index formula is the mathematical expression that calculates the memory address of an element in an array, given its index or key and the base address of the array.
- The index formula depends on the representation of the array, the size of each dimension, and the size of each element.
- For a single-dimensional array A of size n and element size s, the index formula for row major order is:

  - `address(A[i]) = base(A) + i * s`

  - where i is the index of the element, base(A) is the base address of the array, and address(A[i]) is the memory address of the element.

- For a two-dimensional array A of size m x n and element size s, the index formula for row major order is:

  - `address(A[i][j]) = base(A) + (i * n + j) * s`

  - where i and j are the row and column indices of the element, respectively.

- For a two-dimensional array A of size m x n and element size s, the index formula for column major order is:

  - `address(A[i][j]) = base(A) + (j * m + i) * s`

  - where i and j are the row and column indices of the element, respectively.

- For a three-dimensional array A of size l x m x n and element size s, the index formula for row major order is:

  - `address(A[i][j][k]) = base(A) + (i * m * n + j * n + k) * s`

  - where i, j, and k are the indices of the element along the three dimensions, respectively



# Single and Multidimensional Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- An array can have one or more dimensions, depending on the number of subscripts used to specify the position of an element.
- A single-dimensional array (or 1-D array) is a linear array that has only one subscript, representing the row number of the element. For example, `A[5]` is a 1-D array of size 5, and `A[3]` is the element at the third row.
- A multidimensional array (or n-D array) is an array that has more than one subscript, representing the row, column, and other dimensions of the element. For example, `B[3][4]` is a 2-D array of size 3 by 4, and `B[2][3]` is the element at the second row and third column.
- The representation of arrays in memory depends on the order of storing the elements, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the 2-D array `B[3][4]` is stored as `B[0][0], B[0][1], B[0][2], B[0][3], B[1][0], B[1][1], B[1][2], B[1][3], B[2][0], B[2][1], B[2][2], B[2][3]`.
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the 2-D array `B[3][4]` is stored as `B[0][0], B[1][0], B[2][0], B[0][1], B[1][1], B[2][1], B[0][2], B[1][2], B[2][2], B[0][3], B[1][3], B[2][3]`.
- The index formulae for 1-D, 2-D, 3-D and n-D arrays are derived based on the size of each dimension, the base address of the array, and the order of storing the elements.
- For a 1-D array `A[n]` with base address `BA` and element size `ES`, the address of `A[i]` is given by `BA + i * ES`.
- For a 2-D array `B[m][n]` with base address `BA` and element size `ES`, the address of `B[i][j]` is given by `BA + (i * n + j) * ES` in row major order, and `BA + (j * m + i) * ES` in column major order.
- For a 3-D array `C[p][q][r]` with base address `BA` and element size `ES`, the address of `C[i][j][k]` is given by `BA + (i * q * r + j * r + k) * ES` in row major order, and `BA + (k * p * q + j * p + i) * ES` in column major order.
- For an n-D array `D[d1][d2]...[dn]` with base address `BA` and element size `ES`, the address of `D[i1][i2]...[in]` is given by `BA + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * ES` in row major order, and `BA + (in * d1 * d2 * ... * d(n-1) + i(n-1) * d1 * d2 * ... * d(n-2) + ... + i1) * ES` in column major order.
- Arrays are used to store and manipulate data in various applications, such as matrices, vectors, polynomials, strings, graphs, images, etc.
- Sparse matrices are matrices that have a large number of zero elements, and only a few non-zero elements. Storing sparse matrices as arrays can waste a lot of memory space and computation time.
- Sparse matrices can be represented more efficiently by using different methods, such as linked lists, arrays of lists, arrays of arrays, etc. These methods store only the non-zero elements and their positions, and use pointers



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of Representation of Arrays: Row Major Order, and Column Major Order. Here is the content I have generated for you in markdown format:

# Representation of Arrays: Row Major Order, and Column Major Order

## Definition of Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations.
- An array can be single-dimensional or multi-dimensional, depending on the number of indices required to access its elements.
- An array can be declared as `type array_name[size1][size2]...[sizeN]`, where `type` is the data type of the elements, `array_name` is the identifier of the array, and `size1`, `size2`, ..., `sizeN` are the dimensions of the array.

## Row Major Order and Column Major Order

- Row major order and column major order are two ways of storing a multi-dimensional array in linear memory.
- In row major order, the elements of an array are stored row by row, i.e., the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column major order, the elements of an array are stored column by column, i.e., the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The choice of row major order or column major order depends on the programming language, the compiler, and the application of the array.

## Derivation of Index Formulae for 1-D, 2-D, 3-D and n-D Array

- To access an element of an array, we need to calculate its address in memory, based on its indices and the base address of the array.
- The base address of an array is the address of the first element of the array, usually denoted by `A[0]` or `A[0][0]...[0]`.
- The index formula is the expression that gives the address of an element of an array, based on its indices, the base address, and the order of storage.
- For a 1-D array of size `N`, the index formula is:

  - In row major order: `A[i] = A[0] + i * size_of(type)`
  - In column major order: `A[i] = A[0] + i * size_of(type)`

- For a 2-D array of size `M x N`, the index formula is:

  - In row major order: `A[i][j] = A[0][0] + (i * N + j) * size_of(type)`
  - In column major order: `A[i][j] = A[0][0] + (j * M + i) * size_of(type)`

- For a 3-D array of size `L x M x N`, the index formula is:

  - In row major order: `A[i][j][k] = A[0][0][0] + (i * M * N + j * N + k) * size_of(type)`
  - In column major order: `A[i][j][k] = A[0][0][0] + (k * L * M + j * L + i) * size_of(type)`

- For an n-D array of size `D1 x D2 x ... x Dn`, the index formula is:

  - In row major order: `A[i1][i2]...[in] = A[0][0]...[0] + (i1 * D2 * D3 * ... * Dn + i2 * D3 * D4 * ... * Dn + ... + in) * size_of(type)`
  - In column major order: `A[i1][i2]...[in] = A[0][0]...[0] + (in * D1 * D2 * ... * Dn-1 + in-1 * D1 * D2 * ... * Dn-2 + ... + i1) * size_of(type)`

## Application of Arrays

- Arrays are widely used in various fields of computer science and engineering, such as:

  - Storing and manipulating data in a structured and efficient way.
  - Implementing matrices, vectors, and other mathematical objects and operations.
  - Implementing stacks, queues, lists, and other abstract data types.
  - Implementing sorting, searching, hashing, and other algorithms.
  - Representing images, audio, video, and other multimedia data.
  - Representing graphs, trees



# Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

## 1-D Array

A one-dimensional array is a linear collection of elements that are stored in contiguous memory locations. The elements of a one-dimensional array can be accessed by using an index that specifies the position of the element in the array. The index usually starts from zero or one, depending on the programming language or the convention used.

The index formula for a one-dimensional array is a function that calculates the memory address of any element in the array, given the base address of the array, the size of each element, and the index of the element. The index formula for a one-dimensional array can be derived as follows:

- Let A be the name of the array, B be the base address of the array, W be the size of each element in bytes, and i be the index of the element to be accessed.
- The address of the first element of the array, A[0] or A[1], is equal to the base address of the array, B.
- The address of the second element of the array, A[1] or A[2], is equal to the base address of the array plus the size of one element, B + W.
- The address of the third element of the array, A[2] or A[3], is equal to the base address of the array plus the size of two elements, B + 2W.
- In general, the address of the ith element of the array, A[i] or A[i+1], is equal to the base address of the array plus the size of i elements, B + iW.

Therefore, the index formula for a one-dimensional array is:

LOC(A[i]) = B + iW

where LOC(A[i]) is the address of the ith element of the array .

## 2-D Array

A two-dimensional array is a collection of elements that are arranged in rows and columns, forming a matrix or a table. The elements of a two-dimensional array can be accessed by using two indices that specify the row and the column of the element in the array. The indices usually start from zero or one, depending on the programming language or the convention used.

The index formula for a two-dimensional array is a function that calculates the memory address of any element in the array, given the base address of the array, the size of each element, the number of columns in the array, and the row and column indices of the element. The index formula for a two-dimensional array can be derived as follows:

- Let A be the name of the array, B be the base address of the array, W be the size of each element in bytes, C be the number of columns in the array, and i and j be the row and column indices of the element to be accessed, respectively.
- The address of the first element of the first row of the array, A[0][0] or A[1][1], is equal to the base address of the array, B.
- The address of the second element of the first row of the array, A[0][1] or A[1][2], is equal to the base address of the array plus the size of one element, B + W.
- The address of the first element of the second row of the array, A[1][0] or A[2][1], is equal to the base address of the array plus the size of one row, B + WC.
- The address of the second element of the second row of the array, A[1][1] or A[2][2], is equal to the base address of the array plus the size of one row and one element, B + WC + W.
- In general, the address of the element in the ith row and jth column of the array, A[i][j] or A[i+1][j+1], is equal to the base address of the array plus the size of i rows and j elements, B + iWC + jW.

Therefore, the index formula for a two-dimensional array is:

LOC(A[i][j]) = B + iWC + jW

where LOC(A[i][j]) is the address of the element in the ith row and jth column of the array .

## 3-D Array

A three-dimensional array is a collection of elements that are arranged in layers, rows, and columns, forming a cube or a box. The elements of a three



# Application of arrays

- Arrays are the simplest data structures that store items of the same data type in a contiguous memory location  .
- Arrays can be used to store data in tabular format, such as contacts, marks, grades, etc  .
- Arrays can be used to implement other data structures, such as matrices, linked lists, stacks, queues, etc  .
- Arrays can be used to perform sorting and searching algorithms, such as bubble sort, binary search, etc .
- Arrays can be used to represent polynomials, such as ax^2 + bx + c, by storing the coefficients in an array.
- Arrays can be classified into single and multidimensional arrays, depending on the number of indices required to access an element.
- Single dimensional arrays have one index, such as arr[i], where i is the position of the element in the array.
- Multidimensional arrays have more than one index, such as arr[i][j], where i and j are the row and column positions of the element in the array.
- The representation of arrays can be done in two ways: row major order and column major order, depending on how the elements are stored in the memory.
- Row major order stores the elements of an array row by row, such that the elements of the first row are stored first, followed by the elements of the second row, and so on.
- Column major order stores the elements of an array column by column, such that the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The derivation of index formulae for 1-D, 2-D, 3-D and n-D arrays can be done by using the base address, size of the data type, and the indices of the element.
- For a 1-D array arr[n], the index formula is: address(arr[i]) = base(arr) + i * size(data type).
- For a 2-D array arr[m][n], the index formula for row major order is: address(arr[i][j]) = base(arr) + (i * n + j) * size(data type).
- For a 2-D array arr[m][n], the index formula for column major order is: address(arr[i][j]) = base(arr) + (j * m + i) * size(data type).
- For a 3-D array arr[l][m][n], the index formula for row major order is: address(arr[i][j][k]) = base(arr) + (i * m * n + j * n + k) * size(data type).
- For a 3-D array arr[l][m][n], the index formula for column major order is: address(arr[i][j][k]) = base(arr) + (k * m * l + j * l + i) * size(data type).
- For an n-D array arr[d1][d2]...[dn], the index formula for row major order is: address(arr[i1][i2]...[in]) = base(arr) + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size(data type).
- For an n-D array arr[d1][d2]...[dn], the index formula for column major order is: address(arr[i1][i2]...[in]) = base(arr) + (in * d1 * d2 * ... * d(n-1) + i(n-1) * d1 * d2 * ... * d(n-2) + ... + i1) * size(data type).
- Sparse matrices are matrices that have a large number of zero elements, and storing them as arrays would waste a lot of memory space.
- Sparse matrices can be represented in different ways, such as triplet representation, compressed row representation, compressed column representation, etc.
- Triplet representation stores the non-zero elements of a sparse matrix along with their row and column indices in a 3-column array.
- Compressed row



# Sparse Matrices and their representations

- A sparse matrix is a matrix that has a large number of zero elements and a small number of non-zero elements.
- Sparse matrices arise in many applications, such as finite element methods, graph theory, network analysis, image processing, etc.
- Storing and manipulating sparse matrices efficiently is important for saving space and time.
- There are different ways of representing sparse matrices, depending on the structure and sparsity pattern of the matrix.
- Some common representations are:

  - **Triplet representation**: This is the simplest way of storing a sparse matrix. It consists of three arrays: one for the row indices, one for the column indices, and one for the non-zero values. The length of each array is equal to the number of non-zero elements in the matrix. For example, the matrix

    ```
    | 0 0 0 0 |
    | 5 8 0 0 |
    | 0 0 3 0 |
    | 0 6 0 0 |
    ```

    can be stored as:

    ```
    row = [1, 1, 2, 3]
    col = [0, 1, 2, 1]
    val = [5, 8, 3, 6]
    ```

    The advantage of this representation is that it is easy to construct and manipulate. The disadvantage is that it does not preserve the order or structure of the matrix, and it may have duplicate entries for the same element.

  - **Compressed sparse row (CSR) representation**: This is a more compact way of storing a sparse matrix. It consists of three arrays: one for the non-zero values, one for the column indices, and one for the row pointers. The length of the first two arrays is equal to the number of non-zero elements in the matrix. The length of the third array is equal to the number of rows plus one. The row pointers array stores the index of the first non-zero element in each row, and the last element is the total number of non-zero elements. For example, the matrix

    ```
    | 0 0 0 0 |
    | 5 8 0 0 |
    | 0 0 3 0 |
    | 0 6 0 0 |
    ```

    can be stored as:

    ```
    val = [5, 8, 3, 6]
    col = [0, 1, 2, 1]
    row_ptr = [0, 0, 2, 3, 4]
    ```

    The advantage of this representation is that it preserves the row order and structure of the matrix, and it allows for efficient row-wise operations and matrix-vector multiplication. The disadvantage is that it is not easy to insert or delete elements, and it does not support column-wise operations.

  - **Compressed sparse column (CSC) representation**: This is a similar way of storing a sparse matrix as CSR, but with the roles of rows and columns reversed. It consists of three arrays: one for the non-zero values, one for the row indices, and one for the column pointers. The length of the first two arrays is equal to the number of non-zero elements in the matrix. The length of the third array is equal to the number of columns plus one. The column pointers array stores the index of the first non-zero element in each column, and the last element is the total number of non-zero elements. For example, the matrix

    ```
    | 0 0 0 0 |
    | 5 8 0 0 |
    | 0 0 3 0 |
    | 0 6 0 0 |
    ```

    can be stored as:

    ```
    val = [5, 6, 8, 3]
    row = [1, 3, 1, 2]
    col_ptr = [0, 2, 4, 5, 5]
    ```

    The advantage of this representation is that it preserves the column order and structure of the matrix, and it allows for efficient column-wise operations and matrix-vector multiplication. The disadvantage is that it is not easy to insert or delete elements, and it does not support row-wise operations.

  - **Coordinate list (COO) representation**: This is a variation of the triplet representation, where the three arrays are sorted by row and column indices. This makes it easier to convert to CSR or CSC formats, and to perform matrix operations such as addition, subtraction, and multiplication. For example, the matrix

    ```
    | 0 0 0 0

```




# Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Linked lists

- A linked list is a linear data structure that consists of a sequence of nodes, each containing some data and a pointer to the next node in the list.
- A linked list can be used to store any type of data, such as numbers, characters, strings, etc.
- A linked list can grow or shrink dynamically, depending on the insertion and deletion operations performed on it.
- A linked list does not require a contiguous block of memory, unlike an array. It can utilize the available memory space efficiently.
- A linked list can be classified into different types, such as singly linked list, doubly linked list, circularly linked list, etc., based on the number and direction of pointers in each node.

## Array Implementation of Singly Linked Lists

- A singly linked list can be implemented using an array, where each element of the array represents a node of the list.
- The array should have two fields for each element: one to store the data and one to store the index of the next element in the list.
- The first element of the array is the head of the list, and the last element is the tail of the list.
- A special value, such as -1, can be used to indicate the end of the list or an empty list.
- For example, the following array represents a singly linked list of three nodes, containing the data 10, 20, and 30:

| Data | Next |
|------|------|
| 10   | 1    |
| 20   | 2    |
| 30   | -1   |

- The advantages of using an array to implement a singly linked list are:
  - It is easy to access any element of the list by its index.
  - It is easy to implement the basic operations, such as insertion, deletion, and traversal, using simple array operations.
- The disadvantages of using an array to implement a singly linked list are:
  - It requires a fixed size of memory, which may not be available or may be wasted if the list size changes frequently.
  - It is difficult to insert or delete an element at the beginning or in the middle of the list, as it requires shifting the subsequent elements in the array.

## Pointer Implementation of Singly Linked Lists

- A singly linked list can also be implemented using pointers, where each node of the list is a dynamic memory allocation that contains two fields: one to store the data and one to store the pointer to the next node in the list.
- The head of the list is a pointer that points to the first node of the list, and the tail of the list is a pointer that points to the last node of the list.
- A null pointer can be used to indicate the end of the list or an empty list.
- For example, the following diagram represents a singly linked list of three nodes, containing the data 10, 20, and 30:

singly linked list pointer

- The advantages of using pointers to implement a singly linked list are:
  - It does not require a fixed size of memory, as the nodes can be allocated and deallocated dynamically as per the list size.
  - It is easy to insert or delete an element at any position of the list, as it only requires updating the pointers of the adjacent nodes.
- The disadvantages of using pointers to implement a singly linked list are:
  - It requires extra space for storing the pointers in each node, which may increase the memory overhead.
  - It is difficult to access any element of the list by its index, as it requires traversing the list from the head until the desired node is reached.

## Doubly Linked List

- A doubly linked list is a linear data structure that consists of a sequence of nodes, each containing some data and two pointers: one to the previous node and one to the next node in the list.
- A doubly linked list can be used to store any type of data, such as numbers, characters, strings, etc.
- A doubly linked list can grow or shrink dynamically, depending on the insertion and deletion operations performed on it.
- A doubly linked list does not require a contiguous block of memory, unlike an array. It can utilize the available memory space efficiently.
- A doubly linked list can be traversed in both forward and backward directions, unlike a singly linked list that can only be traversed in one direction.
- A doubly linked list can be



# Unit 3 - Searching and Sorting

## Searching
- Searching is the process of finding a particular element or value in a collection of elements or values.
- Searching can be performed on different types of data structures, such as arrays, lists, trees, graphs, etc.
- Searching can be classified into two categories: linear searching and binary searching.

### Linear Searching
- Linear searching is the simplest method of searching, where the search element is compared with each element of the collection sequentially until a match is found or the end of the collection is reached.
- Linear searching can be performed on sorted or unsorted collections, but it is inefficient for large collections as it requires O(n) time in the worst case, where n is the number of elements in the collection.
- Examples of linear searching algorithms are sequential search and index sequential search.

#### Sequential Search
- Sequential search is a linear searching algorithm that starts from the first element of the collection and compares it with the search element. If they match, the search is successful and the position of the element is returned. If they do not match, the algorithm moves to the next element and repeats the process until a match is found or the end of the collection is reached.
- Sequential search can be implemented using a loop or a recursion.
- Sequential search is simple and easy to implement, but it is slow and inefficient for large collections.

#### Index Sequential Search
- Index sequential search is a linear searching algorithm that uses an index to speed up the search process. An index is a separate data structure that stores the key values and the positions of some elements of the collection. The index is usually sorted in ascending or descending order of the key values.
- Index sequential search first searches the index for the search element using binary search. If the search element is found in the index, the position of the corresponding element in the collection is returned. If the search element is not found in the index, the algorithm determines the range of the collection where the search element may be present using the nearest index values. Then, the algorithm performs a sequential search on that range until a match is found or the end of the range is reached.
- Index sequential search is faster than sequential search, but it requires extra space and time to create and maintain the index. The index also needs to be updated whenever the collection is modified.

### Binary Searching
- Binary searching is a method of searching that works on sorted collections. It uses the divide and conquer technique to reduce the search space by half in each iteration.
- Binary searching compares the search element with the middle element of the collection. If they match, the search is successful and the position of the element is returned. If the search element is smaller than the middle element, the algorithm discards the right half of the collection and repeats the process on the left half. If the search element is larger than the middle element, the algorithm discards the left half of the collection and repeats the process on the right half. This process continues until a match is found or the collection becomes empty.
- Binary search can be implemented using a loop or a recursion.
- Binary search is efficient and fast for large collections, as it requires O(log n) time in the worst case, where n is the number of elements in the collection. However, binary search requires the collection to be sorted in advance, which may take O(n log n) time in the worst case.

## Hashing
- Hashing is a technique of mapping a large set of keys or values to a smaller set of indices or addresses, using a function called a hash function. The smaller set is called a hash table, which is an array of fixed size.
- Hashing is useful for implementing fast and efficient searching, insertion, deletion, and retrieval operations on collections of data. The hash function transforms the key or value into an index or address, which can be used to access the corresponding element in the hash table in constant time.
- Hashing can also be used for data compression, encryption, checksums, etc.

### Hash Function
- A hash function is a function that maps a key or value to an index or address in the hash table. The hash function should be deterministic, meaning that it should always produce the same output for the same input. The hash function should also be uniform, meaning that it should distribute the keys or values evenly across the hash table, to avoid collisions.
- A hash function can be simple or complex, depending on the type and range of the keys or values, and the size and structure of the hash table. Some examples of hash functions are:

  - Division method: h(k) = k mod m, where k is the key, m is the size of the hash table, and h(k) is the index or address.
  - Multiplication method: h(k)



# Concept of Searching

- Searching is the process of finding a given value position in a list of values.
- It decides whether a search key is present in the data or not.
- It is the algorithmic process of finding a particular item in a collection of items.
- It can be done on internal data structure or on external data structure.
- Searching in data structure can be done by applying searching algorithms to check for or extract the desired information from the set of items stored in the form of elements in the computer memory .
- Based on the type of search operation, these algorithms are generally classified into two categories:
  - Sequential Search: In this, the list or array is traversed sequentially and every element is checked.
  - Interval Search: In this, the list or array is divided into smaller segments of equal size and then a search is performed on the segment that may contain the item.

## Sequential Search

- Sequential search is the simplest and most basic search algorithm.
- It is also known as linear search.
- It works by comparing each element of the list or array with the search key until a match is found or the end of the list is reached.
- It can be applied to any type of data structure, such as array, linked list, tree, or graph.
- It has the best case time complexity of O(1) when the element is found at the first position.
- It has the worst case time complexity of O(n) when the element is not found or found at the last position.
- It has the average case time complexity of O(n/2) when the element is found at the middle position.
- It is suitable for small and unsorted lists or arrays.

## Index Sequential Search

- Index sequential search is a variation of sequential search that uses an index to speed up the search process.
- It is also known as indexed sequential search or index search.
- It works by dividing the list or array into smaller segments of equal size and creating an index table that stores the first element and the position of each segment.
- It then compares the search key with the first element of each segment in the index table until a segment is found that may contain the item.
- It then performs a sequential search on that segment to find the exact position of the item.
- It can be applied to any type of data structure, such as array, linked list, tree, or graph.
- It has the best case time complexity of O(1) when the element is found at the first position of the first segment.
- It has the worst case time complexity of O(log n + n/m) when the element is not found or found at the last position of the last segment, where n is the size of the list or array and m is the size of the segment.
- It has the average case time complexity of O(log n + n/2m) when the element is found at the middle position of the middle segment.
- It is suitable for large and sorted lists or arrays.

## Binary Search

- Binary search is a popular and efficient search algorithm that uses the divide and conquer technique.
- It works by repeatedly dividing the sorted list or array into two halves and comparing the search key with the middle element of each half until a match is found or the list becomes empty.
- It can be applied to any type of data structure that allows random access, such as array or binary tree.
- It has the best case time complexity of O(1) when the element is found at the middle position of the list or array.
- It has the worst case time complexity of O(log n) when the element is not found or found at the first or last position of the list or array.
- It has the average case time complexity of O(log n) when the element is found at any other position of the list or array.
- It is suitable for large and sorted lists or arrays.



# Sequential Search

- Sequential search is the most natural searching method. In this method, the searching begins with searching every element of the list till the required record is found.
- Sequential search is also known as linear search, as it scans the list or array linearly from the first element to the last element .
- The average number of comparisons in a sequential search is (N+1)/2 where N is the size of the list or array.
- The best case of sequential search is when the target element is the first element, and the worst case is when the target element is the last element or not present in the list or array.
- The time complexity of sequential search is O(N) in the worst case and O(1) in the best case.
- The advantages of sequential search are that it is simple, easy to implement, and does not require any sorting or ordering of the list or array.
- The disadvantages of sequential search are that it is slow, inefficient, and impractical for large lists or arrays.

: https://stacktips.com/articles/sequential-search-algorithm-in-data-structure
: https://www.careerride.com/Data-structure-sequential-search.aspx
: https://www.educba.com/searching-in-data-structure/
: https://www.geeksforgeeks.org/linear-search/



# Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database .
- An index file is a data structure that contains references to a group of records or blocks in the array or database, based on some key values .
- The index file is searched first using a suitable algorithm, such as binary search, to find the index entry that matches or precedes the search key .
- The index entry points to the block or record where the search key is likely to be found, or to another expanded index that further narrows down the search range .
- The block or record is then searched sequentially to locate the exact position of the search key, or to determine that the key is not present .
- Index sequential search reduces the number of comparisons and disk accesses needed to find a key, compared to a simple sequential search .
- However, index sequential search also requires extra space and time to create and maintain the index file, and to update it whenever the array or database is modified .
- Index sequential search is suitable for applications where the array or database is relatively static and the search frequency is high .



# Binary Search

- Binary search is an efficient algorithm for finding an element within a sorted array  .
- Binary search works by repeatedly dividing in half the portion of the list that could contain the element, until you've narrowed down the possible locations to just one.
- Binary search compares the element to the middle element of the array. If they are not equal, the half in which the element cannot lie is eliminated and the search continues on the remaining half, again taking the middle element and comparing it until the element is found.
- Binary search has a time complexity of O(log n), where n is the number of elements in the array .
- Binary search requires that the array is sorted in ascending or descending order before applying the algorithm .
- Binary search can be implemented using iterative or recursive methods.
- Binary search is useful for building more complex algorithms in computer science, such as interpolation search, exponential search, and binary search trees.



# Concept of Hashing & Collision resolution Techniques used in Hashing

## Hashing
- Hashing is a technique of mapping a set of keys to a set of values using a hash function.
- A hash function is a function that takes a key as input and returns an integer value, called a hash value or a hash code, as output.
- The hash value is used as an index to store the key-value pair in an array, called a hash table or a hash map.
- The hash table has a fixed size, usually a prime number, and each slot in the hash table can store one or more key-value pairs.
- The advantage of hashing is that it allows fast access to the values associated with the keys, as the hash function can compute the index in constant time.
- The disadvantage of hashing is that it may cause collisions, which occur when two or more keys have the same hash value and map to the same slot in the hash table.

## Collision resolution Techniques
- Collision resolution techniques are methods to handle the collisions in the hash table and to store the key-value pairs in a proper way.
- There are two main types of collision resolution techniques: open hashing and closed hashing.

### Open hashing (Separate chaining)
- Open hashing is a technique that uses a linked list to store the key-value pairs that have the same hash value in the same slot of the hash table.
- Each slot in the hash table is a pointer to the head of a linked list, which contains the key-value pairs that have the same hash value.
- To insert a new key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the key-value pair is added to the front of the linked list at the corresponding slot in the hash table.
- To search for a key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the linked list at the corresponding slot in the hash table is traversed until the key is found or the end of the list is reached.
- To delete a key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the linked list at the corresponding slot in the hash table is traversed until the key is found and removed from the list.
- The advantage of open hashing is that it can handle any number of collisions, as the linked list can grow dynamically.
- The disadvantage of open hashing is that it requires extra space for the pointers and the linked list, and it may cause long chains that degrade the performance.

### Closed hashing (Open addressing)
- Closed hashing is a technique that uses the hash table itself to store the key-value pairs, without using any extra space or pointers.
- Each slot in the hash table can store only one key-value pair, and the hash table size is usually larger than the number of keys to avoid collisions.
- To insert a new key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the slot at the hash value is checked. If it is empty, the key-value pair is stored there. If it is occupied, a different slot is probed until an empty slot is found or the hash table is full.
- To search for a key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the slot at the hash value is checked. If it is empty, the key is not in the hash table. If it is occupied, the key is compared with the stored key. If they match, the value is returned. If they do not match, a different slot is probed until the key is found or an empty slot is reached.
- To delete a key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the slot at the hash value is checked. If it is empty, the key is not in the hash table. If it is occupied, the key is compared with the stored key. If they match, the slot is marked as deleted. If they do not match, a different slot is probed until the key is found or an empty slot is reached.
- The advantage of closed hashing is that it does not require extra space or pointers, and it can achieve better cache performance.
- The disadvantage of closed hashing is that it may cause clustering, which occurs when many keys have the same or nearby hash values and occupy the same or adjacent slots in the hash table, making the probing more difficult.

#### Probing methods
- Probing methods are the ways to find a different slot in the hash table when a collision occurs in closed



# Sorting: Insertion Sort, Selection, Bubble Sort, Quick Sort, Merge Sort, Heap Sort and Radix Sort

Sorting is the process of arranging the elements of an array or list in a specific order, such as ascending or descending, based on a comparison operator. Sorting algorithms are the methods of implementing sorting in data structures. Sorting algorithms can be classified into different categories based on their time complexity, space complexity, stability, adaptability, and recursion.

## Insertion Sort

Insertion sort is a simple and stable sorting algorithm that works by inserting each element of the array into its correct position in the sorted part of the array. The algorithm starts from the second element and compares it with the previous elements, shifting them to the right until it finds the correct position to insert the element. The algorithm repeats this process for each element until the array is sorted.

The time complexity of insertion sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted. The space complexity is O(1) as it only requires a constant amount of auxiliary space. Insertion sort is adaptive, meaning it performs better for partially sorted arrays. Insertion sort is not suitable for large arrays as it involves many comparisons and shifts.

## Selection Sort

Selection sort is a simple and unstable sorting algorithm that works by selecting the smallest or largest element of the array and placing it at the beginning or end of the sorted part of the array. The algorithm repeats this process for each element until the array is sorted.

The time complexity of selection sort is O(n^2) in all cases, as it involves n-1 comparisons for each of the n elements. The space complexity is O(1) as it only requires a constant amount of auxiliary space. Selection sort is not adaptive, meaning it performs the same for any order of the array. Selection sort is not suitable for large arrays as it involves many comparisons.

## Bubble Sort

Bubble sort is a simple and stable sorting algorithm that works by swapping the adjacent elements of the array if they are in the wrong order. The algorithm repeats this process for each element until no swaps are required, indicating that the array is sorted.

The time complexity of bubble sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted. The space complexity is O(1) as it only requires a constant amount of auxiliary space. Bubble sort is adaptive, meaning it performs better for partially sorted arrays. Bubble sort is not suitable for large arrays as it involves many comparisons and swaps.

## Quick Sort

Quick sort is a fast and unstable sorting algorithm that works by dividing the array into two subarrays based on a pivot element, such that all the elements in the left subarray are smaller than the pivot and all the elements in the right subarray are larger than the pivot. The algorithm then recursively sorts the subarrays until the array is sorted.

The time complexity of quick sort is O(n log n) in the average and best case, and O(n^2) in the worst case when the array is already sorted or contains many duplicate elements. The space complexity is O(log n) in the average and best case, and O(n) in the worst case due to the recursive calls. Quick sort is not adaptive, meaning it performs the same for any order of the array. Quick sort is suitable for large arrays as it involves fewer comparisons and swaps than other algorithms.

## Merge Sort

Merge sort is a fast and stable sorting algorithm that works by dividing the array into two equal or nearly equal subarrays, sorting them recursively, and then merging them back into a single sorted array. The algorithm uses a merge function that takes two sorted subarrays and merges them into one sorted array.

The time complexity of merge sort is O(n log n) in all cases, as it involves log n divisions and n comparisons for each division. The space complexity is O(n) as it requires an auxiliary array of the same size as the original array. Merge sort is not adaptive, meaning it performs the same for any order of the array. Merge sort is suitable for large arrays as it involves fewer comparisons than other algorithms.

## Heap Sort

Heap sort is a fast and unstable sorting algorithm that works by building a binary heap from the array, and then repeatedly extracting the maximum or minimum element from the heap and placing it at the end or beginning of the sorted part of the array. The algorithm maintains the heap property after each extraction by adjusting the heap.

The time complexity of heap sort is O(n log n) in all cases, as it involves n extractions and log n



## Unit 4 - Graphs

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. A graph can be used to model many types of problems, such as networks, maps, games, social networks, etc.

### Terminology used with Graph

Some common terms used with graphs are:

- **Degree** of a vertex: The number of edges incident to the vertex.
- **Parallel edges**: Two or more edges that connect the same pair of vertices.
- **Self-loop**: An edge that connects a vertex to itself.
- **Simple graph**: A graph that has no parallel edges or self-loops.
- **Multigraph**: A graph that may have parallel edges or self-loops.
- **Directed graph** (or digraph): A graph in which each edge has a direction, from one vertex to another.
- **Undirected graph**: A graph in which each edge has no direction, and can be traversed in either direction.
- **Weighted graph**: A graph in which each edge has a numerical value (or weight) associated with it, which can represent the cost, distance, time, etc. of traversing the edge.
- **Unweighted graph**: A graph in which each edge has no weight associated with it.
- **Path**: A sequence of vertices and edges that connects two vertices in a graph.
- **Cycle**: A path that starts and ends at the same vertex.
- **Acyclic graph**: A graph that has no cycles.
- **Connected graph**: A graph in which there is a path between any two vertices.
- **Disconnected graph**: A graph that has at least two vertices that are not connected by a path.
- **Complete graph**: A graph in which there is an edge between every pair of vertices.
- **Subgraph**: A graph that is formed by a subset of the vertices and edges of another graph.
- **Tree**: A connected, acyclic, undirected graph.
- **Forest**: A collection of trees.
- **Spanning tree**: A subgraph of a graph that is a tree and contains all the vertices of the graph.
- **Minimum spanning tree**: A spanning tree of a weighted graph that has the minimum total weight among all possible spanning trees.

### Data Structure for Graph Representations

There are different ways to represent a graph in a computer, depending on the type and size of the graph, and the operations that need to be performed on it. Some common data structures for graph representations are:

- **Adjacency matrix**: A two-dimensional array of size V x V, where V is the number of vertices in the graph, and each element A[i][j] indicates the presence or absence of an edge between vertex i and vertex j. If the graph is weighted, A[i][j] can also store the weight of the edge. The adjacency matrix is a simple and compact way to represent a graph, but it has some drawbacks, such as:
  - It requires O(V^2) space, which can be wasteful if the graph is sparse (has few edges).
  - It takes O(V) time to find the neighbors of a vertex, which can be slow if the graph is dense (has many edges).
  - It is not suitable for dynamic graphs (graphs that change over time), as adding or removing a vertex requires resizing the matrix.

- **Adjacency list**: A one-dimensional array of size V, where each element A[i] is a linked list of the vertices that are adjacent to vertex i. If the graph is weighted, each node in the linked list can also store the weight of the edge. The adjacency list is a flexible and efficient way to represent a graph, as it has some advantages, such as:
  - It requires O(V + E) space, where E is the number of edges in the graph, which can be optimal if the graph is sparse.
  - It takes O(degree) time to find the neighbors of a vertex, where degree is the number of edges incident to the vertex, which can be fast if the graph is sparse.
  - It is suitable for dynamic graphs, as adding or removing a vertex or an edge requires only updating the corresponding linked list.

- **Adjacency map**: A one-dimensional array of size V, where each element A[i] is a map (or a hash table) of the vertices that are adjacent to vertex i, and the values are the weights of the edges. The adjacency map is a variant of the adjacency list, that can be useful for weighted graphs, as it has some benefits, such as:
  - It requires O(V + E) space, which can be optimal if the graph is sparse.
  - It takes O(1) time



# Terminology used with Graph

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. A graph can be used to model many types of problems, such as networks, maps, games, social media, etc. Some of the common terminology used with graphs are:

- **Directed graph**: A graph where the edges have a direction, meaning that there is a distinction between the source and the destination of each edge. For example, a graph that represents the flights between different cities is a directed graph, because the flights go from one city to another, not vice versa.
- **Undirected graph**: A graph where the edges do not have a direction, meaning that there is no distinction between the source and the destination of each edge. For example, a graph that represents the roads between different cities is an undirected graph, because the roads can be traveled in both directions.
- **Weighted graph**: A graph where the edges have a weight, meaning that there is a numerical value associated with each edge that represents some attribute of the connection, such as distance, cost, time, etc. For example, a graph that represents the roads between different cities with the distances as the weights is a weighted graph.
- **Unweighted graph**: A graph where the edges do not have a weight, meaning that there is no numerical value associated with each edge. For example, a graph that represents the friendship relations between different people is an unweighted graph, because there is no numerical measure of how close two people are.
- **Simple graph**: A graph where there are no loops or multiple edges, meaning that there is at most one edge between any pair of vertices, and no edge connects a vertex to itself. For example, a graph that represents the friendship relations between different people is a simple graph, because a person cannot be friends with themselves, and two people cannot have more than one friendship relation.
- **Multigraph**: A graph where there can be multiple edges between any pair of vertices, but no loops, meaning that there can be more than one edge connecting the same pair of vertices, but no edge connects a vertex to itself. For example, a graph that represents the flights between different cities is a multigraph, because there can be more than one flight between the same pair of cities, but no flight can start and end at the same city.
- **Pseudograph**: A graph where there can be loops and multiple edges, meaning that there can be more than one edge connecting the same pair of vertices, and an edge can connect a vertex to itself. For example, a graph that represents the chemical bonds between different atoms is a pseudograph, because there can be more than one bond between the same pair of atoms, and an atom can have a bond with itself.
- **Degree of a vertex**: The number of edges that are incident to a vertex, meaning that the number of edges that have the vertex as one of their endpoints. For example, in an undirected graph, the degree of a vertex is the number of vertices that are adjacent to it, and in a directed graph, the degree of a vertex is the sum of its in-degree (the number of edges that enter the vertex) and its out-degree (the number of edges that leave the vertex).
- **Path**: A sequence of vertices and edges that connects two vertices in a graph, meaning that there is an edge between every pair of consecutive vertices in the sequence. For example, in a graph that represents the roads between different cities, a path is a sequence of cities and roads that can be traveled from one city to another.
- **Cycle**: A path that starts and ends at the same vertex, meaning that there is an edge between the first and the last vertex in the sequence. For example, in a graph that represents the roads between different cities, a cycle is a sequence of cities and roads that can be traveled from one city to another and back to the same city.
- **Connected graph**: A graph where there is a path between any pair of vertices, meaning that every vertex can be reached from any other vertex by following some edges. For example, a graph that represents the roads between different cities is connected if there is a road that connects every pair of cities.
- **Disconnected graph**: A graph where there is not a path between some pair of vertices, meaning that some vertices cannot be reached from some other vertices by following any edges. For example, a graph that represents the roads between different cities is disconnected if there is a pair of cities that are not connected by any road.
- **Component**: A subgraph of a graph that is connected, meaning that it is a subset of vertices and edges that form a connected graph. For example, in a graph that represents the

