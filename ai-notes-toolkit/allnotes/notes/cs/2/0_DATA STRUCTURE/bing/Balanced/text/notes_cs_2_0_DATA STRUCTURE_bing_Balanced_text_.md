

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



### Basic Terminology

- **Data**: Data is a collection of facts and figures that can be processed to produce meaningful information. Data can be of different types, such as numbers, characters, symbols, images, etc.
- **Data Structure**: Data structure is a way of organizing and storing data in a computer memory, so that it can be accessed and modified efficiently. Data structure can be classified into two types: primitive and non-primitive. Primitive data structures are the basic built-in data types in C, such as int, char, float, double, etc. Non-primitive data structures are the user-defined data types, such as arrays, lists, stacks, queues, trees, graphs, etc.
- **Algorithm**: Algorithm is a finite set of instructions or steps that defines a logical process to solve a problem. An algorithm must have the following properties: finiteness, definiteness, input, output and effectiveness. An algorithm can be expressed in different ways, such as natural language, pseudocode, flowchart, etc.
- **Efficiency of an Algorithm**: Efficiency of an algorithm is a measure of how well it performs in terms of time and space. Time efficiency refers to how fast an algorithm can solve a problem, while space efficiency refers to how much memory an algorithm requires to execute. The efficiency of an algorithm depends on the size and nature of the input, as well as the hardware and software environment.
- **Time and Space Complexity**: Time complexity is a function that represents the amount of time an algorithm takes to run as a function of the size of the input. Space complexity is a function that represents the amount of memory an algorithm uses as a function of the size of the input. Both time and space complexity can be expressed using asymptotic notations, such as Big Oh, Big Theta and Big Omega.
- **Asymptotic Notations**: Asymptotic notations are mathematical tools that are used to describe the behavior of functions in the limit, as the input size approaches infinity. They are useful to compare the efficiency of different algorithms and to ignore the constant factors and lower order terms that are insignificant for large inputs. The most common asymptotic notations are:
  - **Big Oh (O)**: Big Oh notation gives the upper bound of a function, that is, the maximum possible value that the function can take for any input size. For example, if f(n) = 3n^2 + 5n + 2, then f(n) = O(n^2), because n^2 is the dominant term and 3, 5 and 2 are constants that can be ignored.
  - **Big Theta (Θ)**: Big Theta notation gives the tight bound of a function, that is, the range of values that the function can take for any input size. For example, if f(n) = 3n^2 + 5n + 2, then f(n) = Θ(n^2), because n^2 is the dominant term and there exist constants c1 and c2 such that c1n^2 <= f(n) <= c2n^2 for all n.
  - **Big Omega (Ω)**: Big Omega notation gives the lower bound of a function, that is, the minimum possible value that the function can take for any input size. For example, if f(n) = 3n^2 + 5n + 2, then f(n) = Ω(n^2), because n^2 is the dominant term and there exist a constant c such that f(n) >= cn^2 for all n.
- **Time-Space Trade-off**: Time-space trade-off is a concept that states that there is a trade-off between the time and space efficiency of an algorithm. That is, an algorithm that is faster may require more memory, and an algorithm that is more memory-efficient may be slower. For example, sorting an array using bubble sort is a time-inefficient but space-efficient algorithm, while sorting an array using merge sort is a time-efficient but space-inefficient algorithm.
- **Abstract Data Type (ADT)**: Abstract data type is a logical concept that defines a data type by its behavior and operations, without specifying its implementation details. An ADT is an abstraction that hides the complexity and details of the data structure from the user. An ADT can be implemented using different data structures, such as arrays, lists, stacks, queues, etc. For example, a stack ADT can be implemented using an array or a linked list.



### Elementary Data Organization

- Data is the basic unit of information that can be processed by a computer.
- Data can be organized in different ways to facilitate efficient storage, retrieval, manipulation and communication.
- Some of the common ways of organizing data are:

  - Arrays: A collection of homogeneous data elements stored in contiguous memory locations and accessed by their indices.
  - Lists: A collection of heterogeneous data elements linked by pointers and accessed by traversing the links.
  - Stacks: A linear data structure that follows the last-in first-out (LIFO) principle of insertion and deletion.
  - Queues: A linear data structure that follows the first-in first-out (FIFO) principle of insertion and deletion.
  - Trees: A hierarchical data structure that consists of nodes and edges, where each node can have zero or more children and at most one parent.
  - Graphs: A non-linear data structure that consists of nodes and edges, where each node can have zero or more neighbors and each edge can have a weight or direction.
  - Hash tables: A data structure that maps keys to values using a hash function and handles collisions using chaining or probing.
  - Files: A collection of data stored on a secondary storage device and accessed by name or path.

- Built-in data types in C are the basic data types that are predefined by the C language and supported by the compiler.
- Some of the built-in data types in C are:

  - int: An integer data type that can store whole numbers in the range of -32768 to 32767 (16 bits) or -2147483648 to 2147483647 (32 bits) depending on the compiler.
  - char: A character data type that can store a single character in the range of -128 to 127 (8 bits) or 0 to 255 (8 bits) depending on the compiler.
  - float: A floating-point data type that can store real numbers with a decimal point in the range of 3.4E-38 to 3.4E+38 (32 bits) with a precision of 6 digits.
  - double: A double-precision floating-point data type that can store real numbers with a decimal point in the range of 1.7E-308 to 1.7E+308 (64 bits) with a precision of 15 digits.
  - void: A special data type that indicates the absence of any data or return value.

- An algorithm is a finite sequence of well-defined steps that solves a specific problem or performs a specific task.
- Efficiency of an algorithm is a measure of how well the algorithm uses the available resources, such as time, space, memory, etc., to produce the desired output.
- Time complexity of an algorithm is a function that expresses the amount of time required by the algorithm to run as a function of the input size.
- Space complexity of an algorithm is a function that expresses the amount of memory or space required by the algorithm to run as a function of the input size.
- Asymptotic notations are mathematical tools that are used to compare the growth rates of different functions and to classify the algorithms based on their time and space complexities.
- Some of the common asymptotic notations are:

  - Big Oh (O): It represents the upper bound or the worst case scenario of a function. It means that the function is always less than or equal to a constant multiple of another function. For example, O(n) means that the function is always less than or equal to cn for some constant c and for all sufficiently large n.
  - Big Theta (Θ): It represents the tight bound or the average case scenario of a function. It means that the function is always bounded by two constant multiples of another function. For example, Θ(n) means that the function is always between cn and dn for some constants c and d and for all sufficiently large n.
  - Big Omega (Ω): It represents the lower bound or the best case scenario of a function. It means that the function is always greater than or equal to a constant multiple of another function. For example, Ω(n) means that the function is always greater than or equal to cn for some constant c and for all sufficiently large n.

- Time-space trade-off is a concept that states that there is often a trade-off between the time and space complexities of an algorithm. It means that by using more space, we can reduce the time required by the algorithm, and vice versa. For example, by using a hash table, we can reduce the time required to search for an element from O(n) to O(1), but at the cost of using more space to store the hash table.
- Abstract data types (ADTs) are data types



### Built in Data Types in C

- Data types are the means of specifying the kind of data that can be stored and manipulated by a program.
- C language supports several built in data types, such as int, char, float, double, etc.
- Each data type has a range of values that it can represent, and a size in bytes that it occupies in memory.
- The range and size of a data type may vary depending on the compiler and the platform.
- The built in data types in C can be classified into four categories: integer, floating-point, character, and derived.

#### Integer Data Types

