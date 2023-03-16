# Quantum Search Algorithms

Quantum search algorithms are a type of quantum algorithm that can be used to search for a specific item in an unstructured database. These algorithms are quadratically faster than their classical counterparts, requiring only O(√N) operations, where N is the number of elements in the database .

One of the most well-known quantum search algorithms is Grover's algorithm. This algorithm is able to find, with high probability, the unique input to a black box function that produces a particular output value, using just O(√N) evaluations of the function, where N is the size of the function's domain .

Search is one of the most commonly used primitives in quantum algorithm design. It is known that the quadratic speedups provided by Grover's algorithm are optimal, and no faster quantum algorithms for search exist .

Quantum walks are also powerful tools for building quantum search algorithms or quantum sampling algorithms. However, the success probability of those algorithms is not always close to 1. Amplitude amplification is usually used to amplify the success probability .