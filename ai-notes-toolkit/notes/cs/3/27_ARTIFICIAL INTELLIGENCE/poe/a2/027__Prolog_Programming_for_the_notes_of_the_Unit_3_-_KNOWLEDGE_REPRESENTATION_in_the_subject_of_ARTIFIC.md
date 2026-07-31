 Here is the content in Markdown format without any emojis or external links:

### Prolog Programming for the notes of the Unit 3 - KNOWLEDGE REPRESENTATION in the subject of ARTIFICIAL INTELLIGENCE KCS.

- Prolog is a logic programming language associated with artificial intelligence and computational linguistics.
- Prolog has its roots in first-order logic, a formal logic, and unlike many other programming languages, Prolog is intended primarily as a declarative programming language.
- A Prolog program is a set of factual statements about relationships. Execution is initiated by running queries over these statements.
- The core of the Prolog language consists of two main components:

1. A database (or knowledge base) comprising facts and rules
2. An inference engine that can activate rules and make deductions based on the database.

- Facts in Prolog are statements that are always true. They are of the form:

parent(tom, sarah).

- This states that tom is sarah's parent.
- Rules in Prolog are statements in the form of logical implications. For example:

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

- This states that X is a grandparent of Z if X is a parent of Y and Y is a parent of Z.
- The inference engine will automatically find all possible solutions (answer substitutions) that satisfy the logical expressions. This is known as forward chaining.

[No emojis or external links included. Content written in points in Markdown format as required.]