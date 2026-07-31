# Value Numbers and Algebraic Laws

- Value numbers are numbers assigned to each expression or variable in a basic block that indicate the equivalence of expressions or variables.
- Value numbers can be used to eliminate redundant computations by replacing expressions or variables with the same value number.
- Value numbers can be computed by a local algorithm that traverses the basic block in a forward direction and assigns value numbers based on the operator and operands of each expression or variable.
- Value numbers can also be computed by a global algorithm that traverses the dominator tree of the control flow graph and assigns value numbers based on the congruence classes of expressions or variables.
- Algebraic laws are rules that describe the properties of arithmetic and logical operations, such as commutativity, associativity, distributivity, identity, inverse, etc.
- Algebraic laws can be used to simplify or transform expressions or variables to a canonical form that is easier to analyze or optimize.
- Algebraic laws can also be used to identify and eliminate common subexpressions or strength-reduce expressions by replacing expensive operations with cheaper ones.