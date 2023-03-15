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