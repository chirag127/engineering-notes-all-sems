

## Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT)

- Basic Terminology: 
  - Data: Data is any information that can be processed by a computer. Data can be of different types, such as numbers, characters, strings, images, etc.
  - Data Structure: Data structure is a way of organizing and storing data in a computer memory, so that it can be accessed and manipulated efficiently. Data structures can be classified into two categories: primitive and non-primitive. Primitive data structures are the basic building blocks of data, such as integers, floats, characters, etc. Non-primitive data structures are composed of primitive data structures, such as arrays, lists, stacks, queues, trees, graphs, etc.
  - Data Type: Data type is a set of values and operations that can be performed on those values. Data types can be predefined or user-defined. Predefined data types are those that are provided by the programming language, such as int, char, float, etc. User-defined data types are those that are created by the programmer, such as structures, unions, enums, etc.
  - Data Object: Data object is an instance of a data type. For example, x is a data object of type int, and s is a data object of type char.
  - Data Element: Data element is the smallest unit of data that can be accessed and manipulated independently. For example, in an array of integers, each integer is a data element.
  - Data Item: Data item is a collection of one or more data elements that are logically related. For example, in a student record, name, roll number, marks, etc. are data items.
- Elementary Data Organization: 
  - Linear Data Organization: Linear data organization is a way of storing data in a sequential manner, such that each data element has a unique successor and predecessor, except the first and last elements. For example, arrays, lists, stacks, and queues are linear data structures.
  - Non-linear Data Organization: Non-linear data organization is a way of storing data in a hierarchical or networked manner, such that each data element can have more than one successor or predecessor. For example, trees and graphs are non-linear data structures.
- Built in Data Types in C: 
  - int: int is a data type that can store integer values, such as 1, -5, 0, etc. The size of int depends on the compiler and the platform, but it is usually 2 or 4 bytes. The range of int values is from -2^(n-1) to 2^(n-1)-1, where n is the number of bits in int.
  - char: char is a data type that can store single characters, such as 'a', 'B', '*', etc. The size of char is 1 byte. The range of char values is from -128 to 127, or from 0 to 255, depending on whether it is signed or unsigned.
  - float: float is a data type that can store floating-point values, such as 3.14, -0.5, 1.0e6, etc. The size of float is 4 bytes. The range of float values is from -3.4e38 to 3.4e38, with a precision of 6 to 7 digits.
  - double: double is a data type that can store double-precision floating-point values, such as 3.14159, -1.23e-45, 6.02e23, etc. The size of double is 8 bytes. The range of double values is from -1.7e308 to 1.7e308, with a precision of 15 to 16 digits.
  - void: void is a data type that can store no value. It is used to indicate the absence of a return value in a function, or the absence of a parameter list in a function declaration.
- Algorithm: Algorithm is a finite set of instructions that can be followed to solve a problem or perform a task. An algorithm must have the following properties:
  - Input: An algorithm must have zero or more inputs, which are the data or information that are given to the algorithm.
  - Output: An algorithm must have one or more outputs, which are the data or information that are produced by the algorithm.
  - Definiteness: An algorithm must have clear and unambiguous instructions, which can be understood and executed by a human or



# Basic Terminology

- **Data**: Data is a collection of facts and figures that can be processed to produce meaningful information. Data can be of different types, such as numerical, textual, audio, video, etc.
- **Data Structure**: Data structure is a way of organizing and storing data in a computer memory, so that it can be accessed and modified efficiently. Data structures can be classified into two categories: built-in data structures and user-defined data structures.
- **Built-in Data Structures**: Built-in data structures are the data types that are predefined and supported by the programming language, such as arrays, strings, structures, unions, etc. in C language. They have fixed memory size and operations.
- **User-defined Data Structures**: User-defined data structures are the data types that are defined by the programmer using the built-in data structures or other user-defined data structures, such as stacks, queues, linked lists, trees, graphs, etc. They have variable memory size and operations.
- **Algorithm**: Algorithm is a finite set of instructions or logic, written in order, to accomplish a certain predefined task. An algorithm is not the complete code or program, it is just the core logic of a problem, which can be expressed in any programming language.
- **Efficiency of an Algorithm**: Efficiency of an algorithm is a measure of how well it performs in terms of time and space complexity. Time complexity is the amount of time required by an algorithm to execute for a given input size. Space complexity is the amount of memory required by an algorithm to execute for a given input size.
- **Time and Space Complexity**: Time and space complexity are the two parameters that are used to analyze the performance of an algorithm. They are expressed as functions of the input size, denoted by n. For example, if an algorithm takes O(n) time and O(1) space, it means that the time required by the algorithm is proportional to the input size, and the space required by the algorithm is constant, irrespective of the input size.
- **Asymptotic Notations**: Asymptotic notations are the mathematical tools that are used to describe the behavior of an algorithm in terms of its time and space complexity, as the input size grows towards infinity. They are also used to compare the efficiency of different algorithms for the same problem. The most common asymptotic notations are: Big Oh, Big Theta and Big Omega.
- **Big Oh Notation**: Big Oh notation, denoted by O, is used to give the upper bound of the time or space complexity of an algorithm. It means that the algorithm will take at most O(f(n)) time or space, where f(n) is some function of n. For example, if an algorithm takes O(n^2) time, it means that the time required by the algorithm is at most proportional to the square of the input size.
- **Big Theta Notation**: Big Theta notation, denoted by Θ, is used to give the tight bound of the time or space complexity of an algorithm. It means that the algorithm will take exactly Θ(f(n)) time or space, where f(n) is some function of n. For example, if an algorithm takes Θ(n) time, it means that the time required by the algorithm is exactly proportional to the input size.
- **Big Omega Notation**: Big Omega notation, denoted by Ω, is used to give the lower bound of the time or space complexity of an algorithm. It means that the algorithm will take at least Ω(f(n)) time or space, where f(n) is some function of n. For example, if an algorithm takes Ω(n^2) time, it means that the time required by the algorithm is at least proportional to the square of the input size.
- **Time-Space Trade-off**: Time-space trade-off is a concept that states that there is a trade-off between the time and space complexity of an algorithm. It means that by increasing the space complexity, we can reduce the time complexity, and vice versa. For example, by using a hash table, we can reduce the time complexity of searching an element from O(n) to O(1), but at the cost of increasing the space complexity from O(1) to O(n).
- **Abstract Data Type (ADT)**: Abstract data type (ADT) is a logical description of how we view the data and the operations that are allowed on the data, without considering how they are implemented. ADT is a way of hiding the implementation details from the user, and providing an interface to manipulate the data. For example, a stack is an ADT that allows us to insert and delete elements only from one end, called the top, without revealing how the stack is implemented using an array



# Elementary Data Organization

## Basic Terminology

- Data: A collection of facts or values that can be processed by a computer.
- Data structure: A way of organizing and storing data in a computer memory or disk, such that it can be accessed and modified efficiently.
- Data type: A classification of data that specifies the possible values, operations and representation of the data.
- Primitive data type: A data type that is predefined by the programming language, such as int, char, float, etc.
- Derived data type: A data type that is defined by the programmer using primitive data types or other derived data types, such as array, structure, union, etc.
- Abstract data type (ADT): A data type that is defined by a set of operations and a mathematical model, but not by its implementation. For example, stack, queue, list, etc.

## Elementary Data Organization

- Data item: A single unit of data that has a value and a type.
- Data element: A group of data items that are logically related and can be accessed by a single name. For example, a record, a structure, etc.
- Data object: A collection of data elements that share a common structure and behavior. For example, an array, a list, etc.
- Data structure: A data object that supports a set of operations that can be performed on it. For example, a stack, a queue, etc.

## Built in Data Types in C