- Integer data types are used to store whole numbers, such as 0, 1, -5, 42, etc.
- C supports four integer data types: char, short, int, and long.
- The char data type is used to store a single character, such as 'a', '9', or '#'. It can also be used to store small integers, such as 0 to 127, or -128 to 127, depending on whether it is signed or unsigned. The size of char is 1 byte.
- The short data type is used to store small integers, such as -32768 to 32767, or 0 to 65535, depending on whether it is signed or unsigned. The size of short is 2 bytes.
- The int data type is used to store medium-sized integers, such as -2147483648 to 2147483647, or 0 to 4294967295, depending on whether it is signed or unsigned. The size of int is usually 4 bytes, but it may vary depending on the compiler and the platform.
- The long data type is used to store large integers, such as -9223372036854775808 to 9223372036854775807, or 0 to 18446744073709551615, depending on whether it is signed or unsigned. The size of long is usually 8 bytes, but it may vary depending on the compiler and the platform.
- The integer data types can be modified by using the keywords signed, unsigned, short, and long, to specify the range and size of the data type. For example, unsigned long int is a data type that can store positive integers up to 18446744073709551615, and has a size of 8 bytes.

#### Floating-Point Data Types

- Floating-point data types are used to store real numbers, such as 3.14, -0.001, 6.022e23, etc.
- C supports two floating-point data types: float and double.
- The float data type is used to store single-precision floating-point numbers, which have a decimal point and a fractional part. The range of float is approximately -3.4e38 to 3.4e38, and the precision is about 6 to 7 digits. The size of float is 4 bytes.
- The double data type is used to store double-precision floating-point numbers, which have a decimal point and a fractional part. The range of double is approximately -1.7e308 to 1.7e308, and the precision is about 15 to 16 digits. The size of double is 8 bytes.
- The floating-point data types can be modified by using the keyword long, to specify a higher precision and range. For example, long double is a data type that can store extended-precision floating-point numbers, which have a decimal point and a fractional part. The range and precision of long double may vary depending on the compiler and the platform, but it is usually greater than double. The size of long double is usually 10 or 16 bytes.

#### Character Data Types

- Character data types are used to store characters, such as letters, digits, symbols, etc.
- C supports one character data type: char.
- The char data type is used to store a single character, such as 'a', '9', or '#'. It can also be used to store small integers, such as 0 to 127, or -128 to 127, depending on whether it is signed or unsigned. The size of char is 1 byte.
- The char data type can be modified by using the keywords signed and unsigned, to specify the range of the data type. For example, unsigned char is a data type that can store positive integers from 0 to 255, and has a size of 1 byte.
- The char data type can also be used to store strings, which are sequences of characters, such as "Hello", "C", or "Data Structure". Strings are stored as arrays of char, and are terminated by a special



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Algorithm for the notes of the Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT) in the subject of DATA STRUCTURE.

### Algorithm

- An algorithm is a finite sequence of well-defined steps that solves a specific problem or performs a specific task.
- An algorithm can be expressed in different ways, such as natural language, pseudocode, flowchart, or programming language.
- An algorithm should have the following characteristics:
  - Finiteness: It should have a clear beginning and end, and terminate after a finite number of steps.
  - Definiteness: Each step should be precisely defined and unambiguous.
  - Input: It should take zero or more inputs from a specified set of values.
  - Output: It should produce one or more outputs from a specified set of values.
  - Effectiveness: Each step should be simple and feasible to execute.

### Efficiency of an Algorithm

- The efficiency of an algorithm measures how well it uses the available resources, such as time and space, to solve a problem or perform a task.
- The efficiency of an algorithm depends on the size and nature of the input, the hardware and software environment, and the implementation details.
- The efficiency of an algorithm can be analyzed using two approaches:
  - A priori analysis: It estimates the efficiency of an algorithm based on some mathematical model or formula, without actually running the algorithm on a specific input or machine.
  - A posteriori analysis: It measures the efficiency of an algorithm based on the actual execution time and space used by the algorithm on a specific input and machine.

### Time and Space Complexity

- The time complexity of an algorithm is the amount of time it takes to complete its execution as a function of the input size.
- The space complexity of an algorithm is the amount of memory it uses to store data and instructions as a function of the input size.
- The time and space complexity of an algorithm can be expressed using different notations, such as:
  - Big Oh notation: It gives the upper bound or the worst-case scenario of the complexity of an algorithm. It is denoted by O(f(n)), where f(n) is some function of the input size n.
  - Big Theta notation: It gives the tight bound or the average-case scenario of the complexity of an algorithm. It is denoted by Θ(f(n)), where f(n) is some function of the input size n.
  - Big Omega notation: It gives the lower bound or the best-case scenario of the complexity of an algorithm. It is denoted by Ω(f(n)), where f(n) is some function of the input size n.

### Time-Space Trade-off

- The time-space trade-off is a concept that states that there is often a trade-off between the time and space complexity of an algorithm, meaning that improving one may worsen the other.
- For example, an algorithm that uses more memory to store intermediate results may reduce the number of computations and hence the time complexity, while an algorithm that uses less memory may increase the number of computations and hence the time complexity.
- The time-space trade-off depends on the problem, the algorithm, and the available resources, and there is no general rule to determine the optimal balance between them.

### Abstract Data Types (ADT)

- An abstract data type (ADT) is a logical representation of a set of data and the operations that can be performed on that data, without specifying the physical implementation details.
- An ADT defines the data type by its behavior or functionality, rather than by its structure or representation.
- An ADT can be implemented using different data structures, such as arrays, linked lists, stacks, queues, trees, graphs, etc.
- An ADT provides a level of abstraction and modularity that makes the design and development of algorithms and programs easier and more efficient.



Hello, I am Sydney, your AI assistant. I can help you with your study material on data structure. Here is some content on the topic of efficiency of an algorithm.

### Efficiency of an Algorithm

- An algorithm is a finite sequence of well-defined steps that solves a problem or performs a task.
- The efficiency of an algorithm measures how well it uses the available resources, such as time and space, to accomplish its goal.
- The time complexity of an algorithm is the amount of time it takes to execute as a function of the input size.
- The space complexity of an algorithm is the amount of memory it uses as a function of the input size.
- The asymptotic notations are mathematical tools that help us compare the growth rates of different functions, such as time and space complexity functions, as the input size approaches infinity.
- The most common asymptotic notations are:
  - Big Oh notation (O): It gives the upper bound of a function, meaning that the function is always less than or equal to a constant multiple of another function.
  - Big Theta notation (Θ): It gives the tight bound of a function, meaning that the function is always between a constant multiple of another function and another constant multiple of the same function.
  - Big Omega notation (Ω): It gives the lower bound of a function, meaning that the function is always greater than or equal to a constant multiple of another function.
- The time-space trade-off is a concept that states that sometimes we can improve the time complexity of an algorithm by using more space, or vice versa.
- An abstract data type (ADT) is a logical representation of a set of data and the operations that can be performed on it, without specifying how the data is stored or how the operations are implemented.



Hello, I am Sydney, your AI assistant. I can help you with your study material on data structures. Here is the content for the topic of time and space complexity.

### Time and Space Complexity

- Time complexity is a measure of how much time an algorithm takes to execute as a function of the input size.
- Space complexity is a measure of how much memory an algorithm uses as a function of the input size.
- Both time and space complexity are important factors to consider when designing and analyzing algorithms, as they affect the performance and efficiency of the program.
- There are different ways to express the time and space complexity of an algorithm, such as using mathematical functions, recurrence relations, or asymptotic notations.

#### Asymptotic Notations

- Asymptotic notations are a way of describing the growth rate of a function, ignoring the constant factors and lower-order terms.
- They are useful for comparing the time and space complexity of different algorithms, as they focus on the dominant term that determines the behavior of the function for large inputs.
- There are three common asymptotic notations: Big Oh, Big Theta, and Big Omega.

##### Big Oh Notation

- Big Oh notation, denoted by O(f(n)), represents the upper bound of a function, meaning that the function is always less than or equal to some constant multiple of f(n) for sufficiently large n.
- For example, if the time complexity of an algorithm is O(n^2), it means that the algorithm takes at most c*n^2 time units to execute for some constant c and for all n greater than some n0.
- Big Oh notation is useful for estimating the worst-case scenario of an algorithm, as it gives the maximum possible time or space required by the algorithm.

##### Big Theta Notation

