### Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, following certain rules and properties.
- A finite field has a finite number of elements, denoted by q. The order of a finite field must be a power of a prime number, i.e., q = p^n, where p is a prime number and n is a positive integer.
- A finite field of the form GF(p) is a special case where n = 1, i.e., q = p. It is also called the prime field of order p.
- GF(p) consists of the integers from 0 to p-1, with arithmetic operations performed modulo p. That is, the result of any operation is the remainder of dividing by p.
- For example, GF(5) = {0, 1, 2, 3, 4}, and 2 + 3 = 0 (mod 5), 2 - 3 = 4 (mod 5), 2 * 3 = 1 (mod 5), 2 / 3 = 4 (mod 5), where 4 is the multiplicative inverse of 3 modulo 5, i.e., 4 * 3 = 1 (mod 5).
- GF(p) satisfies all the axioms of a field, such as commutativity, associativity, distributivity, identity, inverse and closure. It is also a commutative ring and an abelian group under both addition and multiplication.
- Finite fields of the form GF(p) are important for cryptography because they provide a simple and efficient way to perform arithmetic operations on large numbers, and they have many useful properties, such as Fermat's little theorem, Euler's theorem, and the Chinese remainder theorem.