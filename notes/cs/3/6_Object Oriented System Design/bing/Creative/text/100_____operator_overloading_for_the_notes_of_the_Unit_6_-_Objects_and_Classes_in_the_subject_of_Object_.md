### Operator Overloading

- Operator overloading is a feature of object-oriented programming languages that allows the definition of new behaviors for existing operators when applied to user-defined types, such as classes or structs.
- Operator overloading can improve the readability, expressiveness, and consistency of the code, by allowing the use of familiar syntax for custom data types.
- Operator overloading can also enable polymorphism, by allowing different types to implement the same operator with different semantics, depending on the context.
- Operator overloading is not a mandatory feature of object-oriented programming languages, and some languages do not support it at all, such as Java or Python. Other languages, such as C++, C#, or Ruby, support it to varying degrees, with different rules and restrictions.
- Operator overloading should be used with caution, as it can introduce ambiguity, confusion, or unexpected behavior if not implemented correctly or consistently. Some general guidelines for using operator overloading are:

  - Only overload operators that have a clear and intuitive meaning for the type, and avoid changing the original semantics or precedence of the operator.
  - Ensure that the operator overloading is consistent with the existing operators and types in the language, and follows the principle of least surprise for the users of the type.
  - Avoid overloading operators that have side effects, such as assignment or increment operators, as they can violate the principle of referential transparency and cause bugs or errors.
  - Provide the corresponding operators for symmetry and completeness, such as equality and inequality, addition and subtraction, etc.
  - Prefer to overload operators as member functions for unary operators, and as non-member functions for binary operators, to allow implicit conversions and better readability.