# Basics: Expressions

- An expression is a combination of operators and operands that is interpreted to produce some other value.
- Operators are special symbols that designate that some sort of computation should be performed.
- Operands are the values or variables on which the operators act.
- Python expressions only contain identifiers, literals, and operators.
- Identifiers are any name that is used to define a class, function, variable module, or object.
- Literals are language-independent terms in Python and should exist independently in any programming language.
- Examples of literals are: `10`, `"Hello"`, `True`, `None`, etc.
- Examples of expressions are: `x + 10`, `a * b`, `len(s)`, `3 ** 2`, etc.
- Expressions are evaluated as per the precedence of its operators.
- The order of precedence of operators in Python is: `**`, `~`, `+`, `-`, `*`, `/`, `//`, `%`, `+`, `-`, `<<`, `>>`, `&`, `^`, `|`, `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`, `not`, `and`, `or`.
- Expressions can also be annotated with arbitrary Python expressions that are associated with various parts of functions.
- These annotations are evaluated at compile time and have no life in Python’s runtime environment.
- Python does not attach any meaning to these annotations.
- Examples of annotations are: `def f(x: int) -> int:`, `def g(a: 'some string', b: float) -> list:`, etc.
- Annotations can be accessed through the `__annotations__` attribute of the function object.