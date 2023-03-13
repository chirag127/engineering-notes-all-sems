First-order logic is a formal system for representing and reasoning about natural language semantics. It consists of a syntax for writing logical expressions, and a semantics for interpreting them. A logical expression can be composed of constants, variables, predicates, functions, quantifiers, and logical connectives.

The following diagram illustrates the basic components of a first-order logic expression using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Constants    |    |    Variables    |    |   Predicates    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Symbols that   |    |  Symbols that   |    |  Symbols that   |
|  denote fixed   |    |  denote unknown |    |  denote sets of |
|  entities in    |    |  or arbitrary   |    |  entities that  |
|  the domain     |    |  entities in    |    |  have some      |
|                 |    |  the domain     |    |  property or    |
|  Examples:      |    |                 |    |  relation        |
|  John, Mary,    |    |  Examples:      |    |                 |
|  42, red, etc.  |    |  x, y, z, etc.  |    |  Examples:      |
|                 |    |                 |    |  loves, is_a,   |
+-----------------+    +-----------------+    |  greater_than,  |
                                               |  etc.           |
                                               |                 |
                                               +-----------------+
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Functions     |    |   Quantifiers   |    | Logical         |
|                 |    |                 |    | Connectives     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Symbols that   |    |  Symbols that   |    |  Symbols that   |
|  denote         |    |  denote the     |    |  denote logical |
|  mappings from  |    |  scope or       |    |  operations on  |
|  entities to    |    |  quantity of    |    |  logical        |
|  entities       |    |  entities       |    |  expressions    |
|                 |    |                 |    |                 |
|  Examples:      |    |  Examples:      |    |  Examples:      |
|  father_of,     |    |  forall,        |    |  and, or, not,  |
|  square_root,   |    |  exists, etc.   |    |  implies, etc.  |
|  etc.           |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

A first-order logic expression can be written using a combination of these components, following some rules of syntax. For example, the expression `forall x. (is_a(x, human) implies loves(x, chocolate))` means that for every entity x, if x is a human, then x loves chocolate. The expression `exists y. (is_a(y, dog) and loves(John, y))` means that there is some entity y, such that y is a dog and John loves y. The expression `father_of(father_of(John))` means the father of the father of John.