The following is a detailed ASCII diagram for Introduction to group for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security.

### Introduction to group

A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. For example, the set of integers with the operation of addition is a group, because:

- Closure: For any two integers a and b, a + b is also an integer.
- Associativity: For any three integers a, b, and c, (a + b) + c = a + (b + c).
- Identity: There exists an integer 0 such that for any integer a, a + 0 = 0 + a = a.
- Inverse: For any integer a, there exists an integer -a such that a + (-a) = (-a) + a = 0.

A group is called abelian if it also satisfies the property of commutativity, that is, for any two elements a and b, a * b = b * a, where * is the group operation. The set of integers with addition is an abelian group.

A group is called finite if it has a finite number of elements. The order of a finite group is the number of elements in the group. For example, the set {0, 1, 2, 3} with the operation of addition modulo 4 is a finite group of order 4.

A subgroup is a subset of a group that is also a group under the same operation. For example, the set {0, 2} is a subgroup of the group {0, 1, 2, 3} with addition modulo 4, because it satisfies the four properties of a group.

A group diagram is a way of representing the group operation in a table. For example, the group diagram for the group {0, 1, 2, 3} with addition modulo 4 is:

```
+ | 0 1 2 3
-----------
0 | 0 1 2 3
1 | 1 2 3 0
2 | 2 3 0 1
3 | 3 0 1 2
```

### Introduction to field

A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the following properties:

- Closure: For any two elements a and b, a + b and a * b are also elements of the field.
- Associativity: For any three elements a, b, and c, (a + b) + c = a + (b + c) and (a * b) * c = a * (b * c).
- Commutativity: For any two elements a and b, a + b = b + a and a * b = b * a.
- Identity: There exist two distinct elements 0 and 1 such that for any element a, a + 0 = 0 + a = a and a * 1 = 1 * a = a.
- Inverse: For any element a, there exists an element -a such that a + (-a) = (-a) + a = 0. For any nonzero element a, there exists an element a^-1 such that a * a^-1 = a^-1 * a = 1.
- Distributivity: For any three elements a, b, and c, a * (b + c) = (a * b) + (a * c) and (a + b) * c = (a * c) + (b * c).

A field is called finite if it has a finite number of elements. The order of a finite field is the number of elements in the field. It can be shown that the order of a finite field must be a power of a prime number, that is, p^n for some prime p and positive integer n. A finite field of order p^n is denoted by GF(p^n), where GF stands for Galois field.

A subfield is a subset of a field that is also a field under the same operations. For example, the