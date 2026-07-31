### Deductive database systems and logic programming systems—differences

Deductive databases have grown out of the desire to combine logic programming with relational databases to construct systems that support a powerful formalism and are still fast and able to deal with very large datasets. Deductive databases are more expressive than relational databases but less expressive than logic programming systems.

However, there are a number of important differences between deductive databases and logic programming systems:

- **Order sensitivity and procedurality**: In Prolog, program execution depends on the order of rules in the program and on the order of parts of rules; these properties are used by programmers to build efficient programs .

- **Special predicates**: In Prolog, programmers can directly influence the procedural evaluation of the program.

Deductive databases offer elegant and powerful ways of managing complex data in a declarative way, especially for information that is derived by use of recursion. Deductive systems typically provide a declarative query language such as a logic programming language (e.g., Prolog).