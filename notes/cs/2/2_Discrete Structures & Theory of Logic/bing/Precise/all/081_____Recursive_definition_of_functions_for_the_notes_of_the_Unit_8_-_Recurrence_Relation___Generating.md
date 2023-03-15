### Recursive definition of functions

A recursive definition of a function is a definition that defines the value of the function for some inputs in terms of the values of the function for other inputs. This is done by specifying a base case and a recursive step.

1. **Base case:** The base case specifies the value of the function for one or more specific inputs. These inputs are usually the smallest or simplest inputs for which the function is defined.

2. **Recursive step:** The recursive step specifies how to compute the value of the function for an input in terms of the values of the function for smaller or simpler inputs. This is done by expressing the function in terms of itself, but with smaller or simpler inputs.

For example, consider the factorial function, which is defined as the product of all positive integers less than or equal to n. The recursive definition of the factorial function is as follows:

1. **Base case:** 0! = 1
2. **Recursive step:** n! = n * (n-1)!, for n > 0

In this definition, the base case specifies the value of the function for the input 0, and the recursive step specifies how to compute the value of the function for any positive integer n in terms of the value of the function for n-1.

Recursive definitions are commonly used in computer science and mathematics to define functions, sequences, and other mathematical objects. They provide a powerful and concise way to specify complex behavior in terms of simpler behavior.