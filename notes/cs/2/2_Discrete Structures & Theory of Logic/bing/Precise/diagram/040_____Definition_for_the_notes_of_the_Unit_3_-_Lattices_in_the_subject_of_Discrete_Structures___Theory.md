### Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set in which every two elements have a unique supremum (also called a least upper bound or join) and a unique infimum (also called a greatest lower bound or meet).
- An element is said to **cover** another element if the first element is greater than the second element, and there is no element in between the two in the ordering.
- A lattice is said to be **complete** if all subsets have both a supremum and an infimum.
- A lattice is said to be **distributive** if the meet and join operations distribute over each other.
- A lattice is said to be **modular** if, for all elements x, y, and z, if x is less than or equal to z, then the join of x and the meet of y and z is equal to the meet of y and the join of x and z.
- A lattice is said to be **complemented** if every element has a unique complement, which is an element such that the meet of the two elements is the bottom element and the join of the two elements is the top element.
- A lattice is said to be **bounded** if it has a top element and a bottom element.
- A lattice is said to be **algebraic** if it is complete and every element is the join of compact elements, where an element is said to be compact if it is the join of a finite set of elements.
- A lattice is said to be **continuous** if it is complete and every element is the join of way-below elements, where an element is said to be way-below another element if, for every directed set that has the second element as its supremum, there is an element in the directed set that is greater than or equal to the first element.