- C is a low-level programming language that provides a set of built in data types for storing and manipulating data.
- The built in data types in C are:

  - int: An integer data type that can store whole numbers in the range of -32768 to 32767 (16 bits) or -2147483648 to 2147483647 (32 bits), depending on the compiler and the platform.
  - char: A character data type that can store a single character or a byte (8 bits) of data. It can be used to store ASCII characters, such as 'A', 'a', '0', etc.
  - float: A floating-point data type that can store real numbers with a decimal point, such as 3.14, -0.5, etc. It can store up to 6 digits of precision (32 bits).
  - double: A double-precision floating-point data type that can store real numbers with a higher precision than float. It can store up to 15 digits of precision (64 bits).
  - void: A special data type that indicates the absence of any data. It can be used to specify the return type of a function that does not return any value, or the type of a pointer that can point to any data type.

- C also allows the programmer to define derived data types using the built in data types, such as:

  - array: A collection of data items of the same type that are stored in a contiguous memory location and can be accessed by an index. For example, int a[10] declares an array of 10 integers.
  - structure: A collection of data items of different types that are grouped together under a single name. For example, struct student {int roll; char name[20]; float marks;} declares a structure that can store the information of a student.
  - union: A collection of data items of different types that share the same memory location and can be accessed by a single name. For example, union data {int i; char c; float f;} declares a union that can store an integer, a character or a float value at a time.
  - pointer: A variable that can store the address of another variable or data item. For example, int *p declares a pointer that can point to an integer variable.
  - enum: A user-defined data type that can store a set of named constants. For example, enum week {SUN, MON, TUE, WED, THU, FRI, SAT} declares an enumeration that can store the values of the days of the week.

## Algorithm

- An algorithm is a finite set of instructions or steps that can be followed to solve a problem or perform a task.
- An algorithm has the following characteristics:

  - Input: An algorithm may take zero or more inputs from the user or from another source.
  - Output: An algorithm must produce one or more outputs that are the solution to the problem or the result of the task.
  - Definiteness: An algorithm must have clear and unambiguous instructions that can be executed in a finite amount of time.
  - Finiteness: An algorithm must terminate after a finite number of steps and produce the output.
  - Effectiveness: An algorithm must be feasible and practical to implement using



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Built in Data Types in C:

# Built in Data Types in C

- C is a strongly typed language, which means that every variable must have a specific data type.
- A data type defines the size, range, and format of the data that can be stored in a variable.
- C provides several built in data types, such as int, char, float, double, etc.
- Each built in data type has a corresponding keyword, which is used to declare variables of that type.
- For example, to declare a variable named x of type int, we write:

```c
int x;
```

- The size and range of each built in data type may vary depending on the compiler and the platform, but the following table shows the typical values:

| Data Type | Keyword | Size (in bytes) | Range |
|-----------|---------|-----------------|-------|
| Integer   | int     | 4               | -2,147,483,648 to 2,147,483,647 |
| Character | char    | 1               | -128 to 127 or 0 to 255 |
| Floating point | float | 4 | 3.4E-38 to 3.4E+38 |
| Double precision floating point | double | 8 | 1.7E-308 to 1.7E+308 |

- C also allows the use of modifiers to create derived data types from the built in data types.
- Modifiers are keywords that modify the size or range of the data type.
- The most common modifiers are short, long, unsigned, and signed.
- For example, to declare a variable named y of type long int, we write:

```c
long int y;
```

- The following table shows the effect of modifiers on the size and range of the data types:

| Data Type | Modifier | Size (in bytes) | Range |
|-----------|----------|-----------------|-------|
| Integer   | short    | 2               | -32,768 to 32,767 |
| Integer   | long     | 8               | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| Integer   | unsigned | 4               | 0 to 4,294,967,295 |
| Integer   | signed   | 4               | -2,147,483,648 to 2,147,483,647 |
| Character | unsigned | 1               | 0 to 255 |
| Character | signed   | 1               | -128 to 127 |
| Floating point | long  | 8               | 3.4E-38 to 3.4E+38 |
| Double precision floating point | long | 16 | 1.7E-308 to 1.7E+308 |

- C also supports the use of constants, which are fixed values that cannot be changed during the execution of the program.
- Constants can be of any data type, and are declared using the const keyword.
- For example, to declare a constant named PI of type double, we write:

```c
const double PI = 3.14;
```

- C also provides some special data types, such as void, enum, and struct, which will be discussed later in the course.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Algorithm for the notes of the Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT) in the subject of DATA STRUCTURE.

# Algorithm

- An algorithm is a finite sequence of well-defined steps that solves a specific problem or performs a specific task.
- An algorithm can be expressed in different ways, such as natural language, pseudocode, flowchart, or programming language.
- An algorithm should have the following characteristics:
  - Input: An algorithm should have zero or more inputs that are externally supplied.
  - Output: An algorithm should have one or more outputs that are the desired results of the algorithm.
  - Definiteness: Each step of an algorithm should be clear and unambiguous.
  - Finiteness: An algorithm should terminate after a finite number of steps.
  - Effectiveness: Each step of an algorithm should be feasible and executable.
  - Correctness: An algorithm should produce the correct output for any valid input.

# Efficiency of an Algorithm

- The efficiency of an algorithm is a measure of how well it performs in terms of time and space resources.
- The time efficiency of an algorithm is the amount of time it takes to execute on a given input.
- The space efficiency of an algorithm is the amount of memory it uses to execute on a given input.
- The efficiency of an algorithm depends on the size and nature of the input, as well as the implementation and hardware of the algorithm.
- The efficiency of an algorithm can be analyzed using different methods, such as empirical analysis, theoretical analysis, or asymptotic analysis.

# Time and Space Complexity

- The time complexity of an algorithm is a function that describes how the running time of the algorithm grows as the size of the input increases.
- The space complexity of an algorithm is a function that describes how the memory usage of the algorithm grows as the size of the input increases.
- The time and space complexity of an algorithm can be expressed using different notations, such as big O, big Theta, and big Omega.

# Asymptotic Notations

- Asymptotic notations are mathematical tools that are used to compare the growth rates of different functions, especially the time and space complexity functions of algorithms.
- The most common asymptotic notations are big O, big Theta, and big Omega.
- Big O notation gives the upper bound of a function, which means it describes the worst-case scenario of the function's growth rate.
- Big Theta notation gives the tight bound of a function, which means it describes the average-case scenario of the function's growth rate.
- Big Omega notation gives the lower bound of a function, which means it describes the best-case scenario of the function's growth rate.
- For example, if f(n) = 2n^2 + 3n + 5, then we can say that:
  - f(n) is O(n^2), which means f(n) grows at most as fast as n^2.
  - f(n) is Theta(n^2), which means f(n) grows at the same rate as n^2.
  - f(n) is Omega(n), which means f(n) grows at least as fast as n.

# Time-Space Trade-off

- Time-space trade-off is a concept that describes the trade-off between the time and space efficiency of an algorithm.
- In general, there is a trade-off between the time and space efficiency of an algorithm, which means that improving one may worsen the other.
- For example, an algorithm that uses more memory may run faster than an algorithm that uses less memory, or vice versa.
- The time-space trade-off depends on the problem, the algorithm, and the implementation of the algorithm.
- The goal of designing an algorithm is to find the optimal balance between the time and space efficiency of the algorithm, which may vary depending on the requirements and constraints of the problem.

# Abstract Data Types (ADT)

- An abstract data type (ADT) is a logical model of a data type that defines the data and the operations on the data, without specifying the implementation details of the data and the operations.
- An ADT is an abstraction that hides the complexity and details of the data and the operations from the user, and provides a clear and consistent interface for the user to interact with the data and the operations.
- An ADT can be implemented using different data structures, such as arrays, linked lists, stacks,



# Efficiency of an Algorithm

