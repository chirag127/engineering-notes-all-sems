### Auto-associative and hetero-associative memory

- Auto-associative memory is a type of memory that retrieves the same pattern Y given an input pattern X, i.e., Y = X  .
- Auto-associative memory is useful for de-noising or removing interference from the input and can be used to determine whether the given input is “known” or “unknown”.
- Auto-associative memory can be implemented by a single layer neural network in which the input training vector and the output target vectors are the same.
- Hetero-associative memory is a type of memory that retrieves a stored pattern Y given an input pattern X such that Y ≠ X  .
- Hetero-associative memory is useful for mapping or correlating different patterns that are related to each other.
- Hetero-associative memory can be implemented by a bidirectional associative memory (BAM) network, which is a two-layer neural network that can store and recall pairs of patterns .
- The following diagram illustrates the difference between auto-associative and hetero-associative memory:

```
+----------------+       +----------------+
|                |       |                |
|   Input X      |       |   Input X      |
|                |       |                |
+----------------+       +----------------+
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
       |                       |
+----------------+       +----------------+
|                |       |                |
|   Output Y     |       |   Output Y     |
|                |       |                |
+----------------+       +----------------+

Auto-associative memory          Hetero-associative memory
Y = X                           Y ≠ X
```