- Big Theta notation, denoted by Θ(f(n)), represents the tight bound of a function, meaning that the function is always bounded by some constant multiples of f(n) for sufficiently large n.
- For example, if the time complexity of an algorithm is Θ(n^2), it means that the algorithm takes between c1*n^2 and c2*n^2 time units to execute for some constants c1 and c2 and for all n greater than some n0.
- Big Theta notation is useful for estimating the average-case scenario of an algorithm, as it gives the most accurate representation of the time or space required by the algorithm.

##### Big Omega Notation

- Big Omega notation, denoted by Ω(f(n)), represents the lower bound of a function, meaning that the function is always greater than or equal to some constant multiple of f(n) for sufficiently large n.
- For example, if the time complexity of an algorithm is Ω(n^2), it means that the algorithm takes at least c*n^2 time units to execute for some constant c and for all n greater than some n0.
- Big Omega notation is useful for estimating the best-case scenario of an algorithm, as it gives the minimum possible time or space required by the algorithm.

#### Time-Space Trade-off

- Time-space trade-off is a concept that describes the trade-off between the time and space complexity of an algorithm, meaning that improving one may worsen the other.
- For example, an algorithm that uses more memory may run faster than an algorithm that uses less memory, or vice versa.
- Time-space trade-off is important to consider when choosing an algorithm for a given problem, as it depends on the available resources and the desired performance of the program.

#### Abstract Data Types (ADT)

- Abstract data types (ADT) are a way of defining the data and the operations on the data without specifying the implementation details.
- ADT are useful for hiding the complexity and the details of the data structure from the user, and for providing a clear and consistent interface for the user to interact with the data.
- ADT are also useful for allowing the flexibility and the modularity of the data structure, as the implementation can be changed without affecting the user.
- Examples of ADT are stacks, queues, lists, trees, graphs, etc.



### Asymptotic notations: Big Oh, Big Theta and Big Omega

- Asymptotic notations are mathematical tools that help us to analyze the efficiency of an algorithm in terms of its time and space complexity.
- They allow us to express the growth rate of a function that represents the running time or the memory usage of an algorithm as the input size increases.
- They also help us to compare different algorithms and choose the best one for a given problem.
- There are three common asymptotic notations: Big Oh, Big Theta and Big Omega.

#### Big Oh notation

- Big Oh notation, denoted by O(f(n)), is used to describe the upper bound of a function, or the worst-case scenario of an algorithm.
- It means that the function is at most proportional to f(n) for sufficiently large values of n.
- For example, if the running time of an algorithm is O(n^2), it means that the algorithm takes at most n^2 steps to complete for any input of size n.
- Big Oh notation is useful for analyzing the worst-case performance of an algorithm and for determining the upper limit of the resources needed.

#### Big Theta notation

- Big Theta notation, denoted by Θ(f(n)), is used to describe the tight bound of a function, or the average-case scenario of an algorithm.
- It means that the function is both at least and at most proportional to f(n) for sufficiently large values of n.
- For example, if the running time of an algorithm is Θ(n log n), it means that the algorithm takes between n log n and n log n steps to complete for any input of size n.
- Big Theta notation is useful for analyzing the average-case performance of an algorithm and for determining the exact amount of resources needed.

#### Big Omega notation

- Big Omega notation, denoted by Ω(f(n)), is used to describe the lower bound of a function, or the best-case scenario of an algorithm.
- It means that the function is at least proportional to f(n) for sufficiently large values of n.
- For example, if the running time of an algorithm is Ω(n), it means that the algorithm takes at least n steps to complete for any input of size n.
- Big Omega notation is useful for analyzing the best-case performance of an algorithm and for determining the lower limit of the resources needed.



### Time-Space trade-off

- Time-space trade-off is a concept in computer science that refers to the balance between the running time and the memory usage of an algorithm or a program.
- Generally, there is a trade-off between time and space, meaning that faster algorithms or programs tend to use more memory, and slower algorithms or programs tend to use less memory.
- For example, suppose we want to search for an element in an array. One way to do this is to use a linear search, which scans the array from the beginning to the end until it finds the element or reaches the end of the array. This algorithm is simple and uses constant space, but it takes linear time in the worst case, meaning that it can be slow if the array is large or the element is not present. Another way to do this is to use a binary search, which assumes that the array is sorted and repeatedly divides the array into two halves, discarding the half that does not contain the element. This algorithm is more complex and uses logarithmic space, but it takes logarithmic time in the worst case, meaning that it can be fast even if the array is large or the element is not present.
- The choice of which algorithm to use depends on the trade-off between time and space that we are willing to make. If we have limited memory or we care more about the speed of the search, we might prefer the binary search. If we have abundant memory or we care more about the simplicity of the code, we might prefer the linear search.
- In general, the time-space trade-off can be influenced by many factors, such as the input size, the hardware capabilities, the programming language, the design goals, the optimization techniques, and the theoretical limitations. There is no universal rule or formula to determine the optimal trade-off for every problem or situation. Instead, we have to analyze the advantages and disadvantages of different algorithms or programs and choose the one that best suits our needs and constraints.



### Abstract Data Types (ADT)

- An abstract data type (ADT) is a mathematical model of a data structure that specifies the type of data stored, the operations supported on them, and the behaviour of those operations.
- An ADT does not reveal the details of how the data is stored or how the operations are implemented. It only describes what the data can do and what the operations can achieve.
- An ADT is defined by a set of values and a set of operations on those values.
- An ADT can be implemented using different data structures, such as arrays, linked lists, trees, etc. The choice of data structure depends on the efficiency and complexity of the operations.
- An ADT provides a level of abstraction that separates the logical properties of a data type from its physical implementation.
- An ADT allows the programmer to focus on the problem-solving logic rather than the low-level details of data representation and manipulation.
- An ADT can be used to design and implement software modules that are reusable, reliable, and easy to maintain.
- Examples of ADTs are stack, queue, list, set, map, graph, etc. Each of these ADTs defines a set of data and a set of operations on that data. For example, a stack ADT defines a data type that stores elements in a last-in first-out (LIFO) order, and supports operations such as push, pop, peek, isEmpty, etc.



## Unit 2 - Arrays and Linked Lists

- Arrays are data structures that store a collection of elements of the same data type in contiguous memory locations.
- Arrays can be classified into single-dimensional and multi-dimensional arrays based on the number of indices required to access an element.
- Single-dimensional arrays are also called linear or one-dimensional arrays. They have only one index or subscript to access an element. For example, `int a[10]` is a single-dimensional array of 10 integers.
- Multi-dimensional arrays are also called rectangular or n-dimensional arrays. They have more than one index or subscript to access an element. For example, `int b[3][4]` is a two-dimensional array of 12 integers, arranged in 3 rows and 4 columns.
- Representation of arrays: Arrays can be stored in memory in two ways: row major order and column major order.
  - Row major order: In this method, the elements of an array are stored row by row, starting from the first row. The elements of each row are stored in consecutive memory locations. For example, the two-dimensional array `b[3][4]` is stored in row major order as follows:

    | Memory Address | Element |
    | -------------- | ------- |
    | 1000           | b[0][0] |
    | 1004           | b[0][1] |
    | 1008           | b[0][2] |
    | 1012           | b[0][3] |
    | 1016           | b[1][0] |
    | 1020           | b[1][1] |
    | 1024           | b[1][2] |
    | 1028           | b[1][3] |
    | 1032           | b[2][0] |
    | 1036           | b[2][1] |
    | 1040           | b[2][2] |
    | 1044           | b[2][3] |

  - Column major order: In this method, the elements of an array are stored column by column, starting from the first column. The elements of each column are stored in consecutive memory locations. For example, the two-dimensional array `b[3][4]` is stored in column major order as follows:

    | Memory Address | Element |
    | -------------- | ------- |
    | 1000           | b[0][0] |
    | 1004           | b[1][0] |
    | 1008           | b[2][0] |
    | 1012           | b[0][1] |
    | 1016           | b[1][1] |
    | 1020           | b[2][1] |
    | 1024           | b[0][2] |
    | 1028           | b[1][2] |
    | 1032           | b[2][2] |
    | 1036           | b[0][3] |
    | 1040           | b[1][3] |
    | 1044           | b[2][3] |