- An algorithm is a finite sequence of well-defined steps that solves a problem or performs a task.
- The efficiency of an algorithm is a measure of how well it uses the available resources (such as time and space) to achieve the desired output.
- The time complexity of an algorithm is the amount of time it takes to execute as a function of the input size.
- The space complexity of an algorithm is the amount of memory it uses as a function of the input size.
- Asymptotic notations are mathematical tools that help us compare the performance of different algorithms for large input sizes.
- Big Oh notation (O) gives the upper bound of the time or space complexity of an algorithm. It means that the algorithm will not take more than O(f(n)) time or space for any input of size n, where f(n) is some function of n.
- Big Theta notation (Θ) gives the tight bound of the time or space complexity of an algorithm. It means that the algorithm will take Θ(f(n)) time or space for any input of size n, where f(n) is some function of n.
- Big Omega notation (Ω) gives the lower bound of the time or space complexity of an algorithm. It means that the algorithm will take at least Ω(f(n)) time or space for any input of size n, where f(n) is some function of n.
- Time-space trade-off is a concept that describes the trade-off between the time and space complexity of an algorithm. Sometimes, we can improve the time complexity of an algorithm by using more space, or vice versa.
- Abstract Data Types (ADT) are data types that are defined by their operations and properties, rather than by their implementation. ADT hide the details of how the data is stored and manipulated, and provide a clear and consistent interface for the users. Examples of ADT are stacks, queues, lists, trees, graphs, etc.



# Time and Space Complexity

## Basic Terminology

- Data: A collection of facts or values that can be processed by a computer.
- Data structure: A way of organizing and storing data in memory.
- Data type: A set of values and operations that can be performed on those values.
- Built-in data types: Data types that are predefined by the programming language, such as int, char, float, etc. in C.
- Algorithm: A finite sequence of well-defined steps that solves a problem or performs a task.
- Efficiency of an algorithm: A measure of how well an algorithm uses the available resources, such as time and space, to produce the desired output.

## Time Complexity

- Time complexity: The amount of time required by an algorithm to execute as a function of the input size.
- Worst-case time complexity: The maximum amount of time required by an algorithm for any input of a given size.
- Best-case time complexity: The minimum amount of time required by an algorithm for any input of a given size.
- Average-case time complexity: The expected amount of time required by an algorithm for a random input of a given size.
- Asymptotic notation: A mathematical notation that expresses the growth rate of a function as the input size approaches infinity, ignoring constant factors and lower-order terms.
- Big Oh notation: An asymptotic notation that represents the upper bound of a function, i.e., the worst-case time complexity of an algorithm. For example, O(n) means that the time complexity of an algorithm is at most proportional to n, where n is the input size.
- Big Theta notation: An asymptotic notation that represents the tight bound of a function, i.e., the exact order of growth of the time complexity of an algorithm. For example, Θ(n) means that the time complexity of an algorithm is exactly proportional to n, where n is the input size.
- Big Omega notation: An asymptotic notation that represents the lower bound of a function, i.e., the best-case time complexity of an algorithm. For example, Ω(n) means that the time complexity of an algorithm is at least proportional to n, where n is the input size.

## Space Complexity

- Space complexity: The amount of memory required by an algorithm to execute as a function of the input size.
- Worst-case space complexity: The maximum amount of memory required by an algorithm for any input of a given size.
- Best-case space complexity: The minimum amount of memory required by an algorithm for any input of a given size.
- Average-case space complexity: The expected amount of memory required by an algorithm for a random input of a given size.
- Time-space trade-off: A situation where an algorithm can be made faster by using more memory, or vice versa.

## Abstract Data Types

- Abstract data type (ADT): A data type that is defined by its behavior and operations, rather than its implementation and representation.
- ADT specification: A description of the values and operations of an ADT, without specifying how they are implemented or represented.
- ADT implementation: A concrete realization of an ADT, using a specific data structure and programming language.
- ADT examples: Stack, queue, list, tree, graph, etc. are some common ADTs that can be implemented using different data structures.



# Asymptotic notations: Big Oh, Big Theta and Big Omega

- Asymptotic notations are mathematical tools that help us analyze the efficiency of an algorithm in terms of its running time and space usage.
- They allow us to express the growth rate of a function that represents the time or space complexity of an algorithm, as the input size approaches infinity.
- They also help us compare different algorithms and choose the best one for a given problem.
- There are three common asymptotic notations: Big Oh, Big Theta and Big Omega.

## Big Oh notation

- Big Oh notation, denoted by O(f(n)), is used to describe the upper bound of a function, or the worst-case scenario of an algorithm.
- It means that the function is at most proportional to f(n), or grows slower than or equal to f(n), as n approaches infinity.
- For example, if the time complexity of an algorithm is O(n^2), it means that the algorithm takes at most n^2 steps to complete, where n is the input size.
- To find the Big Oh of a function, we can ignore the lower-order terms and the constant factors, as they become insignificant as n grows large.
- For example, 3n^2 + 5n + 2 is O(n^2), because the n^2 term dominates the other terms as n increases.

## Big Theta notation

- Big Theta notation, denoted by Θ(f(n)), is used to describe the tight bound of a function, or the average-case scenario of an algorithm.
- It means that the function is both O(f(n)) and Ω(f(n)), or grows exactly as f(n), as n approaches infinity.
- For example, if the time complexity of an algorithm is Θ(n log n), it means that the algorithm takes exactly n log n steps to complete, where n is the input size.
- To find the Big Theta of a function, we can use the same method as Big Oh, but we have to make sure that the function is bounded both above and below by f(n).
- For example, 2n^2 + 3n is Θ(n^2), because it is both O(n^2) and Ω(n^2).

## Big Omega notation

- Big Omega notation, denoted by Ω(f(n)), is used to describe the lower bound of a function, or the best-case scenario of an algorithm.
- It means that the function is at least proportional to f(n), or grows faster than or equal to f(n), as n approaches infinity.
- For example, if the time complexity of an algorithm is Ω(n), it means that the algorithm takes at least n steps to complete, where n is the input size.
- To find the Big Omega of a function, we can ignore the higher-order terms and the constant factors, as they become insignificant as n grows large.
- For example, n^3 + 2n is Ω(n^3), because the n^3 term dominates the other terms as n increases.



# Time-Space trade-off

- Time-space trade-off is a concept in computer science that refers to the balance between the running time and the memory usage of an algorithm or a program.
- Generally, there is a trade-off between time and space, meaning that faster algorithms or programs tend to use more memory, and slower algorithms or programs tend to use less memory.
- For example, an algorithm that sorts an array of numbers by creating a copy of the array and sorting it in place will use more space than an algorithm that sorts the array by swapping elements without creating a copy, but it will also be faster.
- The time-space trade-off depends on the problem, the input size, the hardware, the programming language, and the implementation of the algorithm or program.
- The goal of designing efficient algorithms or programs is to minimize both the time and the space complexity, or to find the optimal trade-off between them for a given problem and input size.
- Sometimes, there is no trade-off between time and space, meaning that an algorithm or program can be improved in both aspects without sacrificing the other. For example, using a hash table instead of a linear search can improve both the time and the space complexity of finding an element in a collection.
- Time-space trade-off can be analyzed using asymptotic notations, such as Big Oh, Big Theta, and Big Omega, which describe the upper bound, the tight bound, and the lower bound of the time or space complexity of an algorithm or program, respectively.
- Abstract data types (ADTs) are a way of defining the behavior and the operations of a data type without specifying its implementation or representation. ADTs can help to design efficient algorithms or programs by hiding the details of the data structure and allowing the programmer to focus on the logic and the functionality. ADTs can also facilitate the reuse and the abstraction of code by providing a common interface for different implementations of the same data type.



# Abstract Data Types (ADT)

- An abstract data type (ADT) is a mathematical model of a data structure that specifies the type of data stored, the operations supported on them, and the behaviour of those operations.
- An ADT does not describe how the data structure is implemented, only its functionality and interface.
- An ADT can be implemented using different data structures, such as arrays, linked lists, trees, etc.
- An ADT provides a level of abstraction that hides the details of the implementation and allows the user to focus on the problem-solving logic.
- An ADT can be defined using a specification language, such as pseudocode, that describes the syntax and semantics of the operations.
- An ADT can be classified into two categories: primitive and composite.
  - Primitive ADTs are the basic data types, such as integers, floats, characters, booleans, etc. They are usually built-in or predefined in a programming language.
  - Composite ADTs are the complex data types, such as lists, stacks, queues, sets, maps, graphs, etc. They are usually defined by the user or a library using primitive ADTs or other composite ADTs.
