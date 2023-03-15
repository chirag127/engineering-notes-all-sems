 Here are the notes for the given topic:

### Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers

Group: A set of elements with an associative binary operation defined on them is called a group. The identity element and inverse elements must exist for each element in the group.
Examples: Set of integers under addition, set of non-zero real numbers under multiplication, set of permutations of a finite set under composition of mappings, etc.

Field: A set F together with two binary operations (addition and multiplication) is called a field if:
(i) (F, +) forms an abelian group.
(ii) (F, *) is a semi-group in which every element has a multiplicative inverse.
(iii) Multiplication is distributive over addition, i.e. a*(b + c) = a*b + a*c for all a, b, c in F.
Examples: Rational numbers Q, real numbers R, complex numbers C, finite fields like GF(p), etc.

Finite field of the form GF(p): A finite field of order p is a field with p elements where p is a prime number. The elements of GF(p) are {0, 1, 2, ..., p − 1} under modulo p addition and multiplication. The operations are well-defined, the field properties are satisfied and it contains p elements. Used extensively in computer science and cryptography.

Modular arithmetic: Arithmetic on integers that wrap around upon reaching a certain value called the modulus. The results of addition, subtraction and multiplication are the remainders after division by the modulus. Useful for its properties and applications in cryptography.

Prime and relative prime numbers:
Prime number: A positive integer greater than 1 that is only divisible by 1 and itself.
Relative prime numbers: Two integers a and b are said to be relatively prime if their greatest common divisor is 1. Also known as mutually prime.

Extended Euclidean Algorithm: An algorithm to find the greatest common divisor (GCD) of two integers which also gives the coefficients of Bézout's identity. Useful in cryptography for calculating inverse elements in a group or field.