### Modular and Complete Lattice

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** (GLB) and a **least upper bound** (LUB). The GLB of two elements $a$ and $b$ is denoted by $a \wedge b$ and the LUB by $a \vee b$.
- A **complete lattice** is a lattice in which **all subsets** have both a GLB and a LUB. The GLB of a subset $S$ is denoted by $\bigwedge S$ and the LUB by $\bigvee S$. A complete lattice has a **top element** ($\top$) and a **bottom element** ($\bot$) such that $\top = \bigvee L$ and $\bot = \bigwedge L$.
- A **modular lattice** is a lattice that satisfies the **modular law**: $a \vee (b \wedge c) = (a \vee b) \wedge c$ whenever $a \leq c$. This law is an abstraction of the **second isomorphism theorem** in algebra, which states that for any submodules $A$, $B$ and $C$ of a module $M$, if $A \subseteq C$, then $(A + B) / B \cong A / (A \cap B)$.
- A modular lattice can also be characterized by the following equivalent properties:
  - For any elements $a$, $b$ and $c$ in the lattice, if $a \leq b$, then there exists an element $d$ such that $a \vee d = b$ and $a \wedge d = c \wedge b$.
  - For any elements $a$, $b$ and $c$ in the lattice, if $a \leq b$, then $a \vee (b \wedge c) = b \wedge (a \vee c)$.
  - The lattice has a **dimension function** $d$, i.e. an integer-valued function such that $d(a \vee b) + d(a \wedge b) = d(a) + d(b)$ and such that if the interval $[a, b]$ is **prime**, it follows that $d(b) = d(a) + 1$.
  - The lattice is **distributive**, i.e. it satisfies the **distributive law**: $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$ for any elements $a$, $b$ and $c$ in the lattice.
- Examples of modular lattices include:
  - The **subspaces** of a vector space (and more generally the **submodules** of a module over a ring).
  - The **ideals** of a commutative ring.
  - The **normal subgroups** of a group.
  - The **subalgebras** of an algebraic structure.
  - The **power set** of a finite set with the **subset relation**.
  - The **divisors** of a positive integer with the **divisibility relation**.