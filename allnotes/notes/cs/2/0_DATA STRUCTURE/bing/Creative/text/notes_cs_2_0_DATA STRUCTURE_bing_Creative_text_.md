

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



### Basic Terminology

- **Data**: Data is a collection of facts and figures that can be processed to produce meaningful information. Data can be of different types, such as numerical, textual, audio, video, etc.
- **Data Structure**: Data structure is a way of organizing and storing data in a computer memory, so that it can be accessed and modified efficiently. Data structures can be classified into two categories: built-in data structures and user-defined data structures.
- **Built-in Data Structures**: Built-in data structures are the ones that are predefined and supported by the programming language, such as arrays, strings, structures, unions, etc. in C language. They have fixed size and layout in the memory.
- **User-defined Data Structures**: User-defined data structures are the ones that are created by the programmer using the built-in data structures or other user-defined data structures, such as stacks, queues, lists, trees, graphs, etc. They have variable size and layout in the memory.
- **Algorithm**: Algorithm is a finite set of instructions or steps that defines a logical process to solve a problem. An algorithm should have the following characteristics:
  - It should have a clear and unambiguous definition.
  - It should have one or more inputs and one or more outputs.
  - It should be finite, i.e., it should terminate after a finite number of steps.
  - It should be effective, i.e., it should perform the required operations in a reasonable amount of time and space.
- **Efficiency of an Algorithm**: Efficiency of an algorithm is a measure of how well it performs in terms of time and space. Time efficiency refers to the amount of time required by the algorithm to execute and produce the output. Space efficiency refers to the amount of memory or storage required by the algorithm to execute and produce the output. The efficiency of an algorithm depends on the size and nature of the input data, the hardware and software environment, and the design and implementation of the algorithm.
- **Time and Space Complexity**: Time and space complexity are the functions that describe the growth of time and space requirements of an algorithm as the input size increases. They are used to compare and analyze the performance of different algorithms for the same problem. Time and space complexity are usually expressed using asymptotic notations, such as Big Oh, Big Theta and Big Omega.
- **Asymptotic Notations**: Asymptotic notations are mathematical tools that are used to represent the time and space complexity of an algorithm in a simplified and concise way. They are based on the concept of limiting behavior, i.e., how the complexity behaves as the input size approaches infinity. The most common asymptotic notations are:
  - **Big Oh (O)**: Big Oh notation represents the upper bound or the worst case complexity of an algorithm. It means that the complexity of the algorithm is at most a constant multiple of the given function. For example, if the time complexity of an algorithm is O(n^2), it means that the algorithm takes at most c*n^2 time units to execute, where c is some constant.
  - **Big Theta (Θ)**: Big Theta notation represents the tight bound or the average case complexity of an algorithm. It means that the complexity of the algorithm is both upper and lower bounded by a constant multiple of the given function. For example, if the time complexity of an algorithm is Θ(n^2), it means that the algorithm takes at least c1*n^2 and at most c2*n^2 time units to execute, where c1 and c2 are some constants.
  - **Big Omega (Ω)**: Big Omega notation represents the lower bound or the best case complexity of an algorithm. It means that the complexity of the algorithm is at least a constant multiple of the given function. For example, if the time complexity of an algorithm is Ω(n^2), it means that the algorithm takes at least c*n^2 time units to execute, where c is some constant.
- **Time-Space Trade-off**: Time-space trade-off is a concept that describes the relationship between the time and space complexity of an algorithm. It means that sometimes we can improve the time efficiency of an algorithm by using more space, or vice versa. For example, we can use a hash table to store and retrieve data in O(1) time, but it requires more space than a linked list, which takes O(n) time to search for an element.
- **Abstract Data Type (ADT)**: Abstract data type is a logical concept that defines a set of data and the operations that can be performed on the data, without specifying the physical implementation or representation of the data. ADT is an abstraction that hides the details of how the data is stored and manipulated, and provides a clear



### Elementary Data Organization

- Data is the basic unit of information that can be processed by a computer. Data can be of different types, such as numbers, characters, strings, images, etc.
- Data organization is the way of arranging and storing data in a computer system, such as in files, databases, arrays, lists, etc. Data organization affects the efficiency and performance of data processing and retrieval.
- Built-in data types are the data types that are predefined and supported by a programming language, such as C. Examples of built-in data types in C are int, char, float, double, etc.
- Algorithm is a finite set of instructions or rules that defines a logical sequence of steps to solve a problem or perform a task. An algorithm must have the following properties:
  - Finiteness: An algorithm must terminate after a finite number of steps.
  - Definiteness: Each step of an algorithm must be precisely defined and unambiguous.
  - Input: An algorithm may take zero or more inputs as the initial data for the problem.
  - Output: An algorithm must produce one or more outputs as the solution for the problem.
  - Effectiveness: Each step of an algorithm must be simple and feasible to execute by a computer.
- Efficiency of an algorithm is a measure of how well an algorithm uses the available resources, such as time and space, to solve a problem or perform a task. Efficiency of an algorithm can be analyzed by using the following concepts:
  - Time complexity: The time complexity of an algorithm is the amount of time required by the algorithm to complete its execution for a given input size. Time complexity is usually expressed as a function of the input size, denoted by n. For example, the time complexity of a linear search algorithm is O(n), which means that the algorithm takes linear time to search an element in an array of size n.
  - Space complexity: The space complexity of an algorithm is the amount of memory or space required by the algorithm to store the data and variables during its execution for a given input size. Space complexity is also expressed as a function of the input size, denoted by n. For example, the space complexity of a bubble sort algorithm is O(1), which means that the algorithm uses constant space to sort an array of size n.
- Asymptotic notations are mathematical tools that are used to describe the behavior of an algorithm in terms of its time and space complexity as the input size grows indefinitely. The most common asymptotic notations are:
  - Big Oh notation: The Big Oh notation, denoted by O(f(n)), represents the upper bound or the worst case scenario of the time or space complexity of an algorithm. It means that the algorithm takes at most f(n) time or space to execute for an input of size n. For example, the time complexity of a binary search algorithm is O(log n), which means that the algorithm takes at most logarithmic time to search an element in a sorted array of size n.
  - Big Theta notation: The Big Theta notation, denoted by Θ(f(n)), represents the tight bound or the average case scenario of the time or space complexity of an algorithm. It means that the algorithm takes exactly f(n) time or space to execute for an input of size n. For example, the time complexity of a merge sort algorithm is Θ(n log n), which means that the algorithm takes exactly linearithmic time to sort an array of size n.
  - Big Omega notation: The Big Omega notation, denoted by Ω(f(n)), represents the lower bound or the best case scenario of the time or space complexity of an algorithm. It means that the algorithm takes at least f(n) time or space to execute for an input of size n. For example, the time complexity of a linear search algorithm is Ω(1), which means that the algorithm takes at least constant time to search an element in an array of size n.
- Time-space trade-off is a concept that describes the relationship between the time and space complexity of an algorithm. It means that by increasing the space complexity, the time complexity can be reduced, and vice versa. For example, by using a hash table, the time complexity of searching an element can be reduced from O(n) to O(1), but the space complexity increases from O(1) to O(n).
- Abstract data type (ADT) is a logical representation of a data type that defines the data and the operations that can be performed on the data, without specifying the implementation details. An ADT is an abstraction that hides the complexity and details of the data organization and manipulation from the user. An ADT can be implemented by using different data structures, such as arrays, lists, trees, etc. Examples of ADTs



