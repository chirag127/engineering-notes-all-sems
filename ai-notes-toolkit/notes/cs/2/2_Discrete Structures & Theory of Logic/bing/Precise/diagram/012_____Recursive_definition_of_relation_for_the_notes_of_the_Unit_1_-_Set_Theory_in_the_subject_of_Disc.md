### Recursive definition of relation for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

A recursive definition of a relation is a definition that defines a relation in terms of itself. This type of definition is used to define relations that have a repetitive or self-referential structure. 

Here are the key points to remember about recursive definitions of relations:

1. A recursive definition of a relation consists of two parts: a base case and a recursive step.
2. The base case specifies the initial values of the relation.
3. The recursive step specifies how the relation can be extended from the values already defined.
4. The recursive step must be well-defined, meaning that it must specify a unique value for the relation for each possible input.
5. A recursive definition must always have a base case, otherwise the definition would not be well-defined.
6. The recursive step must eventually reach the base case, otherwise the definition would not be well-defined.

An example of a recursive definition of a relation is the definition of the ancestor relation in a family tree. The base case specifies that a person is their own ancestor. The recursive step specifies that if person A is an ancestor of person B, and person B is an ancestor of person C, then person A is also an ancestor of person C. This definition allows us to determine whether one person is an ancestor of another by following the chain of ancestor relationships up the family tree until we reach the base case.