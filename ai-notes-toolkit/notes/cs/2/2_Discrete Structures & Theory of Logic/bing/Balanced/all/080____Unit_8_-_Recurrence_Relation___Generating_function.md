## Unit 8 - Recurrence Relation & Generating function

- A **recurrence relation** is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.
- A **generating function** is a formal power series that encodes the information of a sequence in its coefficients.
- Recurrence relations and generating functions are useful tools for analyzing and solving problems involving discrete structures, such as combinatorics, algorithms, and cryptography.

### Examples of recurrence relations

- The **Fibonacci sequence** is defined by the recurrence relation:

  - F<sub>0</sub> = 0
  - F<sub>1</sub> = 1
  - F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> for n > 1

- The **factorial function** is defined by the recurrence relation:

  - n! = 1 for n = 0
  - n! = n * (n-1)! for n > 0

- The **Tower of Hanoi** problem is defined by the recurrence relation:

  - T<sub>1</sub> = 1
  - T<sub>n</sub> = 2 * T<sub>n-1</sub> + 1 for n > 1

### Examples of generating functions

- The generating function for the sequence {a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, ...} is:

  - A(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> + ...

- The generating function for the Fibonacci sequence is:

  - F(x) = x / (1 - x - x<sup>2</sup>)

- The generating function for the factorial function is:

  - F(x) = e<sup>x</sup>

- The generating function for the Tower of Hanoi problem is:

  - T(x) = (1 - x) / (1 - 2x - x<sup>2</sup>)

### Properties of generating functions

- Generating functions can be manipulated algebraically to obtain new sequences from existing ones.
- Generating functions can be differentiated and integrated term by term to obtain new coefficients.
- Generating functions can be multiplied and divided to obtain convolution and inverse convolution of sequences.
- Generating functions can be used to solve linear recurrence relations with constant coefficients by finding the roots of the characteristic polynomial.