Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of operations on functions for the unit 1 - set theory in the subject of discrete structures and theory of logic.

# Operations on Functions

- A function is a relation that assigns to each element of a set A (called the domain) exactly one element of a set B (called the co-domain).
- A function can be represented by a set of ordered pairs, a table, a graph, or an algebraic expression.
- The notation f: A -> B means that f is a function from A to B.
- The notation f(a) = b means that b is the value of the function f at a, or the image of a under f.
- The notation f(A) = {f(a) | a in A} means the image of the set A under f, or the set of all values of f at elements of A.
- The notation f^-1(b) = {a in A | f(a) = b} means the pre-image of b under f, or the set of all elements of A that are mapped to b by f.
- The notation f^-1(B) = {a in A | f(a) in B} means the pre-image of the set B under f, or the set of all elements of A that are mapped to elements of B by f.

## Operations on Functions

- There are four main operations on functions: composition, inverse, restriction, and extension.
- The composition of two functions f: A -> B and g: B -> C is a function g o f: A -> C that maps each element of A to the value of g at the value of f at that element. That is, (g o f)(a) = g(f(a)) for all a in A.
- The inverse of a function f: A -> B is a function f^-1: B -> A that maps each element of B to an element of A that is mapped to it by f. That is, f^-1(b) = a if and only if f(a) = b for some a in A. A function is invertible if and only if it is one-to-one and onto, meaning that it maps different elements of A to different elements of B, and it maps every element of B to some element of A.
- The restriction of a function f: A -> B to a subset C of A is a function f|C: C -> B that maps each element of C to the same value as f. That is, f|C(c) = f(c) for all c in C. The restriction of f to C is also a function from C to f(C), the image of C under f.
- The extension of a function f: A -> B to a superset D of A is a function f': D -> B that maps each element of D to the same value as f if it is in A, and to some arbitrary value otherwise. That is, f'(d) = f(d) if d in A, and f'(d) = b for some b in B if d not in A. The extension of f to D is not unique, as there may be more than one way to assign values to elements of D that are not in A.