- Some examples of ADTs and their operations are:

  - List ADT: A list is a collection of elements that are ordered and accessible by position. Some operations on a list are: insert, delete, search, traverse, sort, etc.
  - Stack ADT: A stack is a collection of elements that follow the last-in first-out (LIFO) principle. Some operations on a stack are: push, pop, peek, isEmpty, etc.
  - Queue ADT: A queue is a collection of elements that follow the first-in first-out (FIFO) principle. Some operations on a queue are: enqueue, dequeue, front, rear, isEmpty, etc.
  - Set ADT: A set is a collection of elements that are unordered and have no duplicates. Some operations on a set are: add, remove, contains, union, intersection, difference, etc.
  - Map ADT: A map is a collection of key-value pairs that are unordered and have unique keys. Some operations on a map are: put, get, remove, containsKey, containsValue, size, etc.
  - Graph ADT: A graph is a collection of vertices and edges that represent the relationships among them. Some operations on a graph are: addVertex, addEdge, removeVertex, removeEdge, adjacent, degree, etc.



# Unit 2 - Arrays and Linked Lists

## Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- An array can be single-dimensional or multidimensional, depending on the number of dimensions or subscripts used to specify an element.
- A single-dimensional array is a linear array, where each element is identified by a single index. For example, `A[5]` is a single-dimensional array of size 5, and `A[3]` is the element at index 3.
- A multidimensional array is an array of arrays, where each element is identified by a tuple of indices. For example, `A[3][4]` is a two-dimensional array of size 3x4, and `A[2][1]` is the element at row 2 and column 1.
- The representation of arrays in memory depends on the order of storing the elements, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the elements of `A[3][4]` are stored as `A[0][0], A[0][1], A[0][2], A[0][3], A[1][0], A[1][1], A[1][2], A[1][3], A[2][0], A[2][1], A[2][2], A[2][3]`.
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the elements of `A[3][4]` are stored as `A[0][0], A[1][0], A[2][0], A[0][1], A[1][1], A[2][1], A[0][2], A[1][2], A[2][2], A[0][3], A[1][3], A[2][3]`.
- The index formulae for 1-D, 2-D, 3-D and n-D arrays are derived by using the base address, the size of each element, and the order of storing the elements.
- For a 1-D array `A[n]`, the address of `A[i]` is given by `base + i * size`, where `base` is the address of `A[0]` and `size` is the size of each element.
- For a 2-D array `A[m][n]`, the address of `A[i][j]` in row major order is given by `base + (i * n + j) * size`, and in column major order is given by `base + (j * m + i) * size`.
- For a 3-D array `A[l][m][n]`, the address of `A[i][j][k]` in row major order is given by `base + (i * m * n + j * n + k) * size`, and in column major order is given by `base + (k * m * l + j * l + i) * size`.
- For an n-D array `A[d1][d2]...[dn]`, the address of `A[i1][i2]...[in]` in row major order is given by `base + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size`, and in column major order is given by `base + (in * d1 * d2 * ... * d(n-1) + i(n-1) * d1 * d2 * ... * d(n-2) + ... + i1) * size`.
- Arrays are used to store and manipulate data in various applications, such as matrices, vectors, tables, lists, stacks, queues, etc.
- Sparse matrices are matrices that have a large number of zero elements, and storing them as arrays would waste a lot of memory space. Therefore, sparse matrices are represented using different techniques, such as linked lists, arrays of lists, coordinate lists, compressed sparse row, compressed sparse column, etc.

## Linked Lists

- A linked list is a linear data structure, where each element is a node that contains data and a pointer to the next node.
- A linked list can be implemented using either an array or a pointer.
- In array implementation, a fixed-size array is used to store the nodes, and each node has an index that



# Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Arrays: Definition, Single and Multidimensional Arrays

- An array is a collection of homogeneous elements stored in a contiguous memory location for better access and easier calculation by the system.
- An array is a data structure consisting of a collection of elements, each identified by at least one array index or key.
- An array is an assortment of similar types of data, while a list can include dissimilar data values.
- Array elements can be of any type, including an array type.
- Array types are reference types derived from the abstract base type Array.
- All arrays implement IList, and IEnumerable.
- Single-dimensional arrays also implement IList<T> and IEnumerable<T>.
- An array can be declared as follows:

```csharp
// Single-dimensional array
int[] array1 = new int[5];

// Multidimensional array
int[,] array2 = new int[3,4];

// Array of arrays (jagged array)
int[][] array3 = new int[3][];
array3[0] = new int[5];
array3[1] = new int[4];
array3[2] = new int[2];
```

- A single-dimensional array is an array with one dimension, i.e., one index or key to access the elements.
- A multidimensional array is an array with more than one dimension, i.e., multiple indices or keys to access the elements.
- A jagged array is an array of arrays, where each subarray can have a different length.



# Single and Multidimensional Arrays

## Definition

- An array is a data structure that stores a collection of elements of the same type in a contiguous block of memory.
- Each element in an array can be accessed by its index, which is a non-negative integer that represents its position in the array.
- An array can have one or more dimensions, depending on how many indices are needed to specify an element.

## Single and Multidimensional Arrays

- A single-dimensional array, or 1D array, is an array that has only one dimension, meaning that it can be represented as a row or a column of elements.
- A multidimensional array, or nD array, is an array that has more than one dimension, meaning that it can be represented as a matrix or a table of elements, or a higher-dimensional structure.
- A two-dimensional array, or 2D array, is a special case of a multidimensional array that has two dimensions, meaning that it can be represented as a matrix or a table of elements, with rows and columns.
- A three-dimensional array, or 3D array, is another special case of a multidimensional array that has three dimensions, meaning that it can be represented as a cube or a stack of matrices, with rows, columns, and layers.

## Representation of Arrays

- Arrays are stored in memory in a linear fashion, meaning that the elements are placed one after another in a sequential order.
- The way that the elements of an array are mapped to the memory locations is called the array representation or the array layout.
- There are two main ways to represent arrays in memory: row-major order and column-major order.

### Row-major order

- In row-major order, the elements of an array are stored row by row, meaning that the elements of the first row are stored first, followed by the elements of the second row, and so on.
- Row-major order is also called row-wise order or lexicographic order.
- Row-major order is the default way of representing arrays in many programming languages, such as C, C++, Java, and Python.

### Column-major order

- In column-major order, the elements of an array are stored column by column, meaning that the elements of the first column are stored first, followed by the elements of the second column, and so on.
- Column-major order is also called column-wise order or colexicographic order.
- Column-major order is the default way of representing arrays in some programming languages, such as Fortran, MATLAB, and R.

## Derivation of Index Formulae

- To access an element of an array, we need to know its index or indices, which are the numbers that specify its position in the array.
- To compute the index or indices of an element, we need to know the array representation, the array dimensions, and the array base address.
- The array base address is the memory location of the first element of the array.
- The index formulae are the mathematical expressions that relate the index or indices of an element to its memory location.

### Index formula for 1D array

- For a 1D array of size n, the index formula for row-major order is:

  - Memory location of A[i] = Base address + i * size of each element

- For a 1D array of size n, the index formula for column-major order is:

  - Memory location of A[i] = Base address + i * size of each element

- Note that the index formula for 1D array is the same for both row-major and column-major order, because there is only one dimension.

### Index formula for 2D array

- For a 2D array of size m x n, the index formula for row-major order is:

  - Memory location of A[i][j] = Base address + (i * n + j) * size of each element

- For a 2D array of size m x n, the index formula for column-major order is:

  - Memory location of A[i][j] = Base address + (j * m + i) * size of each element

- Note that the index formula for 2D array differs for row-major and column-major order, because the order of the indices matters.

