### Recursively defined functions for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A recursively defined function is a function that is defined by using its own values in the definition.
- A recursively defined function has two parts: a base case and a recursive step.
- The base case specifies the value of the function for one or more initial inputs, usually the smallest or simplest ones.
- The recursive step specifies how to compute the value of the function for any other input, using the values of the function for smaller or simpler inputs.
- A recursively defined function must have a well-defined domain, which is the set of all possible inputs for which the function is defined.
- A recursively defined function must also satisfy the principle of mathematical induction, which states that if the base case is true and the recursive step is true for any input, then the function is true for all inputs in the domain.
- An example of a recursively defined function is the factorial function, which is defined as follows:

  - Base case: `n! = 1` for `n = 0`
  - Recursive step: `n! = n * (n-1)!` for `n > 0`
  - Domain: `n` is a non-negative integer
  - Induction: The base case is true, and the recursive step is true for any `n > 0`, since `(n-1)!` is already defined by the function. Therefore, the function is true for all non-negative integers.

- Another example of a recursively defined function is the Fibonacci sequence, which is defined as follows:

  - Base case: `F(0) = 0` and `F(1) = 1`
  - Recursive step: `F(n) = F(n-1) + F(n-2)` for `n > 1`
  - Domain: `n` is a non-negative integer
  - Induction: The base case is true, and the recursive step is true for any `n > 1`, since `F(n-1)` and `F(n-2)` are already defined by the function. Therefore, the function is true for all non-negative integers.