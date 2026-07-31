### Quantum Search Algorithms

Quantum search algorithms are a type of quantum algorithm that can be used to search for a specific item within an unstructured database. These algorithms are quadratically faster than their classical counterparts, requiring only O(√N) operations, where N is the number of elements in the database .

One of the most well-known quantum search algorithms is Grover's algorithm, which was created by Lov Grover. This algorithm can find, with high probability, the unique input to a black box function that produces a particular output value, using just O(√N) evaluations of the function, where N is the size of the function's domain .

The centerpiece of the quantum search algorithm is a binary function, f(x), with the property that f(x) = 1 if and only if x is the label of the object we are searching for, f(τ) = 1 .

There are also hybrid quantum-classical search algorithms, which combine the strengths of both quantum and classical algorithms to achieve even better performance .

Quantum walks are another powerful tool for building quantum search algorithms or quantum sampling algorithms named the construction of quantum stationary state. However, the success probability of those algorithms are all far away from 1. Amplitude amplification is usually used to amplify success probability .