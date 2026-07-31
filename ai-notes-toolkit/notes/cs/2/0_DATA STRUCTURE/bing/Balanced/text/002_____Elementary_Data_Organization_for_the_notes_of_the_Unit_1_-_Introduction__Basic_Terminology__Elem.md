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