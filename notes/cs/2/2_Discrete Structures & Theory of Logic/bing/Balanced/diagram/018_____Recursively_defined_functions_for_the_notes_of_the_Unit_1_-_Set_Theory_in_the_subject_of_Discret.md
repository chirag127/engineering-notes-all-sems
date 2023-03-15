Hello, I am Sydney, your AI assistant. I can help you with your study material for Discrete Structures & Theory of Logic. Here is the content for the topic of Recursively defined functions for the notes of the Unit 1 - Set Theory.

### Recursively defined functions

- A recursively defined function is a function that is defined by using its own values in the definition.
- A recursively defined function has two parts: a base case and a recursive step.
- The base case specifies the value of the function for one or more initial inputs, usually the smallest or simplest ones.
- The recursive step specifies how to compute the value of the function for any other input, using the values of the function for smaller or simpler inputs.
- A recursively defined function must have a well-defined domain, which is the set of all possible inputs for which the function is defined.
- A recursively defined function must also satisfy the principle of mathematical induction, which states that if the base case is true and the recursive step is true for any input, then the function is true for all inputs in the domain.
- An example of a recursively defined function is the factorial function, which is defined as follows:

  - Base case: `n! = 1` for `n = 0`
  - Recursive step: `n! = n * (n-1)!` for `n > 0`
  - Domain: The set of all non-negative integers
  - Induction: To prove that the factorial function is true for all non-negative integers, we can use the principle of mathematical induction as follows:

    - Base case: `0! = 1` is true by definition.
    - Inductive step: Assume that `k! = k * (k-1)!` is true for some non-negative integer `k`. Then, we can show that `(k+1)! = (k+1) * k!` is also true by using the recursive step of the factorial function:

      - `(k+1)! = (k+1) * k!` by the recursive step
      - `= (k+1) * k * (k-1)!` by the inductive hypothesis
      - `= (k+1) * k!` by the recursive step
    - Therefore, the factorial function is true for all non-negative integers by the principle of mathematical induction.