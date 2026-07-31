# Axioms and Theorems of Boolean algebra

Boolean algebra is a branch of algebra that deals with the manipulation of logical expressions and the properties of binary operations. It is used in the design of digital circuits and computer algorithms. The axioms and theorems of Boolean algebra are the fundamental rules that govern the manipulation of logical expressions.

## Axioms of Boolean algebra

1. **Commutative Law**: The order of the operands does not affect the result of the operation. This law applies to both the AND and OR operations.
    - A + B = B + A
    - A * B = B * A

2. **Associative Law**: The way the operands are grouped does not affect the result of the operation. This law applies to both the AND and OR operations.
    - (A + B) + C = A + (B + C)
    - (A * B) * C = A * (B * C)

3. **Distributive Law**: The AND operation distributes over the OR operation and vice versa.
    - A * (B + C) = (A * B) + (A * C)
    - A + (B * C) = (A + B) * (A + C)

4. **Identity Law**: The identity element for the AND operation is 1 and for the OR operation is 0.
    - A * 1 = A
    - A + 0 = A

5. **Complement Law**: Every element has a complement, which when combined with the original element using the AND operation results in 0 and using the OR operation results in 1.
    - A * A' = 0
    - A + A' = 1

6. **Absorption Law**: An element absorbs itself when combined using the AND operation with itself ORed with another element, or when combined using the OR operation with itself ANDed with another element.
    - A * (A + B) = A
    - A + (A * B) = A

7. **De Morgan's Law**: The complement of the AND of two elements is equal to the OR of the complements of the elements, and the complement of the OR of two elements is equal to the AND of the complements of the elements.
    - (A * B)' = A' + B'
    - (A + B)' = A' * B'

## Theorems of Boolean algebra

1. **Idempotent Law**: An element combined with itself using the AND or OR operation results in the element itself.
    - A * A = A
    - A + A = A

2. **Involution Law**: The complement of the complement of an element is the element itself.
    - (A')' = A

3. **Double Negation Law**: The negation of the negation of an element is the element itself.
    - ¬(¬A) = A

4. **Redundancy Law**: An element combined with itself using the AND operation ORed with another element is equal to the element itself ORed with the other element.
    - (A * A) + B = A + B

5. **Consensus Law**: The AND of two elements ORed with the AND of the complement of the first element and a third element is equal to the AND of the two elements ORed with the third element.
    - (A * B) + (A' * C) = (A * B) + C

6. **Adjacency Law**: The OR of two elements ANDed with the OR of the complement of the first element and a third element is equal to the OR of the two elements ANDed with the third element.
    - (A + B) * (A' + C) = (A + B) * C

These are the axioms and theorems of Boolean algebra that are used in the manipulation of logical expressions. They are the fundamental rules that govern the behavior of binary operations and are essential for understanding the properties of Boolean algebra. These concepts are important for the study of Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic.