### Recursive definition of functions

A recursive definition of a function is a way of defining the value of a function for some inputs in terms of the value of the same function for other inputs, usually smaller or simpler. A recursive definition consists of two parts: a base case and a recursive step.

- The base case specifies the value of the function for some simple or trivial inputs, such as zero or one. For example, the factorial function n! is defined by the base case 0! = 1.
- The recursive step specifies how to compute the value of the function for a given input by using the value of the function for a smaller or simpler input. For example, the factorial function n! is defined by the recursive step (n + 1)! = (n + 1)· n !.

A recursive definition of a function is valid if it satisfies the following conditions:

- Every possible input is covered by either the base case or the recursive step.
- There is no infinite chain of recursive calls, that is, every recursive call eventually reaches a base case.
- The value of the function does not depend on the order or the number of recursive calls, that is, the function is well-defined and unambiguous.

Recursive definitions of functions are useful for describing and analyzing algorithms that use recursion, such as sorting, searching, and tree traversal. Recursive definitions of functions can also be used to define mathematical concepts, such as natural numbers, sequences, sets, and relations.