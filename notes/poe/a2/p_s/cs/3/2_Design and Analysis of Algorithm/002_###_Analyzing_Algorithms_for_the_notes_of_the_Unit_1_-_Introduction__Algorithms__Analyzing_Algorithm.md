 Here is the content in markdown format for the given topic:

### Analyzing Algorithms

- An algorithm is a step-by-step procedure for solving a problem or completing a task.
- To analyze an algorithm, we determine the number of steps required for the algorithm as a function of the size of the input.
- The run time of an algorithm depends on two things:
    - The number of steps (operations) in the algorithm.
    - The time required for each step (which depends on the particular computer/hardware).
- We normally ignore the second factor and count only the number of steps as a measure of efficiency. This gives us an upper bound on the run time.
- For example, if an algorithm takes n steps for an input of size n, we say it is linear or O(n). If it takes n2 steps, we say it is quadratic or O(n2).

- Complexity of Algorithms:
    - The time/space complexity gives an upper bound on the run time/space usage of an algorithm. It describes the worst-case scenario.
    - Commonly used complexities (in increasing order):
        - Constant (O(1)) - Doesn't depend on input size.
        - Logarithmic (O(log n)) - Grows slowly. Example: binary search.
        - Linear (O(n)) - Grows directly proportional to input.
        - Quadratic (O(n2)) - Grows quickly. Example: bubble sort.
        - Exponential (O(2n)) - Grows very quickly. Example: brute-force search.
    - We drop lower-order terms and coefficients to get the complexity in big O notation.

[Detailed content with diagrams and examples can be added here for the sub-topics]

- Performance Measurements:
    - Running time - Amount of time taken by an algorithm to execute. Measured in seconds.
    - Space usage - Additional storage space required by an algorithm. Measured in bytes.
- Sorting and Order Statistics:
    - Shell Sort, Quick Sort, Merge Sort, Heap Sort - Comparison of sorting algorithms based on time/space complexity.
    - Sorting in Linear Time - Examples of algorithms with linear time sorting such as counting sort and radix sort.