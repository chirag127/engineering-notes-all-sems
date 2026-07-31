### Quantum Search Algorithms

Quantum search algorithms are a class of algorithms that use the principles of quantum mechanics to search for a specific item in an unsorted database. One of the most well-known quantum search algorithms is Grover's algorithm, which was created by Lov Grover in 1996.

- Grover's algorithm is quadratically faster than its classical counterpart, requiring only O(√N) operations to search a database of N items .
- The algorithm uses a binary function, f(x), with the property that f(x) = 1 if and only if x is the label of the object being searched for .
- Grover's algorithm is also known as the quantum search algorithm and is used for unstructured search .
- It finds, with high probability, the unique input to a black box function that produces a particular output value, using just O(√N) evaluations of the function, where N is the size of the function's domain .
- Search is one of the most commonly used primitives in quantum algorithm design. It is known that the quadratic speedups provided by Grover's algorithm are optimal, and no faster quantum algorithms for search exist .
- Quantum walks are powerful tools for building quantum search algorithms or quantum sampling algorithms named the construction of quantum stationary state. However, the success probability of those algorithms is far from 1. Amplitude amplification is usually used to amplify the success probability .