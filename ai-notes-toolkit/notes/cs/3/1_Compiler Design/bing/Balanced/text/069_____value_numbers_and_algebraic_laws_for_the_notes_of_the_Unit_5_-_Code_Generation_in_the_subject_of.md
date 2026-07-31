### Value Numbers and Algebraic Laws

- Value numbers are a technique for identifying and eliminating redundant computations in a program.
- A value number is a unique identifier assigned to each expression in a basic block, such that two expressions have the same value number if they are guaranteed to have the same value for all possible inputs.
- Value numbers can be computed using a hash-based algorithm or a partitioning algorithm, both of which traverse the dominator tree of the program and use a data structure to store the value numbers of expressions.
- Algebraic laws are rules that describe the properties of mathematical operations, such as commutativity, associativity, distributivity, identity, and inverse.
- Algebraic laws can be used to simplify expressions, rewrite expressions in a canonical form, and detect equivalent expressions.
- Algebraic laws can be applied to expressions before or after assigning value numbers, depending on the optimization goal and the complexity of the laws.
- Some examples of algebraic laws are:

  - x + 0 = x
  - x * 1 = x
  - x + y = y + x
  - x * y = y * x
  - (x + y) + z = x + (y + z)
  - (x * y) * z = x * (y * z)
  - x * (y + z) = x * y + x * z
  - x / x = 1
  - x - x = 0
  - x ^ 0 = 1
  - x ^ 1 = x
  - x ^ -1 = 1 / x