### Index



# Representation of Arrays: Row Major Order, and Column Major Order

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
  - In column major order: `address(A[i][j][k]) = base(A) + (k * l * m + j * l + i) * size(A)`

- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formula is:

  - In row major order: `address(A[i1][i2]...[in]) = base(A) + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size(A)`
  - In column major order: `address(A[i1][i2]...[in]) = base(A) + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * size(A)`

- The choice of row major order or column major order depends on the programming language, the data structure, and the application of the array.
- Some advantages of row major order are:

  - It is easier to implement and understand, as it follows the natural order of reading and writing data.
  - It is more efficient for accessing rows or sub-arrays of an array, as they are stored contiguously in memory.
  - It is compatible with most programming languages, such as C, C++, Java, Python, etc.

- Some advantages of column major order are:

  - It is more efficient for accessing columns or transposed arrays, as they are stored contiguously in memory.
  - It is compatible with some programming languages, such as Fortran, MATLAB, R, etc.
  - It is more suitable for some mathematical operations, such as matrix multiplication, inversion, etc.



# Derivation of Index Formulae for 1-D, 2-D, 3-D and n-D Array

## 1-D Array

- A one-dimensional array is a linear collection of elements that are stored in contiguous memory locations.
- The index of the first element is usually 0 or 1, depending on the programming language or the implementation.
- To access any element of a 1-D array, we need to know its base address (the address of the first element), the size of each element (in bytes), and the index of the element.
- The formula for calculating the address of any element in a 1-D array is:

  - `LOC(A[i]) = Base_Address + W * (i - LB)`

  - Where:
    - `LOC(A[i])` is the address of the ith element of the array A
    - `Base_Address` is the address of the first element of the array A
    - `W` is the size of each element of the array A (in bytes)
    - `i` is the index of the element to be accessed
    - `LB` is the lower bound of the array A (usually 0 or 1)

  - For example, if the base address of an array A of 10 integers is 1000, the size of each integer is 4 bytes, and the lower bound of the array is 0, then the address of the 5th element of the array is:

    - `LOC(A[5]) = 1000 + 4 * (5 - 0) = 1020`

## 2-D Array

- A two-dimensional array is a collection of elements that are arranged in rows and columns, and are stored in row-major order or column-major order in memory.
- The index of the first row and the first column is usually 0 or 1, depending on the programming language or the implementation.
- To access any element of a 2-D array, we need to know its base address, the size of each element, the number of rows and columns, and the indices of the row and the column of the element.
- The formula for calculating the address of any element in a 2-D array in row-major order is:

  - `LOC(A[i][j]) = Base_Address + W * (N * (i - LB1) + (j - LB2))`

  - Where:
    - `LOC(A[i][j])` is the address of the element in the ith row and jth column of the array A
    - `Base_Address` is the address of the first element of the array A
    - `W` is the size of each element of the array A (in bytes)
    - `N` is the number of columns in the array A
    - `i` and `j` are the indices of the row and the column of the element to be accessed
    - `LB1` and `LB2` are the lower bounds of the rows and columns of the array A (usually 0 or 1)

  - For example, if the base address of an array A of 3 rows and 4 columns of integers is 2000, the size of each integer is 4 bytes, and the lower bounds of the rows and columns are 0, then the address of the element in the 2nd row and 3rd column of the array is:

    - `LOC(A[2][3]) = 2000 + 4 * (4 * (2 - 0) + (3 - 0)) = 2052`

