### Operations on functions

- A function is a relation that assigns to each element of a set A (called the domain) exactly one element of a set B (called the codomain).
- A function can be represented by a set of ordered pairs, a table, a graph, or a formula.
- The notation f: A -> B means that f is a function from A to B.
- The notation f(a) = b means that b is the value of the function f at a, or the image of a under f.
- The notation f(A) = {f(a) | a in A} means the image of the set A under f, or the set of all values of f at elements of A.
- The notation f^-1(b) = {a in A | f(a) = b} means the preimage of b under f, or the set of all elements of A that map to b under f.
- The notation f^-1(B) = {a in A | f(a) in B} means the preimage of the set B under f, or the set of all elements of A that map to elements of B under f.

Some common operations on functions are:

- Composition: The composition of two functions f and g, denoted by f o g, is the function that maps x to f(g(x)). That is, f o g(x) = f(g(x)) for all x in the domain of g. The domain of f o g is the set of all x in the domain of g such that g(x) is in the domain of f.
- Inverse: The inverse of a function f, denoted by f^-1, is the function that maps y to x if and only if f(x) = y. That is, f^-1(y) = x if and only if f(x) = y for all x in the domain of f and y in the codomain of f. The inverse of f exists if and only if f is one-to-one and onto, meaning that f maps each element of A to a unique element of B and covers all elements of B. The domain of f^-1 is the codomain of f, and the codomain of f^-1 is the domain of f. The inverse of f satisfies the property that f o f^-1 = f^-1 o f = I, where I is the identity function that maps x to x.
- Restriction: The restriction of a function f to a subset A of its domain, denoted by f|A, is the function that maps x to f(x) for all x in A. That is, f|A(x) = f(x) for all x in A. The domain of f|A is A, and the codomain of f|A is the same as the codomain of f. The restriction of f to A is a function from A to B.
- Extension: The extension of a function f from a subset A of a set X to the whole set X, denoted by f^X, is the function that maps x to f(x) for all x in A, and to some arbitrary value for all x in X - A. That is, f^X(x) = f(x) for all x in A, and f^X(x) = c for some constant c for all x in X - A. The domain of f^X is X, and the codomain of f^X is the same as the codomain of f. The extension of f from A to X is a function from X to B.