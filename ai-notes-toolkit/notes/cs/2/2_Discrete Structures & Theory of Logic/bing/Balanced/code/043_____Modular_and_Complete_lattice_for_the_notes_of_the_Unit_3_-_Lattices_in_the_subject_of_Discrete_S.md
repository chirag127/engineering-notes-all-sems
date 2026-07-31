# Modular and Complete Lattice

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** (glb) and a **least upper bound** (lub). The glb of two elements $a$ and $b$ is denoted by $a \wedge b$ and the lub by $a \vee b$.
- A **complete lattice** is a lattice in which **all subsets** have both a glb and a lub. The glb of a subset $S$ is denoted by $\bigwedge S$ and the lub by $\bigvee S$.
- A lattice is **modular** if it satisfies the following property: for any elements $a$, $b$, and $c$ in the lattice, if $a \leq c$, then $a \vee (b \wedge c) = (a \vee b) \wedge c$.  
- A modular lattice can be seen as a generalization of the lattice of subspaces of a vector space, where the glb and lub are given by the intersection and sum of subspaces, respectively.
- A modular lattice has a **composition sequence**, which is a finite sequence of elements $a_0, a_1, \dots, a_n$ such that $a_0 = 0$, $a_n = 1$, and $a_i \vee a_{i+1} = a_{i+1}$ for all $i$.
- A modular lattice has a **dimension function**, which is an integer-valued function $d$ such that $d(a \vee b) + d(a \wedge b) = d(a) + d(b)$ and such that if the interval $[a, b]$ is prime, it follows that $d(b) = d(a) + 1$.

: CitizenChoice. https://citizenchoice.in/course/Discrete-Structures-and-Theory-of-Logic/Unit%203-DSTL/Lattices-1
: Modular lattice - Encyclopedia of Mathematics. https://encyclopediaofmath.org/wiki/Modular_lattice
: Modular lattice - Wikipedia. https://en.wikipedia.org/wiki/Modular_lattice
: 13.2: Lattices - Mathematics LibreTexts. https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Applied_Discrete_Structures_(Doerr_and_Levasseur)/13%3A_Boolean_Algebra/13.02%3A_Lattices