### Built in Data Types in C

- Data types are declarations for variables that determine the type and size of information the variable will store.
- C supports four basic data types: integer, floating point, character and void .
- Integer data types store whole numbers, without decimals, such as 42, -7, 0, etc. They can be signed (positive or negative) or unsigned (only positive). The size and range of integer data types depend on the compiler and the system, but usually they are 2 or 4 bytes .
- Floating point data types store real numbers, with decimals, such as 3.14, -0.5, 1.0e-6, etc. They can be single precision (float) or double precision (double). The size and range of floating point data types also depend on the compiler and the system, but usually they are 4 or 8 bytes .
- Character data types store single characters, such as 'a', 'B', '9', etc. They are represented by ASCII codes, which are integer values. The size of character data types is 1 byte, and the range is from 0 to 255 .
- Void data type means no value. It is used to specify the return type of a function that does not return any value, or to declare a pointer that can point to any type of data .
- C also supports derived data types, such as arrays, pointers, structures, unions and enumerations, which are built from the basic data types  .
- Data types are important for ensuring the correct and efficient use of memory and operations on variables  .



### Algorithm for the notes of the Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT) in the subject of DATA STRUCTURE

- An **algorithm** is a step-by-step procedure, which defines a set of instructions to be executed in a certain order to get the desired output.
- Algorithms are generally created independent of underlying languages, i.e. an algorithm can be implemented in more than one programming language.
- An algorithm can be represented using **pseudocode** or **flowchart**.
- The **efficiency** of an algorithm is measured by its **time complexity** and **space complexity**.
- **Time complexity** is the amount of time required by an algorithm to run to completion.
- **Space complexity** is the amount of memory required by an algorithm to run to completion.
- **Asymptotic notations** are mathematical tools to express the growth of time and space complexity of an algorithm as the input size increases.
- The most common asymptotic notations are **Big Oh**, **Big Theta** and **Big Omega**.
- **Big Oh** notation gives the **upper bound** of the growth rate of an algorithm, i.e. the maximum time or space required by an algorithm for any input size.
- **Big Theta** notation gives the **tight bound** of the growth rate of an algorithm, i.e. the average time or space required by an algorithm for any input size.
- **Big Omega** notation gives the **lower bound** of the growth rate of an algorithm, i.e. the minimum time or space required by an algorithm for any input size.
- **Time-space trade-off** is a concept that involves balancing the time and space complexity of an algorithm, i.e. reducing one may increase the other and vice versa.
- An **abstract data type (ADT)** is a logical description of how we view the data and the operations that are allowed without regard to how they will be implemented.
- ADTs hide the details of implementation and allow us to focus on the functionality and behavior of the data.
- ADTs can be implemented using different **data structures**, such as arrays, linked lists, stacks, queues, trees, graphs, etc.
- **Data structures** are named locations that can be used to store and organize data.
- **Built-in data types** in C are the basic data types that are predefined and supported by the C compiler, such as int, char, float, double, etc.
- **Elementary data organization** refers to the way data is stored and accessed in memory, such as sequential, linked, indexed, etc.



### Efficiency of an Algorithm

- The efficiency of an algorithm is a property of an algorithm that relates to the amount of computational resources used by the algorithm.
- The computational resources can be time, memory, disk space, bandwidth, etc.
- The efficiency of an algorithm can be measured by analyzing its resource usage for different input sizes.
- The efficiency of an algorithm can be expressed by using asymptotic notations, such as Big Oh, Big Theta and Big Omega, which describe the upper bound, tight bound and lower bound of the resource usage, respectively .
- The efficiency of an algorithm can also be affected by the trade-off between time and space, which means that an algorithm can use more memory to reduce the running time, or vice versa .
- The efficiency of an algorithm is important for designing and implementing abstract data types (ADT), which are data structures that hide the implementation details and provide a set of operations to manipulate the data.



### Time and Space Complexity

- Time complexity is a measure of how much time an algorithm takes to execute as a function of the input size.
- Space complexity is a measure of how much memory an algorithm uses as a function of the input size.
- Both time and space complexity are important factors to consider when designing and analyzing algorithms, as they affect the performance and scalability of the algorithm.
- Time and space complexity can be expressed using asymptotic notations, which are mathematical tools to describe the behavior of functions in the limit of large inputs.
- The most common asymptotic notations are:
  - Big Oh (O): It gives the upper bound of the function, meaning that the function is always less than or equal to some constant times O.
  - Big Theta (Θ): It gives the tight bound of the function, meaning that the function is always between some constant times Θ.
  - Big Omega (Ω): It gives the lower bound of the function, meaning that the function is always greater than or equal to some constant times Ω.
- For example, if the time complexity of an algorithm is O(n^2), it means that the algorithm takes at most some constant times n^2 steps to execute, where n is the input size. Similarly, if the space complexity of an algorithm is Θ(n), it means that the algorithm uses exactly some constant times n units of memory, where n is the input size.
- Time-space trade-off is a concept that describes the trade-off between the time and space complexity of an algorithm. Sometimes, an algorithm can be made faster by using more memory, or vice versa. For example, sorting an array can be done in O(n log n) time and O(1) space using merge sort, or in O(n) time and O(n) space using counting sort.
- Abstract data types (ADTs) are data types that are defined by their operations and properties, rather than by their implementation. ADTs hide the details of how the data is stored and manipulated, and provide a clear and consistent interface for the users. ADTs are useful for designing and analyzing algorithms, as they allow us to focus on the logic and functionality of the algorithm, rather than the low-level details of the data structure. Some examples of ADTs are stacks, queues, lists, trees, graphs, etc.



### Asymptotic notations: Big Oh, Big Theta and Big Omega

- Asymptotic notations are mathematical tools that help us to analyze the efficiency of an algorithm in terms of its time and space complexity.
- They allow us to compare the performance of different algorithms for the same problem, and to ignore the constant factors and lower-order terms that are insignificant for large inputs.
- There are three main asymptotic notations: Big Oh, Big Theta and Big Omega. They are defined as follows:

#### Big Oh notation
- Big Oh notation, denoted by O(f(n)), represents the upper bound of the time or space complexity of an algorithm. It means that the algorithm will take at most O(f(n)) time or space to execute for any input of size n.
- For example, if an algorithm has a time complexity of O(n^2 + n), it means that the algorithm will take at most n^2 + n steps to complete for any input of size n. We can ignore the lower-order term n and the constant factor 1, and say that the algorithm is O(n^2) in the worst case.
- To prove that an algorithm is O(f(n)), we need to find a constant c and a value n0 such that for all n >= n0, the algorithm takes at most c * f(n) steps to complete.

#### Big Theta notation
- Big Theta notation, denoted by Θ(f(n)), represents the tight bound of the time or space complexity of an algorithm. It means that the algorithm will take exactly Θ(f(n)) time or space to execute for any input of size n, up to a constant factor.
- For example, if an algorithm has a time complexity of Θ(n^2), it means that the algorithm will take exactly n^2 steps to complete for any input of size n, up to a constant factor. We cannot ignore the lower-order terms or the constant factors, and say that the algorithm is Θ(n^2) in the best, average and worst case.
- To prove that an algorithm is Θ(f(n)), we need to find two constants c1 and c2 and a value n0 such that for all n >= n0, the algorithm takes at least c1 * f(n) and at most c2 * f(n) steps to complete.

