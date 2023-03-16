### Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, obeying certain rules called axioms.
- A finite field has a finite number of elements, which must be a power of a prime number, such as p, p^2, p^3, etc.
- A finite field of the form GF(p) is the set of integers from 0 to p-1, where p is a prime number, with arithmetic operations performed modulo p  .
- For example, GF(5) is the set {0, 1, 2, 3, 4} with addition and multiplication modulo 5. So, 2 + 3 = 0, 4 * 3 = 2, and 3^-1 = 2 in GF(5).
- A finite field of the form GF(p) has the following properties  :
  - It is commutative, associative and distributive for both addition and multiplication.
  - It has an additive identity (0) and a multiplicative identity (1).
  - Every element has an additive inverse (-a = p-a) and a multiplicative inverse (a^-1 such that a * a^-1 = 1).
  - It is closed under both addition and multiplication, meaning that the result of any operation is always in the field.
  - It has no zero divisors, meaning that if a * b = 0, then either a = 0 or b = 0.
  - It has a unique solution for every linear equation of the form a * x + b = c, where a, b and c are in the field and a is not zero.