- Derivation of index formulae for 1-D, 2-D, 3-D and n-D arrays: To calculate the memory address of any element in an array, we need to know the base address of the array, the size of each element, the number of dimensions, the size of each dimension, and the index of the element. The formulae for different types of arrays are as follows:
  - For a single-dimensional array `a[n]` stored in row major order, the memory address of `a[i]` is given by:

    `address(a[i]) = base(a) + i * size(a)`

    where `base(a)` is the base address of the array, `i` is the index of the element, and `size(a)` is the size of each element.

  - For a two-dimensional array `a[m][n]` stored in row major order, the memory address of `a[i][j]` is given by:

    `address(a[i][j]) = base(a) + (i * n + j) * size(a)`

    where `base(a)` is the base address of the array, `i` and `j` are the indices of the element, `n` is the size of the second dimension, and `size(a)` is the size of each element.

  - For a three-dimensional array `a[l][m][n]` stored in row major order, the memory address of `a



### Definition for the notes of the Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial. in the subject of DATA STRUCTURE

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- A single-dimensional array is an array with one dimension, or one row of elements. For example, int A[10] is a single-dimensional array of 10 integers.
- A multidimensional array is an array with more than one dimension, or more than one row and column of elements. For example, int B[3][4] is a two-dimensional array of 3 rows and 4 columns of integers.
- The representation of arrays in memory depends on the order in which the elements are stored. There are two common orders: row major order and column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the elements of B[3][4] are stored as B[0][0], B[0][1], B[0][2], B[0][3], B[1][0], B[1][1], B[1][2], B[1][3], B[2][0], B[2][1], B[2][2], B[2][3].
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the elements of B[3][4] are stored as B[0][0], B[1][0], B[2][0], B[0][1], B[1][1], B[2][1], B[0][2], B[1][2], B[2][2], B[0][3], B[1][3], B[2][3].
- The index formulae for an array are used to calculate the address of an element in memory, given its index and the base address of the array. The formulae depend on the order, the number of dimensions, and the size of each dimension of the array.
- For a single-dimensional array A[n] stored in row major order, the address of A[i] is given by:

  - Address of A[i] = Base address of A + i * size of each element

- For a two-dimensional array B[m][n] stored in row major order, the address of B[i][j] is given by:

  - Address of B[i][j] = Base address of B + (i * n + j) * size of each element

- For a three-dimensional array C[p][q][r] stored in row major order, the address of C[i][j][k] is given by:

  - Address of C[i][j][k] = Base address of C + (i * q * r + j * r + k) * size of each element

- For an n-dimensional array D[d1][d2]...[dn] stored in row major order, the address of D[i1][i2]...[in] is given by:

  - Address of D[i1][i2]...[in] = Base address of D + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size of each element

- The index formulae for arrays stored in column major order can be derived by reversing the order of the indices and dimensions in the formulae for row major order.
- Arrays can be used to store and manipulate various types of data, such as matrices, vectors, strings, tables, etc.
- A sparse matrix is a matrix that has a large number of zero elements and a small number of non-zero elements. Storing a sparse matrix as a regular array would waste a lot of memory space. Therefore, there are different ways of representing a sparse matrix, such as:

  - Triplet representation: A sparse matrix is stored as a list of triplets, where each triplet consists of the row index, the column index, and the value of a non-zero element. For example, the



### Single and Multidimensional Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- A single-dimensional array is an array with one dimension, meaning that it can store a fixed number of elements of the same type in a linear sequence.
- A multidimensional array is an array with more than one dimension, meaning that it can store a fixed number of elements of the same type in a rectangular or higher-dimensional grid.
- The representation of arrays in memory depends on the order in which the elements are stored. There are two common orders: row-major order and column-major order.
- In row-major order, the elements of an array are stored row by row, meaning that the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column-major order, the elements of an array are stored column by column, meaning that the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The index formulae for accessing the elements of an array depend on the order, the number of dimensions, and the size of each dimension of the array.
- For a one-dimensional array A of size n, the index formula for accessing the element A[i] in row-major order or column-major order is the same: i.
- For a two-dimensional array A of size m x n, the index formula for accessing the element A[i][j] in row-major order is i * n + j, and in column-major order is i + j * m.
- For a three-dimensional array A of size l x m x n, the index formula for accessing the element A[i][j][k] in row-major order is i * m * n + j * n + k, and in column-major order is i + j * l + k * l * m.
- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formula for accessing the element A[i1][i2]...[in] in row-major order is i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in, and in column-major order is i1 + i2 * d1 + i3 * d1 * d2 + ... + in * d1 * d2 * ... * dn-1.
- Arrays are useful for storing and manipulating data that have a fixed and regular structure, such as matrices, vectors, images, etc.
- Sparse matrices are matrices that have a large number of zero elements and a small number of non-zero elements. Storing sparse matrices as arrays can waste a lot of memory space and computation time.
- There are different ways of representing sparse matrices, such as using linked lists, arrays of lists, hash tables, etc. One common representation is using a triplet (row, column, value) to store each non-zero element of the matrix.



### Representation of Arrays: Row Major Order, and Column Major Order

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by their indices.
- A single-dimensional array is a linear array, where each element has a unique index.
- A multi-dimensional array is an array of arrays, where each element is another array of one lower dimension.
- The representation of arrays in memory depends on the order in which the elements are stored, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, i.e., the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column major order, the elements of an array are stored column by column, i.e., the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The index formulae for accessing the elements of an array depend on the order of storage and the dimensions of the array.
- For a one-dimensional array A of size n, the index formula is:

  - A[i] = base address + i * size of element, where i is the index of the element, 0 <= i < n.

- For a two-dimensional array A of size m x n, the index formulae are:

  - A[i][j] = base address + (i * n + j) * size of element, for row major order, where i is the row index and j is the column index, 0 <= i < m, 0 <= j < n.
  - A[i][j] = base address + (j * m + i) * size of element, for column major order, where i is the row index and j is the column index, 0 <= i < m, 0 <= j < n.

- For a three-dimensional array A of size m x n x p, the index formulae are:

  - A[i][j][k] = base address + (i * n * p + j * p + k) * size of element, for row major order, where i is the first dimension index, j is the second dimension index, and k is the third dimension index, 0 <= i < m, 0 <= j < n, 0 <= k < p.
  - A[i][j][k] = base address + (k * m * n + j * m + i) * size of element, for column major order, where i is the first dimension index, j is the second dimension index, and k is the third dimension index, 0 <= i < m, 0 <= j < n, 0 <= k < p.

- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formulae are:

  - A[i1][i2]...[in] = base address + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size of element, for row major order, where i1, i2, ..., in are the indices of the n dimensions, 0 <= i1 < d1, 0 <= i2 < d2, ..., 0 <= in < dn.
  - A[i1][i2]...[in] = base address + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * size of element, for column major order, where i1, i2, ..., in are the indices of the n dimensions, 0 <= i1 < d1, 0 <= i2 < d2, ..., 0 <= in < dn.

- The application of arrays can be seen in various domains, such as mathematics, science, engineering, computer science, etc. Some examples are:

  - Matrices and vectors, which are used for linear algebra, numerical analysis, differential equations, etc.
  - Images and graphics, which are represented as arrays of pixels or colors.
  - Strings and text, which are arrays of characters or symbols.
  - Tables and databases, which are arrays of records or fields.
  - Sorting and searching algorithms, which operate on arrays of data.

- A sparse matrix is a matrix that has a large number of zero elements, compared to the non-zero elements. Storing a sparse matrix as a regular array would waste a lot of memory space, so different representations are used to store only the non-zero elements and their positions.
- Some common



### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by their indices.
- The index formula is a mathematical expression that calculates the address of any element in an array, given its base address, size, and dimensions.
- The index formula depends on the order of storing the array elements in memory, which can be either row major or column major.
- In row major order, the elements of a row are stored together, followed by the elements of the next row, and so on. In column major order, the elements of a column are stored together, followed by the elements of the next column, and so on.
- The index formula for a 1-D array is:

  - LOC(A[i]) = B + W * (i - LB), where
    - LOC(A[i]) is the address of the ith element of the array A
    - B is the base address of the array A
    - W is the size of each element of the array A
    - i is the index of the element to be accessed
    - LB is the lower bound of the index range of the array A
  - This formula is the same for both row major and column major order, since a 1-D array has only one dimension.

- The index formula for a 2-D array is:

  - LOC(A[i][j]) = B + W * (i * C + j - LB1 * C - LB2), where
    - LOC(A[i][j]) is the address of the element in the ith row and jth column of the array A
    - B is the base address of the array A
    - W is the size of each element of the array A
    - i and j are the indices of the element to be accessed
    - C is the number of columns in the array A
    - LB1 and LB2 are the lower bounds of the index ranges of the array A for rows and columns, respectively
  - This formula is for row major order. For column major order, the formula is:

    - LOC(A[i][j]) = B + W * (j * R + i - LB1 - LB2 * R), where
      - R is the number of rows in the array A.

- The index formula for a 3-D array is:

  - LOC(A[i][j][k]) = B + W * (i * C * D + j * D + k - LB1 * C * D - LB2 * D - LB3), where
    - LOC(A[i][j][k]) is the address of the element in the ith plane, jth row, and kth column of the array A
    - B is the base address of the array A
    - W is the size of each element of the array A
    - i, j, and k are the indices of the element to be accessed
    - C is the number of columns in each plane of the array A
    - D is the number of planes in the array A
    - LB1, LB2, and LB3 are the lower bounds of the index ranges of the array A for planes, rows, and columns, respectively
  - This formula is for row major order. For column major order, the formula is:

    - LOC(A[i][j][k]) = B + W * (k * R * C + j * R + i - LB1 - LB2 * R - LB3 * R * C), where
      - R is the number of rows in each plane of the array A.

- The index formula for an n-D array is:

  - LOC(A[i1][i2]...[in]) = B + W * (i1 * S2 * S3 * ... * Sn + i2 * S3 * S4 * ... * Sn + ... + in - LB1 * S2 * S3 * ... * Sn - LB2 * S3 * S4 * ... * Sn - ... - LBn), where
    - LOC(A[i1][i2]...[in]) is the address of the element in the i1th dimension, i2th dimension, ..., and inth dimension of the array A
    - B is the base address of the array A
    - W is the size of each element of the array A



### Application of arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- Arrays can be used to store and manipulate various kinds of data, such as numbers, characters, strings, matrices, graphs, images, etc.
- Arrays can be classified into single and multidimensional arrays, depending on the number of dimensions or subscripts required to access an element.
- Single dimensional arrays are also called vectors or one-dimensional arrays. They have only one subscript to access an element, such as `a[i]`, where `a` is the name of the array and `i` is the index of the element.
- Multidimensional arrays are also called matrices or n-dimensional arrays. They have more than one subscript to access an element, such as `a[i][j]`, where `a` is the name of the array and `i` and `j` are the indices of the element in the row and column respectively.
- The representation of arrays in memory depends on the order in which the elements are stored. There are two common ways of storing arrays: row major order and column major order.
- Row major order means that the elements of an array are stored row by row, starting from the first row. For example, the elements of a 3x3 matrix `a` are stored as `a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2], a[2][0], a[2][1], a[2][2]`.
- Column major order means that the elements of an array are stored column by column, starting from the first column. For example, the elements of a 3x3 matrix `a` are stored as `a[0][0], a[1][0], a[2][0], a[0][1], a[1][1], a[2][1], a[0][2], a[1][2], a[2][2]`.
- The index formulae for 1-D, 2-D, 3-D and n-D arrays are used to calculate the address of an element in memory, given the base address of the array, the size of each element, and the indices of the element.
- For a 1-D array `a` of size `n` and element size `s`, the address of `a[i]` is given by `base + i * s`, where `base` is the base address of the array and `i` is the index of the element.
- For a 2-D array `a` of size `m x n` and element size `s`, the address of `a[i][j]` is given by `base + (i * n + j) * s` in row major order and `base + (j * m + i) * s` in column major order, where `base` is the base address of the array and `i` and `j` are the indices of the element in the row and column respectively.
- For a 3-D array `a` of size `l x m x n` and element size `s`, the address of `a[i][j][k]` is given by `base + (i * m * n + j * n + k) * s` in row major order and `base + (k * l * m + j * l + i) * s` in column major order, where `base` is the base address of the array and `i`, `j` and `k` are the indices of the element in the depth, row and column respectively.
- For an n-D array `a` of size `d1 x d2 x ... x dn` and element size `s`, the address of `a[i1][i2]...[in]` is given by `base + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * s` in row major order and `base + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * s` in column major order, where `base` is the base address of the array and `i1`, `i2`, ..., `in` are the indices of the element in the dimensions.

### Sparse matrices and their representations

- A sparse matrix is a matrix that has a large number of zero elements and a small number of non-zero elements



### Sparse Matrices and their representations

- A sparse matrix is a matrix in which most of the elements are zero. This is in contrast to a dense matrix, where most of the elements are non-zero.
- Sparse matrices arise in many applications, such as graph theory, network analysis, finite element methods, etc. where the data is sparse or has a lot of empty spaces.
- Storing and manipulating sparse matrices in their original form can be inefficient and wasteful of space and time. Therefore, various representations and operations have been developed to handle sparse matrices more efficiently.
- Sparse matrix representations store only the non-zero elements of the matrix, along with their row and column indices. This avoids the wastage of space in storing the zero elements, and also saves time in finding the non-zero elements in a large matrix.
- There are different ways of representing sparse matrices, such as:

  - **Triplet representation**: In this representation, a sparse matrix is stored as a list of triplets, where each triplet consists of the row index, column index, and value of a non-zero element. For example, the matrix

    | 0 | 0 | 3 | 0 |
    | - | - | - | - |
    | 2 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 |
    | 0 | 4 | 0 | 0 |

    can be represented as

    | row | col | val |
    | --- | --- | --- |
    | 0   | 2   | 3   |
    | 1   | 0   | 2   |
    | 3   | 1   | 4   |

    The advantage of this representation is that it is simple and easy to implement. The disadvantage is that it does not preserve the order of the elements, and it may contain duplicate entries for the same element.

  - **Linked list representation**: In this representation, a sparse matrix is stored as a linked list of nodes, where each node contains the row index, column index, value, and pointers to the next node in the same row and the same column. For example, the matrix

    | 0 | 0 | 3 | 0 |
    | - | - | - | - |
    | 2 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 |
    | 0 | 4 | 0 | 0 |

    can be represented as

    linked list representation

    The advantage of this representation is that it preserves the order of the elements, and it allows easy traversal of the matrix by row or by column. The disadvantage is that it requires extra space for the pointers, and it is more complex to implement.

  - **Compressed sparse row (CSR) representation**: In this representation, a sparse matrix is stored as three arrays: one for the non-zero values, one for the column indices of the non-zero values, and one for the row pointers that indicate the start of each row in the value and column index arrays. For example, the matrix

    | 0 | 0 | 3 | 0 |
    | - | - | - | - |
    | 2 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 |
    | 0 | 4 | 0 | 0 |

    can be represented as

    | val | 3 | 2 | 4 |
    | --- | - | - | - |
    | col | 2 | 0 | 1 |
    | row | 0 | 1 | 2 | 3 |

    The advantage of this representation is that it is compact and efficient for matrix-vector multiplication and other operations. The disadvantage is that it is not easy to insert or delete elements, and it does not allow random access to the elements.

  - **Compressed sparse column (CSC) representation**: In this representation, a sparse matrix is stored as three arrays: one for the non-zero values, one for the row indices of the non-zero values, and one for the column pointers that indicate the start of each column in the value and row index arrays. For example, the matrix

    | 0 | 0 | 3 | 0 |
    | - | - | - | - |



### Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

- A linked list is a linear data structure that consists of a sequence of nodes, each containing some data and a pointer to the next node in the list.
- A linked list can be implemented using either an array or a pointer-based approach.
- In the array implementation, a fixed-size array is used to store the nodes of the linked list. Each node has an index and a next field that stores the index of the next node. The first node has index 0 and the last node has a next field of -1 or null to indicate the end of the list. The array implementation has the advantage of random access and efficient memory allocation, but the disadvantage of limited size and difficulty in insertion and deletion operations.
- In the pointer implementation, each node is a dynamic memory object that contains some data and a pointer to the next node. The pointer implementation has the advantage of flexibility and ease of insertion and deletion operations, but the disadvantage of memory overhead and sequential access.
- A singly linked list is a linked list where each node has only one pointer to the next node. A singly linked list can be traversed in one direction only, from the head node to the tail node.
- A doubly linked list is a linked list where each node has two pointers, one to the next node and one to the previous node. A doubly linked list can be traversed in both directions, from the head node to the tail node or vice versa.
- A circularly linked list is a linked list where the last node points to the first node, forming a loop. A circularly linked list has no head or tail node, and can be traversed indefinitely in either direction.
- Some common operations on a linked list are:
  - Insertion: adding a new node to the list at a specified position.
  - Deletion: removing an existing node from the list at a specified position.
  - Traversal: visiting each node in the list and performing some action on the data or the node.
  - Search: finding a node in the list that matches a given criterion or value.
  - Sort: rearranging the nodes in the list according to some order or comparison function.
  - Reverse: reversing the order of the nodes in the list.
- A polynomial is an algebraic expression that consists of one or more terms, each term being a product of a constant coefficient and a variable raised to a non-negative integer power. For example, 3x^2 + 2x - 5 is a polynomial of degree 2 in the variable x.
- A polynomial can be represented using a linked list, where each node contains the coefficient and the exponent of a term, and the nodes are arranged in descending order of the exponents. For example, the polynomial 3x^2 + 2x - 5 can be represented by the linked list:

| Coefficient | Exponent | Next |
| ----------- | -------- | ---- |
| 3           | 2        | ->   |
| 2           | 1        | ->   |
| -5          | 0        | null |

- A polynomial can also be represented using an array, where each element of the array stores the coefficient of a term, and the index of the element corresponds to the exponent of the term. For example, the polynomial 3x^2 + 2x - 5 can be represented by the array:

| Index | 0  | 1 | 2  |
| ----- | -- | - | -- |
| Value | -5 | 2 | 3  |

- The array representation has the advantage of random access and efficient memory allocation, but the disadvantage of limited size and difficulty in handling sparse polynomials (polynomials with many zero coefficients).
- The linked list representation has the advantage of flexibility and ease of handling sparse polynomials, but the disadvantage of memory overhead and sequential access.
- Some common operations on polynomials are:
  - Addition: adding two polynomials by adding the coefficients of the corresponding terms and creating a new polynomial with the resulting coefficients and exponents. For example, (3x^2 + 2x - 5) + (4x^3 - x + 1) = (4x^3 + 3x^2 + x - 4).
  - Subtraction: subtracting two polynomials by subtracting the coefficients of the corresponding terms and creating a new polynomial with the resulting coefficients and exponents. For example, (3x^2 + 2x -



## Unit 3 - Searching and Sorting Algorithms

### Concept of Searching
- Searching is the process of finding an element or a value in a data structure, such as an array or a list.
- Searching algorithms are designed to check for an element or retrieve an element from any data structure where it is used.
- Based on the type of operations, searching algorithms are generally classified into two categories:
  - Sequential search: The algorithm checks each element in the data structure one by one until it finds the target element or reaches the end of the data structure.
  - Binary search: The algorithm divides the sorted data structure into two halves and compares the target element with the middle element of each half. It repeats this process until it finds the target element or the data structure becomes empty.

### Concept of Hashing and Collision Resolution Techniques
- Hashing is a technique of mapping a large set of data elements to a smaller set of data elements, called hash table, using a function called hash function.
- Hashing is useful for fast and efficient search, insertion and deletion operations on the data elements.
- A collision occurs when two or more data elements are mapped to the same location in the hash table by the hash function.
- Collision resolution techniques are methods to handle the collisions and store the data elements in the hash table without losing any information.
- Some common collision resolution techniques are:
  - Linear probing: The algorithm tries to find the next available location in the hash table by moving linearly from the original location until it finds an empty slot or reaches the end of the hash table.
  - Quadratic probing: The algorithm tries to find the next available location in the hash table by moving quadratically from the original location until it finds an empty slot or reaches the end of the hash table.
  - Chaining: The algorithm uses a linked list to store the data elements that are mapped to the same location in the hash table. Each location in the hash table contains a pointer to the head of the linked list.

### Concept of Sorting
- Sorting is the process of arranging a set of data elements in a certain order, such as ascending or descending order.
- Sorting algorithms are algorithms that put elements of a list in a certain order.
- Efficient sorting is important for optimizing the efficiency of other algorithms (such as search and merge algorithms) that require input data to be in sorted lists.
- Some common sorting algorithms are :
  - Insertion sort: The algorithm iterates over the list and inserts each element into its correct position in the sorted part of the list.
  - Selection sort: The algorithm iterates over the list and selects the smallest (or largest) element and swaps it with the first (or last) element of the list. It repeats this process for the remaining unsorted part of the list.
  - Bubble sort: The algorithm iterates over the list and compares each pair of adjacent elements and swaps them if they are in the wrong order. It repeats this process until no swaps are needed.
  - Quick sort: The algorithm chooses a pivot element from the list and partitions the list into two sublists, one with elements smaller than the pivot and one with elements larger than the pivot. It then recursively sorts the sublists using the same method.
  - Merge sort: The algorithm divides the list into two halves and recursively sorts each half using the same method. It then merges the two sorted halves into one sorted list.
  - Heap sort: The algorithm builds a heap (a binary tree where each node is larger than its children) from the list and repeatedly removes the largest element from the heap and places it at the end of the list. It repeats this process until the heap is empty.
  - Radix sort: The algorithm sorts the list based on the individual digits or characters of the elements, starting from the least significant digit or character and moving to the most significant digit or character.



### Concept of Searching

- Searching is the process of finding a given value position in a list of values.
- It decides whether a search key is present in the data or not.
- It is the algorithmic process of finding a particular item in a collection of items.
- It can be done on internal data structure or on external data structure.
- Searching in data structure can be done by applying searching algorithms to check for or extract the desired information from the set of items stored in the form of elements in the computer memory.
- These sets of items are in various forms, such as an array, tree, graph, or linked list.
- Based on the type of search operation, these algorithms are generally classified into two categories: Sequential Search and Binary Search.

### Sequential Search

- Sequential Search is a method of searching where the list or array is traversed sequentially and every element is checked.
- It has the best case time complexity of O(1) when the element is present at the first position.
- It has the worst case time complexity of O(n) when the element is present at the last position or not present at all.
- It is also known as Linear Search or Serial Search.
- It is a simple and easy to implement algorithm, but it is inefficient for large lists.
- It can be applied to any type of list, whether sorted or unsorted, fixed or variable length.

### Index Sequential Search

- Index Sequential Search is a method of searching where the list is divided into smaller sublists, each of which has an index associated with it.
- The index contains the first element and the last element of each sublist.
- The index is searched first using binary search to find the sublist that may contain the element.
- Then, the sublist is searched using sequential search to find the exact position of the element.
- It has the best case time complexity of O(1) when the element is present at the first position of the first sublist.
- It has the worst case time complexity of O(log n + k) where n is the number of sublists and k is the size of the sublist.
- It is also known as Indexed Linear Search or Indexed Sequential Access Method (ISAM).
- It is an improvement over sequential search, but it requires extra space for the index and it is not suitable for dynamic lists.
- It can be applied to sorted lists of fixed length.

### Binary Search

- Binary Search is a method of searching where the list is divided into two halves repeatedly until the element is found or the list is exhausted.
- The list must be sorted in ascending or descending order before applying binary search.
- The middle element of the list is compared with the search key and based on the result, the search is continued in the left half or the right half of the list.
- It has the best case time complexity of O(1) when the element is present at the middle position of the list.
- It has the worst case time complexity of O(log n) where n is the number of elements in the list.
- It is also known as Half-Interval Search or Logarithmic Search.
- It is a fast and efficient algorithm, but it requires the list to be sorted and it is not suitable for dynamic lists.
- It can be applied to sorted lists of any length.



### Sequential Search

- Sequential search is the most natural searching method. In this method, the searching begins with searching every element of the list till the required record is found.
- Sequential search is also known as linear search, as it scans the list or array linearly from the first element to the last element .
- The average number of comparisons in a sequential search is (N+1)/2 where N is the size of the array.
- The best case of sequential search is when the target element is the first element in the list, which requires only one comparison. The worst case is when the target element is not in the list or the last element in the list, which requires N comparisons.
- The time complexity of sequential search is O(N) in the worst case and O(1) in the best case, where N is the number of elements in the list.
- The advantage of sequential search is that it is simple and easy to implement. It does not require any sorting or ordering of the list. It can be used for any type of data.
- The disadvantage of sequential search is that it is slow and inefficient for large lists. It does not take advantage of any structure or property of the data.

: https://stacktips.com/articles/sequential-search-algorithm-in-data-structure
: https://www.careerride.com/Data-structure-sequential-search.aspx
: https://www.geeksforgeeks.org/linear-search/



### Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database .
- An index file is a data structure that contains references to a group of records or blocks in the array or database, based on some key values .
- The index file is searched first using a suitable algorithm, such as binary search, to find the index that points to the block that contains the desired record .
- Then, the block is searched sequentially to locate the record within the block .
- Index sequential search reduces the number of comparisons and disk accesses required to find a record, compared to a simple sequential search .
- However, index sequential search also has some drawbacks, such as the extra space and time required to create and maintain the index file, and the possibility of index overflow if the index file grows too large .

### Example of Index Sequential Search

- Suppose we have an array of 100 records, sorted by a numeric key, and we want to search for the record with the key 75.
- We can create an index file that contains 10 entries, each pointing to a block of 10 records in the array, as shown below:

| Index | Key | Block |
| ----- | --- | ----- |
| 1     | 10  | 1-10  |
| 2     | 20  | 11-20 |
| 3     | 30  | 21-30 |
| 4     | 40  | 31-40 |
| 5     | 50  | 41-50 |
| 6     | 60  | 51-60 |
| 7     | 70  | 61-70 |
| 8     | 80  | 71-80 |
| 9     | 90  | 81-90 |
| 10    | 100 | 91-100|

- We can use binary search to find the index that contains the key 75, which is index 8 with the key 80.
- Then, we can search the block 71-80 sequentially to find the record with the key 75, which is the fifth record in the block.
- The total number of comparisons required for this search is log2(10) + 5 = 8, which is much less than the 75 comparisons required for a simple sequential search.



### Binary Search

- Binary search is an efficient algorithm for finding an element within a sorted array.   
- Binary search works by repeatedly dividing in half the portion of the list that could contain the element, until you've narrowed down the possible locations to just one. 
- Binary search compares the element to the middle element of the array. If they are not equal, the half in which the element cannot lie is eliminated and the search continues on the remaining half, again taking the middle element and comparing it until the element is found. 
- Binary search has a time complexity of O(log n), where n is the number of elements in the array.  
- Binary search requires that the array is sorted in ascending or descending order. If the array is not sorted, binary search cannot be applied.  
- Binary search can be implemented using an iterative or a recursive approach. The iterative approach uses a loop to repeatedly check and update the search bounds, while the recursive approach uses a function that calls itself with new bounds.  
- Binary search is useful for building more complex algorithms in computer science, such as interpolation search, exponential search, and binary search trees.



### Concept of Hashing & Collision resolution Techniques used in Hashing

- Hashing is a technique of mapping a set of keys to a set of values using a hash function.
- A hash function is a function that takes a key as input and returns an integer value, called a hash value or a hash code, as output.
- A hash table is a data structure that stores key-value pairs in an array, using the hash values as indices.
- Hashing is useful for fast and efficient searching, insertion and deletion of data in a large collection of items.
- However, hashing may cause collisions, which occur when two or more keys have the same hash value and map to the same slot in the hash table.
- Collision resolution techniques are methods to handle collisions and avoid data loss or corruption in the hash table.
- There are two main types of collision resolution techniques: open hashing and closed hashing.

#### Open Hashing (Separate Chaining)

- In open hashing, each slot in the hash table contains a pointer to a linked list of key-value pairs that have the same hash value.
- To insert a new key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, a new linked list is created and the key-value pair is added as the first node. If the slot is not empty, the key-value pair is appended to the existing linked list.
- To search for a key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key is not found. If the slot is not empty, the linked list is traversed until the key is found or the end of the list is reached.
- To delete a key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key is not found. If the slot is not empty, the linked list is traversed until the key is found or the end of the list is reached. If the key is found, the node is removed from the list and the memory is freed. If the key is not found, no action is taken.
- The advantage of open hashing is that it can handle any number of collisions and the hash table size does not need to be fixed or large.
- The disadvantage of open hashing is that it requires extra space for the linked lists and the performance may degrade if the lists become too long.

#### Closed Hashing (Open Addressing)

- In closed hashing, each slot in the hash table can store only one key-value pair and there are no pointers or linked lists.
- To insert a new key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key-value pair is stored in the slot. If the slot is not empty, a collision has occurred and a different slot is probed until an empty slot is found or the entire table is full.
- To search for a key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key is not found. If the slot is not empty, the key is compared with the stored key. If they match, the value is returned. If they do not match, a collision has occurred and a different slot is probed until the key is found or an empty slot is reached.
- To delete a key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key is not found. If the slot is not empty, the key is compared with the stored key. If they match, the slot is marked as deleted. If they do not match, a collision has occurred and a different slot is probed until the key is found or an empty slot is reached.
- The advantage of closed hashing is that it does not require extra space and the access time is constant if there are no collisions.
- The disadvantage of closed hashing is that it has a limited capacity and the performance may degrade if the load factor (the ratio of the number of keys to the table size) is high.

##### Collision Resolution Techniques in Closed Hashing

- There are different ways to probe for an empty slot in closed hashing, such as linear probing, quadratic probing, double hashing, etc.
- Linear probing: In linear probing, the next slot in the hash table is probed if the current slot is occupied. If the end of the table is reached, the probing wraps around to the beginning of the table. The probe sequence is given by:

    ```
    h(k

```




### Sorting: Insertion Sort, Selection, Bubble Sort, Quick Sort, Merge Sort, Heap Sort and Radix Sort

- Sorting is the process of arranging the elements of an array or list in a specific order, such as ascending or descending, based on a comparison operator.
- Sorting algorithms are the methods or techniques used to implement sorting in data structures.
- Sorting algorithms can be classified into different categories based on their time complexity, space complexity, stability, adaptability, recursion, and comparison.
- Some of the common types of sorting algorithms are:

  - **Insertion Sort**: This algorithm works by inserting each element of the array into its correct position in a sorted subarray. It starts with the first element as the sorted subarray and then compares the next element with the sorted subarray and inserts it into the appropriate position. It repeats this process until the whole array is sorted .
  - **Selection Sort**: This algorithm works by selecting the smallest or largest element of the array and swapping it with the first or last element of the unsorted subarray. It then reduces the size of the unsorted subarray by one and repeats the process until the whole array is sorted .
  - **Bubble Sort**: This algorithm works by comparing each pair of adjacent elements of the array and swapping them if they are in the wrong order. It then moves to the next pair and repeats the process until the whole array is sorted. It is called bubble sort because the smaller or larger elements bubble up to the top or bottom of the array .
  - **Quick Sort**: This algorithm works by choosing a pivot element from the array and partitioning the array into two subarrays such that all the elements less than or equal to the pivot are in the left subarray and all the elements greater than the pivot are in the right subarray. It then recursively sorts the left and right subarrays using the same method. It is called quick sort because it is faster than other sorting algorithms on average .
  - **Merge Sort**: This algorithm works by dividing the array into two halves of equal or nearly equal sizes. It then recursively sorts the two halves using the same method. It then merges the two sorted halves into one sorted array using a merge function. It is called merge sort because it merges the sorted subarrays into one sorted array  .
  - **Heap Sort**: This algorithm works by building a heap data structure from the array. A heap is a complete binary tree where each node is either greater than or equal to (max heap) or less than or equal to (min heap) its children. It then repeatedly removes the root node of the heap and places it at the end of the sorted subarray. It then restores the heap property by adjusting the remaining nodes. It is called heap sort because it uses a heap data structure to sort the array .
  - **Radix Sort**: This algorithm works by sorting the array based on the individual digits or characters of the elements. It starts with the least significant digit or character and sorts the array using a stable sorting algorithm, such as counting sort. It then moves to the next significant digit or character and repeats the process until the whole array is sorted. It is called radix sort because it sorts the array based on the radix or base of the elements .

: https://www.geeksforgeeks.org/sorting-algorithms/
: https://www.upgrad.com/blog/sorting-in-data-structure-with-examples/
: https://cselectricalandelectronics.com/sorting-in-data-structure-and-algorithms-code-working-types-of-sorting/
: https://www.programiz.com/dsa/sorting-algorithm
: https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/



## Unit 4 - Graphs

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. A graph can be used to model many types of problems, such as networks, maps, games, social networks, etc.

Some of the terminology used with graphs are:

- **Degree of a vertex**: The number of edges incident to a vertex.
- **Parallel edges**: Two or more edges that connect the same pair of vertices.
- **Self-loop**: An edge that connects a vertex to itself.
- **Simple graph**: A graph that has no parallel edges or self-loops.
- **Multigraph**: A graph that may have parallel edges or self-loops.
- **Directed graph**: A graph in which each edge has a direction, from one vertex to another.
- **Undirected graph**: A graph in which each edge has no direction, and can be traversed in either way.
- **Weighted graph**: A graph in which each edge has a numerical value (or weight) associated with it.
- **Path**: A sequence of vertices and edges that connects two vertices in a graph.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected graph**: A graph in which there is a path between any two vertices.
- **Disconnected graph**: A graph that is not connected.
- **Subgraph**: A graph that is formed by a subset of vertices and edges of another graph.
- **Complete graph**: A graph in which there is an edge between every pair of vertices.
- **Bipartite graph**: A graph in which the vertices can be divided into two disjoint sets, such that there is no edge between vertices in the same set.
- **Tree**: A connected, undirected graph that has no cycles.
- **Forest**: A collection of trees.

There are different ways to represent a graph in a computer, such as:

- **Adjacency matrix**: A two-dimensional array of size n x n, where n is the number of vertices in the graph. The element at row i and column j is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, the adjacency matrix is symmetric. For a weighted graph, the element at row i and column j is the weight of the edge from vertex i to vertex j, and 0 if there is no edge. The space complexity of this representation is O(n^2), where n is the number of vertices in the graph.
- **Adjacency list**: An array of lists, where each list corresponds to a vertex in the graph. The list at index i contains the vertices that are adjacent to vertex i, along with their weights if the graph is weighted. The space complexity of this representation is O(n + m), where n is the number of vertices and m is the number of edges in the graph.
- **Adjacency map**: A variation of the adjacency list, where each list is replaced by a map (or a dictionary or a hash table) that maps the adjacent vertices to their weights. This allows for faster access and update of the weights, but may require more space than the adjacency list.

Graph traversal is the process of visiting all the vertices and edges of a graph in a systematic way. There are two common methods of graph traversal:

- **Depth-first search (DFS)**: A recursive algorithm that starts from a given vertex and explores as far as possible along each branch before backtracking. It uses a stack (or the call stack) to keep track of the vertices to visit. The time complexity of DFS is O(n + m), where n is the number of vertices and m is the number of edges in the graph.
- **Breadth-first search (BFS)**: An iterative algorithm that starts from a given vertex and explores all the vertices at the same distance from the source before moving to the next level. It uses a queue to keep track of the vertices to visit. The time complexity of BFS is O(n + m), where n is the number of vertices and m is the number of edges in the graph.

Some of the applications of graph traversal are:

- **Connected component**: A subgraph of a graph that is connected. To find the connected components of a graph, we can perform DFS or BFS from any vertex and mark all the vertices that are visited. Then, we can repeat the process for any unmarked vertex until all the vertices are marked. The number of times we perform DFS or BFS is the number of connected components in the graph.
- **Spanning tree**: A subgraph of a graph that is a tree and contains all the vertices of the graph. To find a spanning tree of a graph, we can perform DFS



### Terminology used with Graph

- A **graph** is a collection of **vertices** (also called nodes or points) and **edges** (also called arcs or lines) that connect the vertices.
- A graph can be **directed** or **undirected**. A directed graph has edges that are associated with a direction, meaning that they can only be traversed in one way. An undirected graph has edges that are bidirectional, meaning that they can be traversed in both ways.
- A graph can be **weighted** or **unweighted**. A weighted graph has edges that are assigned a numerical value, called the **weight** or **cost**, that represents some attribute of the edge, such as distance, time, or capacity. An unweighted graph has edges that are not assigned any weight.
- A graph can be **simple** or **non-simple**. A simple graph has no **loops** (edges that connect a vertex to itself) and no **multiple edges** (more than one edge between the same pair of vertices). A non-simple graph may have loops and/or multiple edges.
- A graph can be **cyclic** or **acyclic**. A cyclic graph has at least one **cycle** (a path that starts and ends at the same vertex and has no repeated vertices or edges). An acyclic graph has no cycles.
- A graph can be **connected** or **disconnected**. A connected graph has a **path** (a sequence of vertices and edges) between any pair of vertices. A disconnected graph has at least one pair of vertices that are not connected by a path.
- A **subgraph** of a graph is a graph that consists of a subset of the vertices and edges of the original graph. A subgraph is said to be **induced** if it contains all the edges between the vertices in the subset.
- A **degree** of a vertex in a graph is the number of edges incident to that vertex. In a directed graph, the degree can be divided into **in-degree** (the number of edges entering the vertex) and **out-degree** (the number of edges leaving the vertex).
- A **walk** in a graph is a sequence of vertices and edges that starts and ends at any vertex and allows repeated vertices and edges. A walk is said to be **closed** if it starts and ends at the same vertex.
- A **trail** in a graph is a walk that does not repeat any edge. A trail is said to be **Eulerian** if it contains every edge of the graph exactly once.
- A **path** in a graph is a walk that does not repeat any vertex. A path is said to be **Hamiltonian** if it contains every vertex of the graph exactly once.
- A **circuit** in a graph is a closed trail. A circuit is said to be **Eulerian** if it is also Eulerian as a trail.
- A **cycle** in a graph is a closed path. A cycle is said to be **Hamiltonian** if it is also Hamiltonian as a path.
- A **tree** is a connected acyclic graph. A tree is said to be **rooted** if one of its vertices is designated as the **root** and every edge is directed away from the root.
- A **forest** is a graph that consists of one or more trees. A forest is said to be **rooted** if each of its trees is rooted.
- A **spanning tree** of a graph is a subgraph that is a tree and contains all the vertices of the original graph. A graph may have more than one spanning tree.
- A **minimum spanning tree** of a weighted graph is a spanning tree that has the minimum possible sum of edge weights among all the spanning trees of the graph. A weighted graph may have more than one minimum spanning tree.

