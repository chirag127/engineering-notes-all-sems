 Here is the content in markdown format without any feeling or friendliness:

### Discrete Logarithmic Problem

- Discrete logarithmic problem is a mathematical problem of finding the exponent x given the base a and the result a^x in a finite group.
- It is easy to compute a^x given a, x but hard to compute x given a, a^x which forms the basis of many public key cryptosystems like ElGamal and DSA.
- The discrete logarithm problem can be stated as: Given a and a^x in a finite group G, find x. This is easy if a has small order but difficult if the order of a is very large.
- The security of discrete logarithm based public key cryptosystems depends on the difficulty of solving discrete logarithmic problem which is a one-way function.
- Discrete logarithm is easy to compute if a is a primitive root of the group order n. So, for security a should not be a primitive root of n.
- The best known general techniques to solve discrete logarithm problem are exhaustive search and index calculus methods. But for large group order, these techniques take exponential time.
- Hence, discrete logarithm problem is considered computationally infeasible for large group order and provides the basis for secure public key cryptography.

The points are written in a formal tone without any emojis or external links as required. Let me know if you would like me to modify or add any other points.