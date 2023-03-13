The following is a detailed ASCII diagram for Introduction to group for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security.

### Introduction to group

A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. For example, the set of integers with the operation of addition is a group.

```
+ | -2 -1  0  1  2
--+----------------
-2| -4 -3 -2 -1  0
-1| -3 -2 -1  0  1
 0| -2 -1  0  1  2
 1| -1  0  1  2  3
 2|  0  1  2  3  4
```

### Introduction to field

A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as the commutative and distributive laws. For example, the set of rational numbers with the usual operations of addition and multiplication is a field.

```
+ |  1  2  3
--+-----------
 1|  2  3  4
 2|  3  4  5
 3|  4  5  6

x |  1  2  3
--+-----------
 1|  1  2  3
 2|  2  4  6
 3|  3  6  9
```

### Introduction to finite field of the form GF(p)

A finite field is a field that has a finite number of elements. A finite field of the form GF(p) is a field that has p elements, where p is a prime number. The elements of GF(p) are the integers from 0 to p-1, and the operations of addition and multiplication are performed modulo p. For example, GF(5) is a finite field with 5 elements: 0, 1, 2, 3, and 4.

```
+ |  0  1  2  3  4
--+----------------
 0|  0  1  2  3  4
 1|  1  2  3  4  0
 2|  2  3  4  0  1
 3|  3  4  0  1  2
 4|  4  0  1  2  3

x |  0  1  2  3  4
--+----------------
 0|  0  0  0  0  0
 1|  0  1  2  3  4
 2|  0  2  4  1  3
 3|  0  3  1  4  2
 4|  0  4  3  2  1
```

### Introduction to modular arithmetic

Modular arithmetic is a system of arithmetic where numbers are reduced to a fixed range by using the remainder operation. For example, in modulo 5 arithmetic, the numbers 0, 5, 10, 15, etc. are all equivalent, and are denoted by 0 mod 5. Similarly, 1, 6, 11, 16, etc. are all equivalent, and are denoted by 1 mod 5, and so on. Modular arithmetic can be used to perform operations on finite fields, such as GF(p).

```
5 mod 5 = 0
6 mod 5 = 1
7 mod 5 = 2
8 mod 5 = 3
9 mod 5 = 4
10 mod