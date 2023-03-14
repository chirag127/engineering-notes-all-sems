I am Sydney, your AI assistant. I can help you with drawing ASCII diagrams for cryptography. Here is a possible diagram for Unit 2, based on the search results and my own knowledge. I have used the Graph::Easy module to convert dot files to ASCII.

```
+-----------------+     +-----------------+     +-----------------+
| Group           |     | Field           |     | Finite Field    |
|                 |     |                 |     | of the form     |
| A set of        |     | A set of        |     | GF(p)           |
| elements with   |     | elements with   |     |                 |
| a binary        |     | two binary      |     | A field with    |
| operation that  |     | operations that |     | a finite number |
| satisfies       |     | satisfy         |     | of elements,    |
| closure,        |     | closure,        |     | usually a prime |
| associativity,  |     | associativity,  |     | number p.       |
| identity, and   |     | identity,       |     |                 |
| invertibility.  |     | invertibility,  |     | Operations are  |
|                 |     | commutativity,  |     | performed       |
| Examples:       |     | and distributivity.   | modulo p.       |
| (Z, +),         |     |                 |     |                 |
| (Z, x),         |     | Examples:       |     | Examples:       |
| (R, +),         |     | (Q, +, x),      |     | GF(2), GF(3),   |
| (R, x).         |     | (R, +, x),      |     | GF(5), etc.     |
|                 |     | (C, +, x),      |     |                 |
|                 |     | (Z_p, +, x).    |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

```
+-----------------+     +-----------------+     +-----------------+
| Modular         |     | Prime and       |     | Extended        |
| arithmetic      |     | relative prime  |     | Euclidean       |
|                 |     | numbers         |     | Algorithm       |
| Performing      |     |                 |     |                 |
| arithmetic      |     | A prime number  |     | An algorithm    |
| operations on   |     | is a natural    |     | that finds the  |
| the remainder   |     | number that has |     | greatest common |
| of the division |     | exactly two     |     | divisor of two  |
| of two numbers. |     | divisors: 1 and |     | numbers and     |
|                 |     | itself.         |     | also the linear |
| Examples:       |     |                 |     | combination of  |
| 7 mod 3 = 1,    |     | Examples:       |     | them using      |
| 12 mod 5 = 2,   |     | 2, 3, 5, 7, 11, |     | their           |
| 15 mod 4 = 3.   |     | 13, etc.        |     | coefficients.   |
|                 |     |                 |     |                 |
|                 |     | Two numbers are |     | Example:        |
|                 |     | relative prime  |     | gcd(30, 12) = 6 |
|                 |     | (or coprime)    |     | = 2 x 30 - 5 x  |
|                 |     | if their        |     | 12.             |
|                 |     | greatest common |     |                 |
|                 |     | divisor is 1.   |     |                 |
|                 |     |                 |     |                 |
|                 |     | Example:        |     |                 |
|                 |     | 8 and 15 are    |     |                 |
|                 |     | coprime.        |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

```
+-----------------+     +-----------------+     +-----------------+
| AES encryption  |     | Fermat's and    |     | Primality       |
| and