## Recursion

- Recursion is a technique of defining a problem in terms of itself.
- Recursion involves two main components: a base case and a recursive step.
- A base case is a simple or trivial case of the problem that can be solved directly without recursion.
- A recursive step is a way of reducing a complex or larger case of the problem to one or more simpler or smaller cases that can be solved by applying the same technique recursively.
- A recursive function is a function that calls itself within its body, either directly or indirectly, with different arguments that lead to the base case.
- Recursion can be used to solve problems that have a recursive structure, such as mathematical sequences, tree traversal, backtracking, divide and conquer, dynamic programming, etc.
- Recursion can be implemented using either a stack or a heap data structure to store the function calls and their local variables.
- Recursion can be classified into two types: tail recursion and non-tail recursion.
- Tail recursion is a special case of recursion where the recursive call is the last statement in the function body, and the return value of the recursive call is the same as the return value of the function.
- Non-tail recursion is a general case of recursion where the recursive call is not the last statement in the function body, and the return value of the function may depend on the return value of the recursive call and some other computations.
- Tail recursion can be optimized by the compiler to eliminate the function call overhead and use a constant amount of space, while non-tail recursion may require a linear amount of space proportional to the depth of recursion.
- Recursion can be converted to iteration using a loop and a stack or a queue data structure to simulate the function calls and their local variables.