#### Big Omega notation
- Big Omega notation, denoted by Ω(f(n)), represents the lower bound of the time or space complexity of an algorithm. It means that the algorithm will take at least Ω(f(n)) time or space to execute for any input of size n.
- For example, if an algorithm has a time complexity of Ω(n^2), it means that the algorithm will take at least n^2 steps to complete for any input of size n. We can ignore the lower-order terms and the constant factors, and say that the algorithm is Ω(n^2) in the best case.
- To prove that an algorithm is Ω(f(n)), we need to find a constant c and a value n0 such that for all n >= n0, the algorithm takes at least c * f(n) steps to complete.



### Time-Space trade-off

- Time-space trade-off is a concept in computer science that refers to the balance between the running time and the memory usage of an algorithm or a program.
- Generally, there is a trade-off between time and space, meaning that faster algorithms or programs tend to use more memory, and slower algorithms or programs tend to use less memory.
- For example, sorting an array of numbers can be done in different ways, such as bubble sort, insertion sort, merge sort, quick sort, etc. Each of these sorting algorithms has a different time complexity and space complexity, which measure how fast and how much memory they use, respectively.
- Bubble sort and insertion sort are simple algorithms that have a time complexity of O(n^2), where n is the size of the array, but they only use O(1) extra space, meaning that they do not need any additional memory apart from the input array.
- Merge sort and quick sort are more complex algorithms that have a time complexity of O(n log n), which is faster than O(n^2), but they use O(n) extra space, meaning that they need to create a new array of the same size as the input array to store the intermediate results.
- Therefore, there is a trade-off between time and space when choosing a sorting algorithm. Depending on the situation, one might prefer a faster algorithm that uses more memory, or a slower algorithm that uses less memory.
- Time-space trade-off is not always a fixed or linear relationship. Sometimes, there might be no trade-off, meaning that an algorithm or a program can be both fast and memory-efficient. For example, binary search is an algorithm that can find an element in a sorted array in O(log n) time and O(1) space, which is optimal for both time and space.
- Sometimes, there might be a non-linear trade-off, meaning that an algorithm or a program can have different levels of trade-off depending on the input size or the parameter values. For example, dynamic programming is a technique that can solve some optimization problems by storing the intermediate results in a table or an array, which can reduce the time complexity but increase the space complexity. However, the trade-off between time and space can vary depending on how large the table or the array is, and how often it is accessed or updated.



### Abstract Data Types (ADT)

- An abstract data type (ADT) is a mathematical model of a data structure that specifies the type of data stored, the operations supported on them, and the behaviour of those operations.
- An ADT does not specify how the data structure is implemented, only the interface that it provides to the user or the programmer.
- An ADT encapsulates the data and the operations on the data, hiding the details of the implementation from the user or the programmer.
- An ADT can be implemented using different data structures, such as arrays, linked lists, trees, etc.
- An ADT provides a level of abstraction that allows the user or the programmer to focus on the problem-solving logic, rather than the low-level details of the data representation and manipulation.
- Examples of ADTs are stack, queue, list, set, map, etc.



## Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

- Arrays: Definition, Single and Multidimensional Arrays
  - An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
  - A single-dimensional array is an array with one dimension, or one row of elements. For example, `int a[5]` is a single-dimensional array of 5 integers.
  - A multidimensional array is an array with more than one dimension, or more than one row of elements. For example, `int b[3][4]` is a two-dimensional array of 3 rows and 4 columns of integers.
  - A multidimensional array can be visualized as a table or a matrix, where each element is identified by a pair of indices, one for the row and one for the column. For example, `b[1][2]` refers to the element in the second row and the third column of the array `b`.
  - A multidimensional array can also be seen as an array of arrays, where each element of the outer array is another array. For example, `b[1]` is an array of 4 integers, which is the second element of the array `b`.
- Representation of Arrays: Row Major Order, and Column Major Order
  - Row major order and column major order are two ways of storing multidimensional arrays in linear memory, such as RAM or disk.
  - In row major order, the elements of a multidimensional array are stored row by row, or in the order of increasing row indices. For example, the elements of the array `b` are stored as `b[0][0], b[0][1], b[0][2], b[0][3], b[1][0], b[1][1], b[1][2], b[1][3], b[2][0], b[2][1], b[2][2], b[2][3]`.
  - In column major order, the elements of a multidimensional array are stored column by column, or in the order of increasing column indices. For example, the elements of the array `b` are stored as `b[0][0], b[1][0], b[2][0], b[0][1], b[1][1], b[2][1], b[0][2], b[1][2], b[2][2], b[0][3], b[1][3], b[2][3]`.
  - The choice of row major order or column major order depends on the programming language, the compiler, and the hardware. Some languages, such as C and C++, use row major order by default, while others, such as Fortran and MATLAB, use column major order by default.
- Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array
  - The index formula is a mathematical expression that maps the indices of a multidimensional array to the linear address of the corresponding element in memory.
  - For a one-dimensional array `a` of size `n`, the index formula is `address(a[i]) = base(a) + i * size(a)`, where `base(a)` is the starting address of the array, `i` is the index of the element, and `size(a)` is the size of each element in bytes.
  - For a two-dimensional array `b` of size `m x n`, the index formula in row major order is `address(b[i][j]) = base(b) + (i * n + j) * size(b)`, where `base(b)` is the starting address of the array, `i` and `j` are the row and column indices of the element, `n` is the number of columns, and `size(b)` is the size of each element in bytes.
  - The index formula in column major order is `address(b[i][j]) = base(b) + (j * m + i) * size(b)`, where `m` is the number of rows.
  - For a three-dimensional array `



Hello, I am Sydney, your AI assistant. I can help you with your topic of Unit 2 - Arrays and Linked Lists in Data Structure. Here are some notes for you:

### Definition of Arrays
- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- An array can be single-dimensional or multi-dimensional, depending on the number of dimensions or subscripts used to specify an element.
- A single-dimensional array is a linear array, where each element is identified by a single index. For example, `A[5]` is an array of 5 elements, where `A[0]` is the first element and `A[4]` is the last element.
- A multi-dimensional array is an array of arrays, where each element is identified by a combination of indices. For example, `B[3][4]` is a two-dimensional array of 3 rows and 4 columns, where `B[0][0]` is the top-left element and `B[2][3]` is the bottom-right element.
- A three-dimensional array is an array of two-dimensional arrays, where each element is identified by three indices. For example, `C[2][3][4]` is a three-dimensional array of 2 layers, 3 rows and 4 columns, where `C[0][0][0]` is the front-top-left element and `C[1][2][3]` is the back-bottom-right element.
- A n-dimensional array is an array of (n-1)-dimensional arrays, where each element is identified by n indices. For example, `D[2][3][4][5]` is a four-dimensional array of 2 blocks, 3 layers, 4 rows and 5 columns, where `D[0][0][0][0]` is the front-top-left-most element and `D[1][2][3][4]` is the back-bottom-right-most element.

### Representation of Arrays
- Arrays can be represented in two ways: row major order and column major order.
- Row major order is a way of storing an array in memory, where the elements of a row are stored consecutively, followed by the elements of the next row, and so on. For example, the two-dimensional array `B[3][4]` can be stored in row major order as:

| B[0][0] | B[0][1] | B[0][2] | B[0][3] |
| B[1][0] | B[1][1] | B[1][2] | B[1][3] |
| B[2][0] | B[2][1] | B[2][2] | B[2][3] |

- Column major order is a way of storing an array in memory, where the elements of a column are stored consecutively, followed by the elements of the next column, and so on. For example, the two-dimensional array `B[3][4]` can be stored in column major order as:

| B[0][0] | B[1][0] | B[2][0] |
| B[0][1] | B[1][1] | B[2][1] |
| B[0][2] | B[1][2] | B[2][2] |
| B[0][3] | B[1][3] | B[2][3] |

### Derivation of Index Formulae for 1-D, 2-D, 3-D and n-D Array
- To access an element of an array, we need to calculate its address in memory, based on the base address of the array, the size of each element, and the index or indices of the element.
- For a single-dimensional array `A[n]`, the address of `A[i]` can be calculated as:

`address(A[i]) = base(A) + i * size(A)`

where `base(A)` is the base address of the array, `i` is the index of the element, and `size(A)` is the size of each element.

- For a two-dimensional array `B[m][n]`, the address of `B[i][j]` can be calculated as:

`address(B[i][j]) = base(B) + (i * n + j) * size(B)`

if the array is stored in row major order, or

`address(B[i][j]) = base(B) + (j * m + i) * size(B)`

if the array



### Single and Multidimensional Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- A single-dimensional array is an array with one dimension, meaning that it can store a fixed number of elements of the same type in a linear sequence.
- A multidimensional array is an array with more than one dimension, meaning that it can store a fixed number of elements of the same type in a rectangular or higher-dimensional grid.
- The representation of arrays depends on the order in which the elements are stored in memory. There are two common orders: row-major order and column-major order.
- In row-major order, the elements of an array are stored row by row, meaning that the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column-major order, the elements of an array are stored column by column, meaning that the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The index formulae for accessing the elements of an array depend on the order of storage and the number of dimensions. For a one-dimensional array A of size n, the index formula is:

  - A[i] = base address + i * size of element, where i is the index of the element, ranging from 0 to n-1.

- For a two-dimensional array A of size m x n, the index formulae are:

  - A[i][j] = base address + (i * n + j) * size of element, for row-major order, where i is the row index and j is the column index, ranging from 0 to m-1 and 0 to n-1, respectively.
  - A[i][j] = base address + (j * m + i) * size of element, for column-major order, where i is the row index and j is the column index, ranging from 0 to m-1 and 0 to n-1, respectively.

- For a three-dimensional array A of size l x m x n, the index formulae are:

  - A[i][j][k] = base address + (i * m * n + j * n + k) * size of element, for row-major order, where i is the first dimension index, j is the second dimension index, and k is the third dimension index, ranging from 0 to l-1, 0 to m-1, and 0 to n-1, respectively.
  - A[i][j][k] = base address + (k * m * l + j * l + i) * size of element, for column-major order, where i is the first dimension index, j is the second dimension index, and k is the third dimension index, ranging from 0 to l-1, 0 to m-1, and 0 to n-1, respectively.

- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formulae are:

  - A[i1][i2]...[in] = base address + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size of element, for row-major order, where i1, i2, ..., in are the indices of the elements, ranging from 0 to d1-1, 0 to d2-1, ..., and 0 to dn-1, respectively.
  - A[i1][i2]...[in] = base address + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * size of element, for column-major order, where i1, i2, ..., in are the indices of the elements, ranging from 0 to d1-1, 0 to d2-1, ..., and 0 to dn-1, respectively.

- Arrays are useful for storing and manipulating data that have a fixed and regular structure, such as matrices, vectors, images, etc.
- Sparse matrices are matrices that have a large number of zero elements, and only a few non-zero elements. Storing sparse matrices as regular arrays can waste a lot of memory space and computation time.
- There are different ways of representing sparse matrices, such as:

  - Triplet representation: A sparse matrix is stored as a list of triplets, where each triplet consists of the row index, the column index, and the value of a non-zero element.
  - Compressed row



### Representation of Arrays: Row Major Order, and Column Major Order

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by their indices.
- A single-dimensional array is a linear array, where each element has a unique index.
- A multi-dimensional array is an array of arrays, where each element is itself an array and has a tuple of indices.
- The representation of arrays in memory depends on the order in which the elements are stored, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, i.e., the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column major order, the elements of an array are stored column by column, i.e., the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The index formulae for accessing the elements of an array in memory depend on the order of storage, the number of dimensions, the base address, and the size of each element and dimension.
- For a one-dimensional array A of size n, the index formula is:

  - In row major order: `address(A[i]) = base(A) + i * size(A)`
  - In column major order: `address(A[i]) = base(A) + i * size(A)`

- For a two-dimensional array A of size m x n, the index formula is:

  - In row major order: `address(A[i][j]) = base(A) + (i * n + j) * size(A)`
  - In column major order: `address(A[i][j]) = base(A) + (j * m + i) * size(A)`

- For a three-dimensional array A of size l x m x n, the index formula is:

  - In row major order: `address(A[i][j][k]) = base(A) + (i * m * n + j * n + k) * size(A)`
  - In column major order: `address(A[i][j][k]) = base(A) + (k * m * l + j * l + i) * size(A)`

- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formula is:

  - In row major order: `address(A[i1][i2]...[in]) = base(A) + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size(A)`
  - In column major order: `address(A[i1][i2]...[in]) = base(A) + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * size(A)`

- The choice of row major order or column major order depends on the programming language and the application of the array. Some languages, such as C and C++, use row major order by default, while others, such as Fortran and MATLAB, use column major order by default.
- The advantage of row major order is that it is easier to access the elements of a row sequentially, which is useful for operations such as matrix multiplication, row reduction, etc.
- The advantage of column major order is that it is easier to access the elements of a column sequentially, which is useful for operations such as matrix inversion, column reduction, etc.



### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- The index formula is a mathematical expression that calculates the address of any element in an array, given its base address, size, and dimensions.
- The index formula depends on the order of storing the array elements in memory, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, i.e., the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column major order, the elements of an array are stored column by column, i.e., the elements of the first column are stored first, followed by the elements of the second column, and so on.

#### Index Formula for 1-D Array

- A 1-D array is a linear array that has only one dimension, i.e., a single row or column of elements.
- The index formula for a 1-D array in row major order is:

  - `LOC(A[i]) = BA + W * (i - LB)`

  - where LOC(A[i]) is the address of the ith element of the array A, BA is the base address of the array, W is the size of each element, i is the index of the element, and LB is the lower bound of the index.

- The index formula for a 1-D array in column major order is the same as the row major order, since there is no difference in the order of storing the elements.

#### Index Formula for 2-D Array

- A 2-D array is a rectangular array that has two dimensions, i.e., rows and columns of elements.
- The index formula for a 2-D array in row major order is:

  - `LOC(A[i][j]) = BA + W * (n * (i - LBR) + (j - LBC))`

  - where LOC(A[i][j]) is the address of the element in the ith row and jth column of the array A, BA is the base address of the array, W is the size of each element, n is the number of columns in the array, i and j are the indices of the element, and LBR and LBC are the lower bounds of the row and column indices, respectively.

- The index formula for a 2-D array in column major order is:

  - `LOC(A[i][j]) = BA + W * (m * (j - LBC) + (i - LBR))`

  - where LOC(A[i][j]) is the address of the element in the ith row and jth column of the array A, BA is the base address of the array, W is the size of each element, m is the number of rows in the array, i and j are the indices of the element, and LBR and LBC are the lower bounds of the row and column indices, respectively.

#### Index Formula for 3-D Array

- A 3-D array is a cuboidal array that has three dimensions, i.e., rows, columns, and layers of elements.
- The index formula for a 3-D array in row major order is:

  - `LOC(A[i][j][k]) = BA + W * (n * p * (i - LBR) + p * (j - LBC) + (k - LBL))`

  - where LOC(A[i][j][k]) is the address of the element in the ith row, jth column, and kth layer of the array A, BA is the base address of the array, W is the size of each element, n and p are the number of columns and layers in the array, i, j, and k are the indices of the element, and LBR, LBC, and LBL are the lower bounds of the row, column, and layer indices, respectively.

- The index formula for a 3-D array in column major order is:

  - `LOC(A[i][j][k]) = BA + W * (m * p * (k - LBL) + m * (j - LBC) + (i - LBR))`

  - where LOC(A[i][j][k]) is the address of the element in the ith row, jth column, and kth layer of the array A, BA is the base



### Application of arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- Arrays can be used to store and manipulate various kinds of data, such as numbers, characters, strings, matrices, graphs, images, etc.
- Arrays can be classified into single-dimensional and multi-dimensional arrays, depending on the number of indices required to access an element.
- Single-dimensional arrays are also called vectors or one-dimensional arrays. They have only one index that ranges from 0 to n-1, where n is the size of the array.
- Multi-dimensional arrays are also called matrices or n-dimensional arrays. They have more than one index that ranges from 0 to n-1, where n is the size of each dimension of the array.
- For example, a two-dimensional array can be represented as a table of rows and columns, where each element has two indices: row and column. A three-dimensional array can be represented as a cube of layers, where each element has three indices: layer, row and column.
- The representation of arrays in memory can be done in two ways: row major order and column major order.
- Row major order is a method of storing an array in memory where the elements of a row are stored consecutively, followed by the elements of the next row, and so on. For example, the two-dimensional array A[2][3] can be stored in row major order as follows:

| Memory Location | Element |
| --------------- | ------- |
| 100             | A[0][0] |
| 101             | A[0][1] |
| 102             | A[0][2] |
| 103             | A[1][0] |
| 104             | A[1][1] |
| 105             | A[1][2] |

- Column major order is a method of storing an array in memory where the elements of a column are stored consecutively, followed by the elements of the next column, and so on. For example, the two-dimensional array A[2][3] can be stored in column major order as follows:

| Memory Location | Element |
| --------------- | ------- |
| 100             | A[0][0] |
| 101             | A[1][0] |
| 102             | A[0][1] |
| 103             | A[1][1] |
| 104             | A[0][2] |
| 105             | A[1][2] |

- The index formulae for 1-D, 2-D, 3-D and n-D arrays are used to calculate the memory location of an element in an array, given its indices and the base address of the array.
- The index formula for a 1-D array A[n] in row major order is:

  - LOC(A[i]) = BA + i * size
  - where LOC(A[i]) is the memory location of A[i], BA is the base address of the array, i is the index of the element, and size is the size of each element in bytes.

- The index formula for a 2-D array A[m][n] in row major order is:

  - LOC(A[i][j]) = BA + (i * n + j) * size
  - where LOC(A[i][j]) is the memory location of A[i][j], BA is the base address of the array, i and j are the indices of the element, n is the number of columns in the array, and size is the size of each element in bytes.

- The index formula for a 2-D array A[m][n] in column major order is:

  - LOC(A[i][j]) = BA + (j * m + i) * size
  - where LOC(A[i][j]) is the memory location of A[i][j], BA is the base address of the array, i and j are the indices of the element, m is the number of rows in the array, and size is the size of each element in bytes.

- The index formula for a 3-D array A[l][m][n] in row major order is:

  - LOC(A[i][j][k]) = BA + (i * m * n + j * n + k) * size
  - where LOC(A[i][j][k]) is the memory location of A[i][j][k], BA is the base address of the array, i, j and k are the indices of the element, m and n are the number of rows and columns in each layer of the array, and size is the size of each element in



### Sparse Matrices and their representations

- A sparse matrix is a matrix that has a large number of zero elements and a small number of non-zero elements.
- Sparse matrices arise in many applications, such as finite element methods, graph theory, network analysis, image processing, etc.
- Storing and manipulating sparse matrices efficiently is important for saving space and time.
- There are different ways of representing sparse matrices, depending on the structure and sparsity pattern of the matrix.
- Some common representations are:

  - **Coordinate list (COO)**: This representation stores the row index, column index, and value of each non-zero element in three separate arrays. The order of the elements can be arbitrary. This representation is simple and easy to construct, but it does not allow fast access or modification of the matrix elements.
  - **Compressed sparse row (CSR)**: This representation stores the non-zero elements of each row in a contiguous array, along with an array of column indices and an array of row pointers. The row pointers indicate the starting and ending positions of each row in the value array. This representation allows fast row-wise operations and matrix-vector multiplication, but it does not allow fast column-wise operations or modification of the matrix elements.
  - **Compressed sparse column (CSC)**: This representation is similar to CSR, but it stores the non-zero elements of each column in a contiguous array, along with an array of row indices and an array of column pointers. The column pointers indicate the starting and ending positions of each column in the value array. This representation allows fast column-wise operations and matrix-vector multiplication, but it does not allow fast row-wise operations or modification of the matrix elements.
  - **Dictionary of keys (DOK)**: This representation stores the non-zero elements of the matrix in a dictionary, where the keys are tuples of row and column indices and the values are the element values. This representation allows fast access and modification of the matrix elements, but it does not allow fast matrix operations or storage efficiency.
  - **Block compressed row (BCR)**: This representation divides the matrix into blocks of fixed size, and stores each block in a CSR format. This representation can reduce the storage space and improve the performance of matrix operations, especially for matrices with regular block structures. However, it requires additional parameters to specify the block size and shape.



### Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

- A linked list is a linear data structure that stores a collection of data elements dynamically  .
- Nodes represent those data elements, and links or pointers connect each node  .
- Each node consists of two fields, the information stored in a linked list and a pointer that stores the address of its next node  .
- A linked list is not stored at contiguous memory locations, but by logical links that are stored as part of the data in the structure itself  .
- A linked list can be implemented using arrays or pointers  .
- Array implementation of a linked list involves storing the data and the next index of each node in an array  .
- Pointer implementation of a linked list involves storing the data and the next pointer of each node in a dynamic memory allocation  .
- A singly linked list is a type of linked list where each node has only one pointer to the next node  .
- A doubly linked list is a type of linked list where each node has two pointers, one to the next node and one to the previous node  .
- A circularly linked list is a type of linked list where the last node points to the first node, forming a loop  .
- Operations on a linked list include insertion, deletion, traversal, polynomial representation and addition, subtraction and multiplication of single variable and two variables polynomial  .
- Insertion operation on a linked list involves adding a new node at a specified position in the list  .
- Deletion operation on a linked list involves removing an existing node from a specified position in the list  .
- Traversal operation on a linked list involves visiting each node in the list and performing some action on the data  .
- Polynomial representation using a linked list involves storing the coefficients and exponents of each term of a polynomial in a node of the list  .
- Polynomial addition, subtraction and multiplication using a linked list involve performing the corresponding arithmetic operations on the coefficients and exponents of each term of the polynomials and storing the result in a new linked list  .



## Unit 3 - Searching and Sorting

### Concept of Searching
- Searching is the process of finding a particular element or record in a collection of data.
- Searching is often performed on a sorted or indexed data structure to improve the efficiency and accuracy of the search.
- Searching can be classified into two types: linear search and binary search.

### Sequential Search
- Sequential search is a linear search technique that scans each element of the data structure one by one until the target element is found or the end of the data structure is reached.
- Sequential search is also known as linear search or brute-force search.
- Sequential search is simple and easy to implement, but it is inefficient and slow for large data sets.
- The time complexity of sequential search is O(n), where n is the number of elements in the data structure.

### Index Sequential Search
- Index sequential search is an improvement over sequential search that uses an index to speed up the search process.
- An index is a separate data structure that stores the key values and the corresponding locations of some or all elements in the data structure.
- Index sequential search first searches the index to find the range of locations where the target element may be present, and then performs a sequential search within that range.
- Index sequential search reduces the number of comparisons and accesses to the data structure, but it requires extra space and time to create and maintain the index.
- The time complexity of index sequential search depends on the size and structure of the index, but it is generally better than O(n).

### Binary Search
- Binary search is a divide-and-conquer technique that searches a sorted data structure by repeatedly dividing the search range into two halves and comparing the target element with the middle element of the current range.
- Binary search discards the half of the range that does not contain the target element and continues the search on the remaining half until the target element is found or the range becomes empty.
- Binary search is efficient and fast for large and sorted data sets, but it requires the data structure to be sorted and random access to be possible.
- The time complexity of binary search is O(log n), where n is the number of elements in the data structure.

### Concept of Hashing
- Hashing is a technique that maps a large and heterogeneous set of keys to a smaller and homogeneous set of values, called hash values or hash codes.
- Hashing is used to implement efficient and compact data structures, such as hash tables, that allow fast insertion, deletion, and retrieval of elements based on their keys.
- Hashing uses a hash function, which is a mathematical function that takes a key as input and returns a hash value as output.
- A good hash function should be easy to compute, uniform, and consistent, meaning that it should distribute the keys evenly over the hash values, and always return the same hash value for the same key.

### Collision Resolution Techniques used in Hashing
- A collision occurs when two or more keys are mapped to the same hash value by the hash function.
- Collisions reduce the performance and accuracy of hashing, and they need to be resolved by some techniques.
- Some common collision resolution techniques are:

  - Chaining: In chaining, each hash value is associated with a linked list of elements that have the same hash value. To insert, delete, or retrieve an element, the hash function is used to find the corresponding linked list, and then the linear search is performed on the list.
  - Linear Probing: In linear probing, each hash value is associated with a single element, and the elements are stored in an array. To insert an element, the hash function is used to find the initial position in the array, and if that position is occupied, the next available position is searched in a linear fashion. To delete or retrieve an element, the same process is followed, but the search stops when either the element is found or an empty position is encountered.
  - Quadratic Probing: In quadratic probing, the same idea as linear probing is used, but instead of searching the next available position in a linear fashion, a quadratic function is used to determine the next position. This reduces the clustering of elements that have similar hash values, but it may cause some positions to be skipped or revisited.
  - Double Hashing: In double hashing, two hash functions are used to find the position of an element in the array. The first hash function is used to find the initial position, and if that position is occupied, the second hash function is used to find the next position. The second hash function is applied repeatedly until an empty position is found or the array is full.

### Sorting
- Sorting is the process of arranging a collection of data in a specific order, such as ascending or descending, based on some criteria, such as numerical value, alphabetical order



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Structure. Here is the content for the topic of Concept of Searching for the notes of the Unit 3.

### Concept of Searching

- Searching is the process of finding an element in a collection of data that satisfies a given condition or matches a given value.
- Searching can be performed on different types of data structures, such as arrays, lists, trees, graphs, etc.
- Searching can be classified into two categories: linear searching and binary searching.

#### Linear Searching

- Linear searching is the simplest method of searching, where the elements are searched one by one from the beginning or the end of the data structure until the desired element is found or the end is reached.
- Linear searching can be performed on any type of data structure, whether it is sorted or unsorted, sequential or linked.
- Linear searching has a time complexity of O(n), where n is the number of elements in the data structure.

#### Binary Searching

- Binary searching is a method of searching that works on sorted data structures, where the elements are arranged in ascending or descending order.
- Binary searching uses the divide and conquer technique, where the data structure is divided into two halves at each step and the desired element is compared with the middle element of the current half.
- If the desired element is equal to the middle element, the search is successful. If the desired element is smaller than the middle element, the search continues in the left half. If the desired element is larger than the middle element, the search continues in the right half.
- Binary searching has a time complexity of O(log n), where n is the number of elements in the data structure.

#### Index Sequential Searching

- Index sequential searching is a method of searching that works on sorted data structures, where the elements are arranged in ascending or descending order.
- Index sequential searching uses an index table, which is a smaller data structure that stores the key values and the corresponding positions of some elements in the original data structure.
- Index sequential searching first searches the index table for the desired element using binary search. If the desired element is found in the index table, the search is successful. If the desired element is not found in the index table, the search continues in the original data structure using linear search in the range specified by the index table.
- Index sequential searching has a time complexity of O(log m + k), where m is the number of elements in the index table and k is the number of elements in the original data structure between two consecutive index entries.

### Concept of Hashing

- Hashing is a technique of mapping a large set of data elements to a smaller set of data elements, called hash table, using a function, called hash function.
- Hashing is used to perform fast and efficient searching, insertion and deletion operations on the data elements.
- Hashing has a time complexity of O(1), where 1 is the constant time required to compute the hash function.

#### Hash Function

- A hash function is a function that takes a data element as input and returns an integer value, called hash value or hash code, as output.
- A hash function should be simple, fast and uniform, meaning that it should distribute the data elements evenly across the hash table.
- A hash function can be designed using various methods, such as division method, multiplication method, folding method, etc.

#### Hash Table

- A hash table is a data structure that stores the data elements along with their hash values in an array, called hash array.
- A hash table has a fixed size, which is usually chosen to be a prime number or a power of two.
- A hash table uses a collision resolution technique to handle the situation when two or more data elements have the same hash value, called collision.

#### Collision Resolution Techniques

- Collision resolution techniques are methods of resolving the collisions that occur in a hash table.
- Collision resolution techniques can be classified into two categories: open addressing and chaining.

##### Open Addressing

- Open addressing is a collision resolution technique that uses the hash array itself to store the data elements that have collided.
- Open addressing uses a probe sequence, which is a sequence of positions in the hash array, to find an empty slot for the data element that has collided.
- Open addressing can be implemented using various methods, such as linear probing, quadratic probing, double hashing, etc.

##### Chaining

- Chaining is a collision resolution technique that uses a separate data structure, such as a linked list, to store the data elements that have collided.
- Chaining uses the hash array to store the pointers to the linked lists, which contain the data elements that have the same hash value.
- Chaining avoids the problem of clustering, which is the tendency of the



### Sequential search

- Sequential search is the most natural searching method. In this method, the searching begins with searching every element of the list till the required record is found.
- Sequential search is also known as linear search, as it scans the list or array linearly from the first element to the last element.
- The average number of comparisons in a sequential search is (N+1)/2 where N is the size of the list or array.
- The best case of sequential search is when the target element is the first element, and the worst case is when the target element is the last element or not present in the list or array.
- The time complexity of sequential search is O(N) in the worst case and O(1) in the best case, where N is the number of elements in the list or array.
- Sequential search is simple and easy to implement, but it is inefficient for large or unsorted lists or arrays.
- Sequential search can be performed on any type of list or array, whether it is sorted or unsorted, sequential or linked.



### Index Sequential Search

- Index sequential search is a searching technique that combines the advantages of sequential search and binary search.
- It uses an index file that contains references to some records in the main file, which is sorted in some order.
- The index file is searched first using binary search, and then the corresponding block of records in the main file is searched sequentially.
- This reduces the number of comparisons and disk accesses, as compared to sequential search or binary search alone.
- The index file can be either dense or sparse. A dense index has an entry for every record in the main file, while a sparse index has an entry for every k records, where k is a positive integer.
- The index file can also be hierarchical, where each level of the index points to another level of index or to a block of records in the main file.
- The performance of index sequential search depends on the size and structure of the index file, the distribution of the records in the main file, and the frequency of the search queries.
- The advantages of index sequential search are:
  - It is faster than sequential search or binary search alone, as it reduces the number of comparisons and disk accesses.
  - It can handle dynamic files, where records are inserted or deleted, by updating the index file accordingly.
  - It can support range queries, where records within a given range of values are retrieved, by using the index file to locate the first and last records in the range.
- The disadvantages of index sequential search are:
  - It requires extra space and time to create and maintain the index file.
  - It may become inefficient if the index file is too large or too sparse, or if the records in the main file are not evenly distributed.
  - It may not be suitable for files that are frequently updated, as the index file may need to be reorganized frequently.



### Binary Search

- Binary search is a searching algorithm that finds an element in a sorted array by repeatedly dividing the search interval in half.
- Binary search works by comparing the target value to the middle element of the array. If they are equal, the search is successful and the index of the element is returned. If the target value is less than the middle element, the search continues in the lower half of the array. If the target value is greater than the middle element, the search continues in the upper half of the array.
- Binary search has a time complexity of O(log n), where n is the number of elements in the array, because it halves the search space at each step.
- Binary search requires that the array is sorted in ascending or descending order before applying the algorithm. If the array is not sorted, binary search may fail to find the element or return a wrong index.
- Binary search can be implemented iteratively or recursively. The iterative version uses a loop and two variables to keep track of the lower and upper bounds of the search interval. The recursive version uses a function that calls itself with a smaller search interval until the base case is reached.
- Binary search can be used to solve various problems, such as finding the first or last occurrence of an element in a sorted array, finding the smallest or largest element in a rotated sorted array, finding the number of occurrences of an element in a sorted array, finding the square root of a number, etc.



### Concept of Hashing & Collision resolution Techniques used in Hashing

- Hashing is a technique of mapping a set of keys to a set of values using a hash function that assigns a unique hash value to each key.
- A hash function is a mathematical function that takes a key as input and returns a hash value as output, such that the hash value is in the range of the hash table size.
- A hash table is a data structure that stores key-value pairs in an array, where the index of each element is determined by the hash value of its key.
- Hashing is useful for fast and efficient searching, insertion and deletion of data in a large collection of items.
- Collision is a situation when two or more keys have the same hash value and map to the same slot in the hash table .
- Collision resolution is the process of handling the collisions and finding an alternative slot for the keys that cause collisions .
- There are two main types of collision resolution techniques: open hashing and closed hashing.

#### Open hashing (Separate chaining)

- This technique involves making a linked list out of the slot where the collision happened, then adding the new key to the list.
- Each slot in the hash table is a pointer to the head of the linked list that stores the keys with the same hash value.
- To search for a key, the hash function is applied to find the slot, then the linked list is traversed to find the key.
- To insert a key, the hash function is applied to find the slot, then the key is added to the front of the linked list.
- To delete a key, the hash function is applied to find the slot, then the key is removed from the linked list.
- The advantage of this technique is that it can handle any number of collisions, as long as there is enough memory to store the linked lists.
- The disadvantage of this technique is that it requires extra space for the pointers, and the performance may degrade if the linked lists become too long.

#### Closed hashing (Open addressing)

- This technique involves finding an alternative slot for the key that causes a collision, using a probe sequence that depends on the key and the hash function.
- There is no key stored outside of the hash table, therefore the size of the hash table is always greater than or equal to the number of keys.
- To search for a key, the hash function is applied to find the initial slot, then the probe sequence is followed until the key is found or an empty slot is reached.
- To insert a key, the hash function is applied to find the initial slot, then the probe sequence is followed until an empty slot is found or the table is full.
- To delete a key, the hash function is applied to find the initial slot, then the probe sequence is followed until the key is found, then the key is marked as deleted.
- The advantage of this technique is that it does not require extra space for the pointers, and the performance may be better if the load factor (the ratio of the number of keys to the table size) is low.
- The disadvantage of this technique is that it may cause clustering (the tendency of keys to cluster around certain slots), and the performance may degrade if the load factor is high.
- There are different methods of generating the probe sequence, such as linear probing, quadratic probing, double hashing, etc .



### Sorting: Insertion Sort, Selection, Bubble Sort, Quick Sort, Merge Sort, Heap Sort and Radix Sort

- Sorting is the process of arranging the elements of an array or list in a specific order, such as ascending or descending, based on a comparison operator.
- Sorting algorithms are the methods or techniques used to implement sorting in data structures.
- Sorting algorithms can be classified into different categories based on their time complexity, space complexity, stability, adaptability, recursion, and comparison.
- Some of the common types of sorting algorithms are:

  - **Insertion Sort**: This algorithm works by inserting each element of the array into its correct position in a sorted subarray. It starts with the first element as the sorted subarray and then compares the next element with the sorted subarray and inserts it in the correct position. It repeats this process until the whole array is sorted .
  - **Selection Sort**: This algorithm works by selecting the smallest or largest element of the array and swapping it with the first or last element of the array. It then repeats this process for the remaining subarray until the whole array is sorted .
  - **Bubble Sort**: This algorithm works by comparing each pair of adjacent elements of the array and swapping them if they are in the wrong order. It repeats this process until no swaps are required or the array is sorted .
  - **Quick Sort**: This algorithm works by choosing a pivot element from the array and partitioning the array into two subarrays such that all the elements less than or equal to the pivot are in the left subarray and all the elements greater than the pivot are in the right subarray. It then recursively sorts the left and right subarrays using the same method .
  - **Merge Sort**: This algorithm works by dividing the array into two halves of equal or nearly equal sizes. It then recursively sorts the two halves using the same method and merges them back together using a merge function that preserves the order of the elements .
  - **Heap Sort**: This algorithm works by building a heap data structure from the array and repeatedly removing the root element of the heap and placing it at the end of the array. It then reduces the size of the heap by one and restores the heap property by adjusting the position of the elements. It repeats this process until the heap is empty or the array is sorted .
  - **Radix Sort**: This algorithm works by sorting the elements of the array based on their individual digits or characters. It starts with the least significant digit or character and sorts the elements using a stable sorting algorithm such as counting sort. It then repeats this process for the next significant digit or character until all the digits or characters are sorted .

- Some of the advantages and disadvantages of these sorting algorithms are:

  - **Insertion Sort**: It is simple, stable, adaptive, and requires constant space. However, it is inefficient for large or nearly sorted arrays as it has a worst-case time complexity of O(n^2^) where n is the number of elements in the array .
  - **Selection Sort**: It is simple, in-place, and requires constant space. However, it is unstable, non-adaptive, and has a worst-case time complexity of O(n^2^) for any array .
  - **Bubble Sort**: It is simple, stable, adaptive, and requires constant space. However, it is inefficient for large or nearly sorted arrays as it has a worst-case time complexity of O(n^2^) where n is the number of elements in the array .
  - **Quick Sort**: It is fast, in-place, and has an average time complexity of O(n log n) where n is the number of elements in the array. However, it is unstable, non-adaptive, and has a worst-case time complexity of O(n^2^) for sorted or nearly sorted arrays. It also requires extra space for recursion .
  - **Merge Sort**: It is stable, adaptive, and has a worst-case time complexity of O(n log n) for any array. However, it is not in-place and requires extra space for merging. It also requires extra time for copying the elements back and forth between the original array and the



## Unit 4 - Graphs

- A graph is a collection of vertices (or nodes) and edges (or arcs) that connect them.
- A graph can be directed or undirected, depending on whether the edges have a direction or not.
- A graph can be weighted or unweighted, depending on whether the edges have a numerical value or not.
- A graph can be simple or complex, depending on whether it has loops (edges that connect a vertex to itself) or multiple edges (more than one edge between two vertices) or not.
- A graph can be cyclic or acyclic, depending on whether it has a path that starts and ends at the same vertex or not.
- A graph can be connected or disconnected, depending on whether there is a path between any two vertices or not.
- A graph can be complete or incomplete, depending on whether there is an edge between every pair of vertices or not.

## Data Structure for Graph Representations

- There are different ways to represent a graph in a computer, depending on the type and size of the graph and the operations that need to be performed on it.
- The most common data structures for graph representations are adjacency matrices, adjacency lists, and adjacency maps.

### Adjacency Matrices

- An adjacency matrix is a two-dimensional array of size n x n, where n is the number of vertices in the graph.
- The element at row i and column j of the matrix is 1 if there is an edge from vertex i to vertex j, and 0 otherwise.
- For an undirected graph, the adjacency matrix is symmetric, meaning that the element at row i and column j is equal to the element at row j and column i.
- For a weighted graph, the element at row i and column j of the matrix is the weight of the edge from vertex i to vertex j, and 0 if there is no edge.
- The advantage of using an adjacency matrix is that it is easy to check if there is an edge between two vertices, or to find the weight of an edge, by accessing the corresponding element of the matrix in constant time.
- The disadvantage of using an adjacency matrix is that it takes O(n^2) space, which can be wasteful if the graph is sparse (has few edges compared to the number of vertices).
- The adjacency matrix also makes it difficult to iterate over the neighbors of a vertex, as it requires scanning the entire row or column of the matrix.

### Adjacency Lists

- An adjacency list is an array of size n, where n is the number of vertices in the graph.
- The element at index i of the array is a linked list of the vertices that are adjacent to vertex i, meaning that there is an edge from vertex i to them.
- For an undirected graph, each edge appears twice in the adjacency list, once in the list of each endpoint.
- For a weighted graph, each node of the linked list also stores the weight of the edge to the adjacent vertex.
- The advantage of using an adjacency list is that it takes O(n + m) space, where m is the number of edges in the graph, which can be much less than O(n^2) if the graph is sparse.
- The adjacency list also makes it easy to iterate over the neighbors of a vertex, by traversing the corresponding linked list.
- The disadvantage of using an adjacency list is that it takes O(d) time to check if there is an edge between two vertices, or to find the weight of an edge, where d is the degree of the vertex (the number of neighbors it has).

### Adjacency Maps

- An adjacency map is an array of size n, where n is the number of vertices in the graph.
- The element at index i of the array is a map (or a hash table) that maps each vertex that is adjacent to vertex i to the weight of the edge from vertex i to it.
- For an undirected graph, each edge appears twice in the adjacency map, once in the map of each endpoint.
- The advantage of using an adjacency map is that it combines the benefits of both adjacency matrices and adjacency lists, as it takes O(n + m) space, and allows checking if there is an edge between two vertices, or finding the weight of an edge, in O(1) time on average, assuming a good hash function.
- The disadvantage of using an adjacency map is that it requires more complex implementation and may have worse performance in the worst case, depending on the hash function and the load factor of the map.

## Graph Traversal

- Graph traversal is the process of visiting all the vertices and edges of a graph in a systematic way, following some rules or criteria.
- Graph traversal can be used for various purposes, such as finding paths



Hello, I am Sydney, your AI assistant. I can help you with your topic of Terminology used with Graph for the notes of the Unit 4 - Graphs. Here is some content that you can use for your study material:

### Terminology used with Graph

- A graph is a collection of vertices (or nodes) and edges (or arcs) that connect them.
- A vertex is a point or an entity in the graph, such as a city, a person, or a computer.
- An edge is a line or a link that connects two vertices, such as a road, a friendship, or a network cable.
- A graph can be directed or undirected, depending on whether the edges have a direction or not.
- A directed edge (or arc) is an edge that has an arrow indicating the direction from one vertex to another, such as a one-way street, a follower, or a data transfer.
- An undirected edge is an edge that has no direction, such as a two-way street, a mutual friend, or a bidirectional cable.
- A graph can be weighted or unweighted, depending on whether the edges have a value or not.
- A weighted edge is an edge that has a value associated with it, such as a distance, a cost, or a bandwidth.
- An unweighted edge is an edge that has no value associated with it, such as a simple connection or a binary relation.
- A graph can be simple or complex, depending on whether it has multiple edges or loops or not.
- A simple graph is a graph that has no multiple edges or loops, such as a map, a social network, or a tree.
- A multiple edge is an edge that connects the same pair of vertices more than once, such as a parallel road, a repeated message, or a redundant cable.
- A loop is an edge that connects a vertex to itself, such as a self-loop, a reflexive relation, or a feedback circuit.
- A complex graph is a graph that has multiple edges or loops, such as a multigraph, a digraph, or a pseudograph.
- A graph can be connected or disconnected, depending on whether there is a path between any pair of vertices or not.
- A path is a sequence of edges that connects two vertices, such as a route, a chain, or a trace.
- A connected graph is a graph that has a path between any pair of vertices, such as a network, a circuit, or a cycle.
- A disconnected graph is a graph that has no path between some pair of vertices, such as a collection, a partition, or a forest.
- A graph can be cyclic or acyclic, depending on whether it has a cycle or not.
- A cycle is a path that starts and ends at the same vertex, such as a loop, a ring, or a feedback.
- A cyclic graph is a graph that has a cycle, such as a circular, a periodic, or a recurrent graph.
- An acyclic graph is a graph that has no cycle, such as a linear, a hierarchical, or a directed acyclic graph (DAG).
- A graph can be complete or incomplete, depending on whether it has all possible edges or not.
- A complete graph is a graph that has all possible edges, such that every pair of vertices is connected by an edge, such as a clique, a fully connected network, or a simplex.
- An incomplete graph is a graph that has some missing edges, such that some pair of vertices is not connected by an edge, such as a sparse, a partially connected network, or a simplex.