- The formula for calculating the address of any element in a 2-D array in column-major order is:

  - `LOC(A[i][j]) = Base_Address + W * (M * (j - LB2) + (i - LB1))`

  - Where:
    - `LOC(A[i][j])` is the address of the element in the ith row and jth column of the array A
    - `Base_Address` is the address of the first element of the array A
    - `W` is the size of each element of the array A (in bytes)
    - `M` is the number of rows in the array A
    - `i` and `j` are the indices of the row and the column of the element to be accessed
    - `LB1` and `LB2` are the lower bounds of the rows and columns of the array A (usually 0 or



# Application of arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- Arrays can be used to store and manipulate various kinds of data, such as numbers, characters, strings, matrices, graphs, images, etc.
- Arrays can be classified into single and multidimensional arrays, depending on the number of dimensions or subscripts required to access an element.
- A single-dimensional array is a linear array, where each element is identified by a single index. For example, `A[5]` is a single-dimensional array of size 5, and `A[3]` refers to the fourth element of the array.
- A multidimensional array is an array of arrays, where each element is identified by two or more indices. For example, `B[3][4]` is a two-dimensional array of size 3 by 4, and `B[2][1]` refers to the second element of the third row of the array.
- The representation of arrays in memory depends on the order in which the elements are stored. There are two common ways of storing multidimensional arrays: row major order and column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the elements of the array `B[3][4]` are stored as `B[0][0], B[0][1], B[0][2], B[0][3], B[1][0], B[1][1], B[1][2], B[1][3], B[2][0], B[2][1], B[2][2], B[2][3]`.
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the elements of the array `B[3][4]` are stored as `B[0][0], B[1][0], B[2][0], B[0][1], B[1][1], B[2][1], B[0][2], B[1][2], B[2][2], B[0][3], B[1][3], B[2][3]`.
- The index formulae for accessing an element of an array depend on the order of storage, the base address of the array, the size of each element, and the number of dimensions. For example, the general formula for accessing an element of a n-dimensional array `A[d1][d2]...[dn]` stored in row major order is:

`LOC(A[i1][i2]...[in]) = BA + size * (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in-1 * dn + in)`

where LOC is the location of the element, BA is the base address of the array, size is the size of each element, and i1, i2, ..., in are the indices of the element.

- The application of arrays can be seen in various domains, such as:

  - Mathematics: Arrays can be used to represent and perform operations on matrices, vectors, polynomials, etc. For example, a matrix can be stored as a two-dimensional array, and matrix multiplication can be done by using nested loops and array operations.
  - Computer graphics: Arrays can be used to store and manipulate images, pixels, colors, etc. For example, an image can be stored as a two-dimensional array of pixels, and image processing techniques can be applied by using array operations.
  - Data structures: Arrays can be used to implement various data structures, such as stacks, queues, heaps, hash tables, etc. For example, a stack can be implemented as a one-dimensional array, where the top element is stored at the end of the array, and push and pop operations can be done by using array operations.
  - Algorithms: Arrays can be used to store and sort data, search for elements, perform pattern matching, etc. For example, a sorting algorithm can be implemented by using an array, where the elements are compared and swapped by using array operations.

# Sparse matrices and their representations

- A sparse matrix is a matrix that has a large number of zero elements, and only a few non-zero elements. For example, the following matrix is a sparse matrix:

```
0 0 0 0 0
0 5 0 0 0
0 0 0 2 0
0 0 0 0 0
0 0 0 0 0

```




# Sparse Matrices and their representations

- A sparse matrix is a matrix in which most of the elements are zero.
- A sparse matrix can be represented in different ways to save space and time, such as:
  - Triplet representation : A two-dimensional array with three rows, where each column stores the row index, column index and value of a non-zero element.
  - Linked representation: A linked list of nodes, where each node stores the row index, column index, value and pointer to the next node of a non-zero element.
  - Compressed sparse row (CSR) representation: Three one-dimensional arrays, where one array stores the non-zero values, one array stores the column indices of the non-zero values, and one array stores the cumulative number of non-zero values in each row.
  - Compressed sparse column (CSC) representation: Similar to CSR, but with column indices and values interchanged.
- Operations on sparse matrices, such as addition, multiplication and transpose, can be performed using the sparse representations, with different algorithms and complexities.



# Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Linked lists
- A linked list is a linear data structure that stores a collection of data elements dynamically .
- Nodes represent those data elements, and links or pointers connect each node .
- Each node consists of two fields, the information stored in a linked list and a pointer that stores the address of its next node .
- Linked lists are not stored at contiguous memory locations, unlike arrays .
- Linked lists can grow and shrink in size during execution, unlike arrays .
- Linked lists can be classified into different types based on the number and direction of links between nodes .

## Array Implementation of Singly Linked Lists
- A singly linked list is a type of linked list that has only one link or pointer for each node .
- The link points to the next node in the list, and the last node has a null pointer .
- An array implementation of a singly linked list uses a fixed-size array to store the nodes of the list .
- The array has two columns, one for the data field and one for the link field .
- The link field stores the index of the next node in the array, or -1 if there is no next node .
- The array implementation of a singly linked list has some advantages and disadvantages over the pointer implementation .
  - Advantages:
    - It is easy to access any node by its index in the array .
    - It does not require dynamic memory allocation .
  - Disadvantages:
    - It has a fixed size and cannot grow or shrink dynamically .
    - It may waste space if the array is larger than the number of nodes in the list .
    - It may not have enough space if the array is smaller than the number of nodes in the list .
    - It requires shifting of elements when inserting or deleting nodes .

## Pointer Implementation of Singly Linked Lists
- A pointer implementation of a singly linked list uses dynamic memory allocation to create nodes as needed .
- The nodes are not stored in a fixed order in memory, but are linked by pointers .
- The pointer field of each node stores the address of the next node in memory, or null if there is no next node .
- The pointer implementation of a singly linked list has some advantages and disadvantages over the array implementation .
  - Advantages:
    - It can grow and shrink dynamically according to the number of nodes in the list .
    - It does not waste space as it only allocates memory for the nodes that are needed .
    - It does not require shifting of elements when inserting or deleting nodes .
  - Disadvantages:
    - It is difficult to access any node by its index as it requires traversing the list from the beginning .
    - It requires dynamic memory allocation and deallocation, which may be costly and prone to errors .

## Doubly Linked List
- A doubly linked list is a type of linked list that has two links or pointers for each node .
- The links point to the previous and the next node in the list, and the first and the last node have null pointers for the previous and the next node respectively .
- A doubly linked list allows traversal in both directions, forward and backward .
- A doubly linked list can be implemented using arrays or pointers, similar to a singly linked list



# Unit 3 - Searching and Sorting Algorithms

## Concept of Searching
Searching is the process of finding an element or a value in a data structure, such as an array or a list. Searching algorithms are designed to check for an element or retrieve an element from any data structure where it is stored. Based on the type of operations, these algorithms are generally classified into two categories:

- Sequential Search: In this, the data structure is traversed sequentially and every element is checked. For example, linear search and interpolation search are sequential search algorithms.
- Interval Search: In this, the data structure is divided into smaller substructures and the search is performed in a specific interval. For example, binary search and exponential search are interval search algorithms.

## Concept of Hashing and Collision Resolution Techniques
Hashing is a technique of mapping a large set of data items to a smaller set of data items, called hash table, using a function called hash function. The hash function maps each data item to a unique index, called hash code or hash value, in the hash table. Hashing is useful for fast and efficient search and insertion operations.

However, sometimes two or more data items may have the same hash code, which is called a collision. Collision reduces the performance of hashing and may cause data loss. Therefore, collision resolution techniques are used to handle the collisions and store the data items properly in the hash table. Some of the common collision resolution techniques are:

- Linear Probing: In this, the next available slot in the hash table is used to store the data item that causes collision.
- Quadratic Probing: In this, a quadratic function is used to calculate the next available slot in the hash table for the data item that causes collision.
- Chaining: In this, each slot in the hash table is a linked list of data items that have the same hash code. The data item that causes collision is added to the end of the linked list.

## Concept of Sorting
Sorting is the process of arranging a set of data items in a specific order, such as ascending or descending order. Sorting algorithms are used to rearrange a given array or list of elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of the elements in the respective data structures. Sorting algorithms are important for optimizing the efficiency of other algorithms (such as search and merge algorithms) that require input data to be in sorted order.

Some of the common sorting algorithms are:

- Insertion Sort: In this, the array is divided into two parts: sorted and unsorted. The first element is considered as sorted and the rest as unsorted. The unsorted element is inserted into the correct position in the sorted part by shifting the larger elements to the right.
- Selection Sort: In this, the array is divided into two parts: sorted and unsorted. The smallest element in the unsorted part is selected and swapped with the leftmost element in the unsorted part. The sorted part is extended by one element and the unsorted part is reduced by one element.
- Bubble Sort: In this, the array is traversed from left to right and the adjacent elements are compared and swapped if they are in the wrong order. This process is repeated until no swaps are required, which means the array is sorted.
- Quick Sort: In this, a pivot element is chosen from the array and the array is partitioned into two subarrays: one with elements smaller than the pivot and one with elements larger than the pivot. The subarrays are then sorted recursively using the same algorithm.
- Merge Sort: In this, the array is divided into two halves and each half is sorted recursively using the same algorithm. The sorted halves are then merged together by comparing and merging the elements in order.
- Heap Sort: In this, the array is converted into a binary heap data structure, which is a complete binary tree that satisfies the heap property. The heap property means that the parent node is either greater than or equal to (max-heap) or less than or equal to (min-heap) its child nodes. The root node of the heap is the largest (max-heap) or the smallest (min-heap) element in the array. The root node is removed from the heap and placed at the end of the array. The heap is then adjusted to maintain the heap property and the process is repeated until the heap is empty and the array is sorted.
- Radix Sort: In this, the array is sorted based on the individual digits of the elements, starting from the least significant digit to the most significant digit. The elements



# Concept of Searching

- Searching is the process of finding a given value position in a list of values.
- It decides whether a search key is present in the data or not.
- It is the algorithmic process of finding a particular item in a collection of items.
- It can be done on internal data structure or on external data structure.
- Searching in data structure can be done by applying searching algorithms to check for or extract the desired information.
- Based on the type of search operation, searching algorithms are generally classified into two categories:
  - Sequential Search: In this, the list or array is traversed sequentially and every element is checked.
  - Interval Search: In this, the list or array is divided into smaller segments of equal size and then a search is performed in a specific interval.
- Some of the common searching algorithms are:
  - Linear Search: It is the simplest form of sequential search that checks every element of the list until a match is found or the list is exhausted.
  - Binary Search: It is a form of interval search that works on a sorted list or array and repeatedly divides the search interval in half until the key is found or the interval is empty.
  - Interpolation Search: It is an improved form of binary search that estimates the position of the key based on the first and last element of the sorted list or array and then performs a binary search in the estimated interval.
  - Hashing: It is a technique that maps a large range of keys to a smaller range of indices using a hash function and then stores the elements in an array called a hash table.
  - Index Sequential Search: It is a technique that creates an index table for a sorted list or array and then performs a binary search on the index table to find the position of the key in the original list or array.



# Sequential Search

- Sequential search is the most natural searching method. In this method, the searching begins with searching every element of the list till the required record is found.
- Sequential search is also known as linear search, as it scans the list or array linearly from the first element to the last element .
- The average number of comparisons in a sequential search is (N+1)/2 where N is the size of the list or array.
- The best case of sequential search is when the target element is the first element, and the worst case is when the target element is the last element or not present in the list or array.
- The time complexity of sequential search is O(N) in the worst case and O(1) in the best case.
- Sequential search is simple and easy to implement, but it is inefficient for large or unsorted lists or arrays.
- Sequential search can be performed on any type of list or array, whether it is sorted or unsorted, sequential or linked.

# Index Sequential Search

- Index sequential search is a searching method that uses an index file to speed up the search process.
- An index file is a file that contains some specific group or division of required records, such as the first letter of the name, the range of values, or the category of items.
- The index file is sorted according to the key field of the records, and each index entry points to the first record of the corresponding group or division in the main file.
- To perform an index sequential search, first the index file is searched using binary search or interpolation search to find the index entry that matches or precedes the target key.
- Then, the main file is searched sequentially from the record pointed by the index entry until the target record is found or the end of the group or division is reached.
- The advantage of index sequential search is that it reduces the number of comparisons and disk accesses compared to sequential search, especially for large or sorted files.
- The disadvantage of index sequential search is that it requires extra space and time to create and maintain the index file, and it may become outdated if the main file is updated frequently.
- The time complexity of index sequential search is O(log I + S) where I is the size of the index file and S is the average size of the group or division in the main file.



# Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database.
- An index file is a separate file that contains references to some records or blocks of records in the main file, based on some key values or ranges.
- The index file is much smaller than the main file, and can be searched faster using binary search or interpolation search.
- Once the index file is searched, the corresponding record or block of records in the main file can be accessed directly or sequentially, depending on the type of index.
- There are two types of index files: primary index and secondary index.
  - A primary index is a sorted index file that has one entry for each block of records in the main file. The entry contains the key value of the first record in the block, and the address of the block. The main file is also sorted by the same key field.
  - A secondary index is a sorted index file that has one entry for each record in the main file. The entry contains the key value of the record, and the address of the record. The main file can be sorted or unsorted by the key field.
- The advantages of index sequential search are:
  - It reduces the number of comparisons and disk accesses required to find a record, compared to sequential search or binary search on the main file.
  - It allows multiple keys to be used for searching, by creating different index files for different key fields.
  - It supports both exact and range queries, by using the index file to locate the first or last record that satisfies the query condition, and then scanning the main file sequentially.
- The disadvantages of index sequential search are:
  - It requires extra space and time to create and maintain the index file, especially when the main file is updated frequently.
  - It may become inefficient if the index file becomes too large or too sparse, or if the distribution of the key values changes significantly over time.



# Binary Search

- Binary search is an efficient algorithm for finding an element within a sorted array.   
- Binary search works by repeatedly dividing in half the portion of the list that could contain the element, until you've narrowed down the possible locations to just one. 
- Binary search compares the element to the middle element of the array. If they are not equal, the half in which the element cannot lie is eliminated and the search continues on the remaining half, again taking the middle element and comparing it until the element is found. 
- Binary search has a time complexity of O(log n), where n is the number of elements in the array.  
- Binary search requires that the array is sorted in ascending or descending order.  
- Binary search can be implemented using an iterative or a recursive approach.  
- Binary search is useful for building more complex algorithms in computer science, such as interpolation search, exponential search, and binary search trees. 

: Binary search algorithm - Wikipedia
: Binary search (article) | Algorithms | Khan Academy
: Binary Search - GeeksforGeeks



# Concept of Hashing & Collision resolution Techniques used in Hashing

## Hashing
- Hashing is a technique of mapping a set of keys to a set of values using a hash function.
- A hash function is a function that takes a key as input and returns an integer value, called a hash value or a hash code, as output.
- The hash value is used as an index to store the key-value pair in an array, called a hash table or a hash map.
- The hash table has a fixed size, usually a prime number, and each slot in the hash table can store one or more key-value pairs.
- The advantage of hashing is that it allows fast access to the values associated with the keys, as the hash function can compute the index in constant time.
- The disadvantage of hashing is that it may cause collisions, which occur when two or more keys have the same hash value and map to the same slot in the hash table.

## Collision resolution Techniques
- Collision resolution techniques are methods to handle the collisions in the hash table and to ensure that every key can be inserted and retrieved successfully.
- There are two main types of collision resolution techniques: open hashing and closed hashing.

### Open hashing (Separate chaining)
- Open hashing, also known as separate chaining, is a technique that uses a linked list to store the key-value pairs that have the same hash value in the same slot of the hash table.
- Each slot in the hash table is either empty or contains a pointer to the head of a linked list.
- To insert a key-value pair, the hash function is applied to the key and the hash value is used as the index to locate the slot in the hash table. Then, the key-value pair is added to the front of the linked list in that slot.
- To search for a key-value pair, the hash function is applied to the key and the hash value is used as the index to locate the slot in the hash table. Then, the linked list in that slot is traversed until the key is found or the end of the list is reached.
- The advantage of open hashing is that it can handle any number of collisions, as the linked list can grow dynamically.
- The disadvantage of open hashing is that it requires extra space for the pointers and the linked list, and it may cause long search time if the linked list is too long.

### Closed hashing (Open addressing)
- Closed hashing, also known as open addressing, is a technique that stores the key-value pairs directly in the hash table, without using any pointers or linked lists.
- Each slot in the hash table can store at most one key-value pair, and the hash table size is equal to or larger than the number of keys.
- To insert a key-value pair, the hash function is applied to the key and the hash value is used as the index to locate the slot in the hash table. If the slot is empty, the key-value pair is stored in that slot. If the slot is occupied, a different slot is probed until an empty slot is found or the entire hash table is scanned.
- To search for a key-value pair, the hash function is applied to the key and the hash value is used as the index to locate the slot in the hash table. If the slot is empty, the key is not in the hash table. If the slot is occupied, the key is compared with the key in that slot. If they match, the value is returned. If they do not match, a different slot is probed until the key is found or an empty slot is encountered.
- The advantage of closed hashing is that it does not require extra space for the pointers or the linked lists, and it may cause faster access time if the hash table is not too full.
- The disadvantage of closed hashing is that it may cause insertion failure if the hash table is full, and it may cause clustering, which occurs when many keys have the same or similar hash values and map to the same or adjacent slots in the hash table.

#### Probing methods
- Probing methods are the methods to find a different slot in the hash table when a collision occurs in closed hashing.
- There are three common probing methods: linear probing, quadratic probing, and double hashing.

##### Linear probing
- Linear probing is a probing method that uses a linear function to find the next slot in the hash table.
- The linear function is of the form: h'(k, i) = (h(k) + i) mod m, where h(k) is the original hash value, i is the probe number, and m is the hash table size.
- To



# Sorting: Insertion Sort, Selection, Bubble Sort, Quick Sort, Merge Sort, Heap Sort and Radix Sort

Sorting is the process of arranging the elements of an array or list in a specific order, such as ascending or descending, based on a comparison operator. Sorting algorithms are the methods of implementing sorting in data structures. Sorting algorithms can be classified into different categories based on their time complexity, space complexity, stability, adaptability, and recursion.

## Insertion Sort

Insertion sort is a simple and stable sorting algorithm that works by inserting each element of the array into its correct position in the sorted part of the array. The algorithm starts from the second element and compares it with the previous elements, shifting them to the right until it finds the correct position to insert the current element. The algorithm repeats this process for each element until the array is sorted. The time complexity of insertion sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted. The space complexity of insertion sort is O(1) as it only requires a constant amount of extra space.

## Selection Sort

Selection sort is a simple and unstable sorting algorithm that works by selecting the smallest or largest element of the array and swapping it with the first or last element of the unsorted part of the array. The algorithm repeats this process for each element until the array is sorted. The time complexity of selection sort is O(n^2) in all cases, as it always performs n-1 comparisons for each of the n elements. The space complexity of selection sort is O(1) as it only requires a constant amount of extra space.

## Bubble Sort

Bubble sort is a simple and stable sorting algorithm that works by repeatedly swapping the adjacent elements of the array if they are in the wrong order. The algorithm passes through the array n-1 times, where n is the number of elements, and each pass reduces the size of the unsorted part of the array by one. The algorithm stops when no swaps are performed in a pass, indicating that the array is sorted. The time complexity of bubble sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted. The space complexity of bubble sort is O(1) as it only requires a constant amount of extra space.

## Quick Sort

Quick sort is a fast and unstable sorting algorithm that works by using the divide and conquer technique. The algorithm chooses a pivot element from the array and partitions the array into two subarrays, such that all the elements less than the pivot are in the left subarray and all the elements greater than or equal to the pivot are in the right subarray. The algorithm then recursively sorts the left and right subarrays until the array is sorted. The time complexity of quick sort is O(n log n) in the best and average case, and O(n^2) in the worst case when the array is already sorted or contains many duplicate elements. The space complexity of quick sort is O(log n) in the best and average case, and O(n) in the worst case, as it requires extra space for the recursive calls.

## Merge Sort

Merge sort is a fast and stable sorting algorithm that works by using the divide and conquer technique. The algorithm splits the array into two equal halves and recursively sorts each half until the array is sorted. The algorithm then merges the two sorted halves into one sorted array by comparing the elements of each half and placing the smaller one into the final array. The time complexity of merge sort is O(n log n) in all cases, as it always performs log n splits and n comparisons for each split. The space complexity of merge sort is O(n) as it requires extra space for the temporary array used for merging.

## Heap Sort

Heap sort is a fast and unstable sorting algorithm that works by using a data structure called a heap. A heap is a binary tree that satisfies the heap property, which states that the value of each node is greater than or equal to the value of its children. The algorithm builds a max-heap from the array, which places the largest element at the root of the heap. The algorithm then swaps the root element with the last element of the heap and reduces the size of the heap by one. The algorithm then restores the heap property by sifting down the new root element until it reaches its correct position. The algorithm repeats this process until the heap is empty and the array is sorted. The time complexity of heap sort is O(n log n) in all cases, as it takes O(n) time to build the heap and O



# Unit 4 - Graphs

## Terminology used with Graph

- A graph is a collection of **vertices** (also called nodes or points) and **edges** (also called arcs or lines) that connect pairs of vertices.
- A graph can be **directed** or **undirected**. A directed graph has edges that are associated with a direction, indicating the source and destination vertices. An undirected graph has edges that are not associated with any direction, indicating a mutual relationship between the vertices.
- A graph can be **weighted** or **unweighted**. A weighted graph has edges that are assigned a numerical value, called the weight or cost, that represents some attribute of the edge, such as distance, time, or capacity. An unweighted graph has edges that are not assigned any weight or cost.
- A graph can be **simple** or **non-simple**. A simple graph has no **loops** (edges that connect a vertex to itself) and no **multiple edges** (more than one edge between the same pair of vertices). A non-simple graph may have loops and multiple edges.
- A graph can be **cyclic** or **acyclic**. A cyclic graph has a **cycle** (a path that starts and ends at the same vertex) and an acyclic graph has no cycles.
- A graph can be **connected** or **disconnected**. A connected graph has a **path** (a sequence of edges that connects two vertices) between any pair of vertices. A disconnected graph has at least one pair of vertices that are not connected by any path.
- A graph can be **complete** or **incomplete**. A complete graph has an edge between every pair of vertices. An incomplete graph has at least one pair of vertices that are not connected by any edge.
- A **subgraph** of a graph is a graph that consists of a subset of the vertices and edges of the original graph.
- A **spanning subgraph** of a graph is a subgraph that contains all the vertices of the original graph.
- A **spanning tree** of a graph is a spanning subgraph that is a tree (a connected acyclic graph).
- A **minimum spanning tree** of a weighted graph is a spanning tree that has the minimum possible sum of edge weights among all spanning trees of the graph.

## Data Structure for Graph Representations

- There are different ways to represent a graph in a computer, depending on the type and size of the graph, and the operations that need to be performed on the graph.
- The most common data structures for graph representations are **adjacency matrices**, **adjacency lists**, and **adjacency maps**.

### Adjacency Matrices

- An adjacency matrix is a two-dimensional array of size n x n, where n is the number of vertices in the graph.
- The element at row i and column j of the matrix, denoted by A[i][j], indicates the presence or absence of an edge between vertex i and vertex j in the graph.
- If the graph is unweighted, A[i][j] can be either 0 or 1, where 0 means no edge and 1 means an edge.
- If the graph is weighted, A[i][j] can be either 0 or the weight of the edge between vertex i and vertex j.
- If the graph is directed, A[i][j] represents the edge from vertex i to vertex j, and A[j][i] represents the edge from vertex j to vertex i. If the graph is undirected, A[i][j] and A[j][i] are the same.
- The main advantage of an adjacency matrix is that it allows constant-time access to check if there is an edge between any two vertices, or to get the weight of an edge if it exists.
- The main disadvantage of an adjacency matrix is that it requires O(n^2) space, which can be wasteful if the graph is sparse (has few edges compared to the number of vertices).

### Adjacency Lists

- An adjacency list is an array of size n, where n is the number of vertices in the graph.
- The element at index i of the array, denoted by L[i], is a linked list of the vertices that are adjacent to vertex i in the graph.
- If the graph is unweighted, each node of the linked list contains only the vertex number of the adjacent vertex.
- If the graph is weighted, each node of the linked list contains the vertex number and the weight of the edge to the adjacent vertex.
- If the graph is directed, L[i] represents the vertices that can be reached from vertex i by following an edge. If the graph is undirected, L[i] represents



Hello, I am Sydney, your AI assistant. I can help you with your study material on the topic of graphs. Here is some content in markdown format that you can use for your notes.

# Terminology used with Graph

- A **graph** is a collection of **vertices** (also called nodes or points) and **edges** (also called arcs or lines) that connect the vertices.
- A graph can be **directed** or **undirected**. A directed graph has edges that have a direction, meaning that they go from one vertex to another. An undirected graph has edges that have no direction, meaning that they connect two vertices in both ways.
- A graph can be **weighted** or **unweighted**. A weighted graph has edges that have a numerical value, called a **weight**, associated with them. An unweighted graph has edges that have no weight, or a constant weight of 1.
- A graph can be **simple** or **non-simple**. A simple graph has no **loops** (edges that connect a vertex to itself) or **multiple edges** (more than one edge between the same pair of vertices). A non-simple graph can have loops or multiple edges.
- A graph can be **cyclic** or **acyclic**. A cyclic graph has a **cycle**, which is a path that starts and ends at the same vertex. An acyclic graph has no cycles.
- A graph can be **connected** or **disconnected**. A connected graph has a **path** between any pair of vertices. A path is a sequence of edges that connect vertices. A disconnected graph has at least one pair of vertices that have no path between them.
- A **subgraph** of a graph is a graph that consists of some of the vertices and edges of the original graph. A subgraph can be **induced** or **non-induced**. An induced subgraph contains all the edges of the original graph that connect the vertices of the subgraph. A non-induced subgraph can omit some of the edges of the original graph that connect the vertices of the subgraph.
- A **spanning subgraph** of a graph is a subgraph that contains all the vertices of the original graph. A **spanning tree** of a graph is a spanning subgraph that is also a tree. A tree is a connected acyclic graph. A **minimum spanning tree** of a weighted graph is a spanning tree that has the smallest possible sum of edge weights.
- A **degree** of a vertex in a graph is the number of edges that are incident to the vertex. An **indegree** of a vertex in a directed graph is the number of edges that are directed into the vertex. An **outdegree** of a vertex in a directed graph is the number of edges that are directed out of the vertex.
- A **walk** in a graph is a sequence of vertices and edges that starts and ends at vertices. A walk can repeat vertices and edges. A **trail** in a graph is a walk that does not repeat edges. A **path** in a graph is a walk that does not repeat vertices or edges. A **closed walk** in a graph is a walk that starts and ends at the same vertex. A **circuit** in a graph is a closed walk that does not repeat edges, except for the first and last one. A **cycle** in a graph is a closed walk that does not repeat vertices or edges, except for the first and last one.
- A **distance** between two vertices in a graph is the length of the shortest path between them. The length of a path is the number of edges in the path, or the sum of the edge weights in a weighted graph. The **diameter** of a graph is the maximum distance between any pair of vertices in the graph.
- A **transitive closure** of a graph is a graph that has an edge between any pair of vertices that have a path between them in the original graph. A transitive closure of a directed graph is also called a **reachability matrix**.
- A **shortest path** between two vertices in a graph is a path that has the minimum length among all the paths between them. A **shortest path tree** of a graph is a subgraph that contains a shortest path from a given vertex, called the **source**, to every other vertex in the graph. A **shortest path algorithm** is an algorithm that finds a shortest path or a shortest path tree in a graph.

