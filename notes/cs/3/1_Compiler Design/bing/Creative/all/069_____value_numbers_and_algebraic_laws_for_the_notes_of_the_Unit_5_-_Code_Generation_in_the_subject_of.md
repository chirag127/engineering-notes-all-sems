# Value Numbers and Algebraic Laws

- Value numbers are numbers assigned to each expression or variable in a program to identify equivalent computations and eliminate redundant ones.
- Value numbers are computed by traversing the program's control flow graph in a dominator-based order and applying a hash function to each expression or variable.
- Value numbers can be used to implement local and global common subexpression elimination, copy propagation, constant folding, and partial redundancy elimination.
- Algebraic laws are rules that describe the properties of mathematical operations and expressions, such as commutativity, associativity, distributivity, and identity.
- Algebraic laws can be used to simplify expressions and optimize code generation by applying algebraic transformations, such as x = x * 1 -> x = x, x + y = y + x, x * (y + z) = x * y + x * z, etc.
- Algebraic laws can also be used to detect and eliminate strength-reducing operations, such as x * 2 -> x + x, x / 2 -> x >> 1, x * 4 -> x << 2, etc.
- Algebraic laws can be applied to expressions with the same value number, as they are guaranteed to be equivalent for all possible program inputs.